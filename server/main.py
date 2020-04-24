#!/usr/bin/env python3

import os
import time
import logging
import configparser
import sys
from common.server import Server
CONFIG_PATH = "/config/config.ini"

def parse_param(path, env, param):
	"""
	Parse parameters from the config file and the enviroment and returns
	a dictionary with key value pairs. For any given parameter the falue from the enviroment is figen preference to the one from the configuration file
	"""
	config = configparser.ConfigParser()
	config.read(path)
	print(config.sections())
	print("{} config: {}".format(param, env in config  and config[env][param]) )
	print("{} env: {}".format(param, os.getenv(param,None)))
	try:
		return int(os.getenv(param) or env in config  and config[env][param])
	except KeyError as e:
		raise KeyError("Key was not found. Error: {} .Aborting server".format(e))
	except ValueError as e:
		raise ValueError("Key could not be parsed. Error: {}. Aborting server".format(e))

def parse_config_params(environment, config_path):
	""" Parse env variables to find program config params

	Function that search and parse program configuration parameters in the
	program environment variables. If at least one of the config parameters
	is not found a KeyError exception is thrown. If a parameter could not
	be parsed, a ValueError is thrown. If parsing succeeded, the function
	returns a map with the env variables
	"""
	config_params = {}
	parse_param_binded = lambda param: parse_param(config_path, environment, param)

	config_params["port"] = parse_param_binded("SERVER_PORT")
	config_params["listen_backlog"] = parse_param_binded("SERVER_LISTEN_BACKLOG")

	return config_params

def parse_clargs():
	"""
	Parse console line arguments and returns a dictionary with key value pairs
	"""
	ret = {}
	for arg in sys.argv[1:]:
		s = arg.split("=")
		if len(s[0]) > 0 and len(s[1]) > 0:
			ret[s[0]] = s[1]
	return ret

def main():

	args = parse_clargs();
	initialize_log()
	config_params = parse_config_params(args.get('environment') or 'DEVELOPMENT', args.get('config') or CONFIG_PATH)

	# Initialize server and start server loop
	server = Server(config_params["port"], config_params["listen_backlog"])
	server.run()

def initialize_log():
	"""
	Python custom logging initialization

	Current timestamp is added to be able to identify in docker
	compose logs the date when the log has arrived
	"""
	logging.basicConfig(
		format='%(asctime)s %(levelname)-8s %(message)s',
		level=logging.INFO,
		datefmt='%Y-%m-%d %H:%M:%S',
	)


if __name__== "__main__":
	main()
