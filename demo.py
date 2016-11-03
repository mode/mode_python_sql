
import json, requests, datetime, ConfigParser, argparse, sys, csv, yaml
from requests.auth import HTTPBasicAuth


def get_auth(whichAuth):
	with open ('mode.yml', 'r') as f:
		mode = yaml.load(f) 

	token = mode["mode"]["token"]
	password = mode["mode"]["password"]
	auth = (token, password)
	return auth

def get_response_json(url, auth):
	response = requests.get(url, auth=auth)
	return response.json()

def get_mode_results():

	if __name__ == '__main__':
		parser = argparse.ArgumentParser()
		parser.add_argument('-org', '--org')
		parser.add_argument('-reporttoken', '--reporttoken')
		args = parser.parse_args()

	mode_url = 'https://modeanalytics.com'
	if(args.org is not None and args.reporttoken is not None):
		api_url = '/api/' + args.org + '/reports/' + args.reporttoken
	else:
		sys.exit('We did not get your -org or -reporttoken parameters.')

	auth = get_auth('mode')

	url = mode_url + api_url

	print "API URL: " + url

	data = get_response_json(url, auth)

	links = data['_links']
	last_run = links['last_successful_run']
	run_url = last_run['href']	
	url = mode_url + run_url + '/query_runs/'

	data = get_response_json(url, auth)
	
	embedded = data['_embedded']
	query_runs = embedded['query_runs']

	file = open('sql.csv', 'w')
	writer = csv.writer(file, lineterminator='\n')
	writer.writerow(["Query Token", "SQL Query"])

	for x in query_runs:
		token = x['query_token']
		raw = x['raw_source']
		print "Query Token: " + token
		print raw
		print "*************************************"
		writer.writerow([token, raw])

	file.close()

get_mode_results()

