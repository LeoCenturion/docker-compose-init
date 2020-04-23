CLIENT_VOL_MNT=$(sudo docker volume inspect dockercomposeinit_client-vol | grep Mount | cut -d ':' -f2| tr -d "\"" | tr -d "," | tr -d " ");
SERVER_VOL_MNT=$(sudo docker volume inspect dockercomposeinit_server-vol | grep Mount | cut -d ':' -f2| tr -d "\"" | tr -d "," | tr -d " " );
mkdir -p "$CLIENT_VOL_MNT/config" && cp ./config/config.yaml "$CLIENT_VOL_MNT/config";
mkdir -p "$SERVER_VOL_MNT/config" &&  cp ./config/config.ini "$SERVER_VOL_MNT/config";
