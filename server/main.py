#!/usr/bin/env python3

import os
import time
import logging
import configparser
import sys
from common.server import Server
CONFIG_PATH = ""
DEFAULT_PARAMS = {"SERVER_PORT","SERVER_LISTEN_BACKLOG"}

def parse_param(path, env, param):
	config = configparser.ConfigParser()
	config.read(path)
	print(param)
	print(os.getenv(param))
	try:
		return int(env in config  and config[env][param] or os.getenv(param))
	except KeyError as e:
		raise KeyError("Key was not found. Error: {} .Aborting server".format(e))
	except ValueError as e:
		raise ValueError("Key could not be parsed. Error: {}. Aborting server".format(e))

def parse_config_params(environment):
	""" Parse env variables to find program config params

	Function that search and parse program configuration parameters in the
	program environment variables. If at least one of the config parameters
	is not found a KeyError exception is thrown. If a parameter could not
	be parsed, a ValueError is thrown. If parsing succeeded, the function
	returns a map with the env variables
	"""
	config_path = CONFIG_PATH
	config_params = {}
	parse_param_binded = lambda param: parse_param(config_path, environment, param)

	config_params["port"] = parse_param_binded("SERVER_PORT")
	config_params["listen_backlog"] = parse_param_binded("SERVER_LISTEN_BACKLOG")

	return config_params

def parse_clargs():
	ret = {}
	for arg in sys.argv[1:]:
		s = arg.split("=")
		if len(s[0]) > 0 and len(s[1]) > 0:
			ret[s[0]] = s[1]
	return ret

def main():

	args = parse_clargs();
	initialize_log()
	config_params = parse_config_params(args.get('environment') or 'development')

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
