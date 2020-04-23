PORT=$(cat docker-compose-dev.yaml | egrep -iu "SERVER_PORT" | cut -d '=' -f2)
SERVER_IP=$(cat docker-compose-dev.yaml | egrep -iu "#server ip" | cut -d ':' -f2 | cut -d '#' -f1)

docker run --network=dockercomposeinit_testing_net --rm alpine:latest sh -c "echo 'test msg' | nc $SERVER_IP $PORT | egrep -ic 'test msg'  | (read line; if [[ \$line -ge 1 ]]; then echo 'server working properly'; else echo 'go fix your server'; fi)"
