import json
import boto3
from collections import defaultdict


def alert(msg: str):
    print("+ ", end='')
    print(msg)


def parseRoute(graph: str):
    src_des_pairs = graph.strip().split(',')

    # map: src -> [des]
    route_map = defaultdict(set)
    for p in src_des_pairs:
        p = p.strip()
        src, des = p.split('->')
        route_map[src].add(des)
    # alert(route_map)

    return route_map


def findShortestDistance(graph: str):
    route_map = parseRoute(graph)
    shortest_distances = defaultdict(int)       # map: (src, des) -> distance

    srcs = list(route_map.keys())
    for src in srcs:
        queue = [(src, 0)]                      # (city, distance)
        visited_cities = set()

        while queue:
            curr_city, curr_dist = queue.pop(0)
            visited_cities.add(curr_city)

            if src != curr_city and (src, curr_city) not in shortest_distances:
                shortest_distances[(src, curr_city)] = curr_dist

            curr_neighbors = route_map[curr_city]
            for neighbor in curr_neighbors:
                if neighbor not in visited_cities:
                    queue.append((neighbor, curr_dist + 1))

    shortest_distance_tab = [(*p[0], p[1]) for p in shortest_distances.items()]
    alert(shortest_distance_tab)

    return shortest_distance_tab


# Lambda handler
def lambda_handler(event, context):
    # Getting the table
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table = dynamodb.Table('MP3-Shortest-Distances')

    # Clear table, ref: https://stackoverflow.com/questions/64187825/how-to-delete-all-the-items-in-the-dynamodb-with-boto3
    flag = True
    while flag:
        scan = table.scan()
        alert("Deleting {} records".format(scan['ScannedCount']))

        flag = 'LastEvaluatedKey' in scan and scan['LastEvaluatedKey']
        with table.batch_writer() as batch:
            for each in scan['Items']:
                batch.delete_item(
                    Key = {
                        'Source': each['Source'],
                        'Destination': each['Destination']
                    }
                )

    # Get shortest distances
    shortest_distance_tab = findShortestDistance(event['graph'])

    # Putting a try/catch to log to user when some error occurs
    try:
        for src, des, dist in shortest_distance_tab:
            table.put_item(
                Item = {
                    'Source': src,
                    'Destination': des,
                    'Distance': int(dist)
                }
            )

        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully uploaded graph!')
        }

    except Exception as e:
        alert(e)
        return {
            'statusCode': 400,
            'body': json.dumps('Error saving the graph!')
        }


if __name__ == '__main__':
    findShortestDistance("Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette,New York->Chicago,New York->Urbana,Lafayette->New York,Urbana->Bloominton")
