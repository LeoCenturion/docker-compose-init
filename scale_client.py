import yaml
import sys
import copy
with open("docker-compose-dev.yaml", 'r') as stream:
    n_clients = int((len(sys.argv) > 1 and sys.argv[1].split('=')[1]) or 1)
    root = yaml.safe_load(stream)
    client_yaml = copy.deepcopy(root['services']['client'])
    for i in range(2, n_clients+1):
        new_client = copy.deepcopy(client_yaml)
        new_client['container_name'] = 'client{}'.format(i)
        new_client['environment'][0] = 'CLI_ID={}'.format(i)
        root['services']['client{}'.format(i)] = new_client
        yaml.dump(root)
    with open('docker-compose-dev-tmp.yaml', 'w') as out_stream:
        yaml.dump(root, out_stream)
