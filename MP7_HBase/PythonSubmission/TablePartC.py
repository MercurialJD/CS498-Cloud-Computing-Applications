import happybase as hb
import csv

csv_reader = csv.reader(open('input.csv', 'r'))

connection = hb.Connection()
table = connection.table("powers")

for row in csv_reader:
    table.put(
        row[0],
        {
            "personal:hero": row[1],
            "personal:power": row[2],
            "professional:name": row[3],
            "professional:xp": row[4],
            "custom:color": row[5],
        }
    )

connection.close()
