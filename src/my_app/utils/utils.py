"""
utils.py is used for small helper methods to reduce redundancy
"""
import yaml

def get_config_yaml():
    with open("../../config.yaml", 'r') as stream:
        return yaml.safe_load(stream)