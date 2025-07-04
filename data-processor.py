import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='<json>', help='configuration file')
arg = parser.parse_args()



with open(arg.file) as fp: config = json.load(fp)

print(config)

