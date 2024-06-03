from kubernetes import client, config
from flask import Flask,request
from os import path
import yaml, random, string, json
import sys
import json

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
v1 = client.CoreV1Api()
app = Flask(__name__)
# app.run(debug = True)

@app.route('/config', methods=['GET'])
def get_config():
    pods = []

    # your code here
    pods_all_info = v1.list_pod_for_all_namespaces(watch=False)

    for i in pods_all_info.items:
        pods.append({
            'node': i.spec.node_name,
            'ip': i.status.pod_ip,
            'namespace': i.metadata.namespace,
            'name': i.metadata.name,
            'status': i.status.phase
        })

    output = {"pods": pods}
    output = json.dumps(output)

    return output

@app.route('/img-classification/free', methods=['POST'])
def post_free():
    # your code here
    free_yaml = "free_service.yaml"
    with open(free_yaml) as f:
        dep = yaml.safe_load(f)

        k8s_apps_v1 = client.BatchV1Api()
        resp = k8s_apps_v1.create_namespaced_job(body=dep, namespace="free-service")

        print_str = "Success! Free job {} created.".format(resp.metadata.labels["job-name"])
        print(print_str)

    return print_str


@app.route('/img-classification/premium', methods=['POST'])
def post_premium():
    # your code here
    premium_yaml = "premium_service.yaml"
    with open(premium_yaml) as f:
        dep = yaml.safe_load(f)

        k8s_apps_v1 = client.BatchV1Api()
        resp = k8s_apps_v1.create_namespaced_job(body=dep, namespace="default")

        print_str = "Success! Premium job {} created.".format(resp.metadata.labels["job-name"])
        print(print_str)

    return print_str

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
