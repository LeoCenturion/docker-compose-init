# Presentación del trabajo.

#Ejercicio 1 y 1.1
	Para levantar más de un cliente se debe pasar el parametro CLIENT al ejecutar docker-compose-up. Por defecto se ejecuta un cliente. Los servicios (y contenedores) correspondientes se nombran como: cliente, cliente2, etc...
	Los identificadores se signan de la siguente forma: ID1 para cliente, ID2 par cliente2, etc...
	Ejemplo:
		make docker-compose-up CLIENTS=3

#Ejercicio 2
