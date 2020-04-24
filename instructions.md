# Presentación del trabajo.
Requerimientos:
	docker, docker-compose, python3, pyyaml, bash

#Ejercicio 1 y 1.1
	Para levantar más de un cliente se debe pasar el parametro CLIENT al ejecutar docker-compose-up. Por defecto se ejecuta un cliente. Los servicios (y contenedores) correspondientes se nombran como: cliente, cliente2, etc...
	Los identificadores se signan de la siguente forma: ID1 para cliente, ID2 par cliente2, etc...
	Ejemplo:
		make docker-compose-up CLIENTS=3

#Ejercicio 2
Teniendo los archivos config.ini para el servidor y config.yaml para el cliente en el directorio /config se corre el comando make inject-config el cual copia los dos archivos. Tener en cuenta que las variables de entorno tienen mayor prioridad que las variables declaradas en los archivos de configuracion

#Ejercicio 3
	sudo make test
