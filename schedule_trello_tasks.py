import requests
from pathlib import Path
import cronex
import time

# constants
input_file_path = 'tasks.txt'

trello_key =
trello_token =

list_id = '5ea37d5a04b0754aea510964'

def create_card(name, list_id):
	url = "https://api.trello.com/1/cards"
	querystring = {
		"name":name,
		"idList":list_id,
		"keepFromSource":"all",
		"pos":'top',
		"key":trello_key,"token":trello_token
	}
	response = requests.request("POST", url, params=querystring)

p = Path(input_file_path)

for task in [line for line in p.read_text().splitlines()]:
	cron = cronex.CronExpression(task)
	if cron.check_trigger(time.gmtime(time.time())[:5]):
		create_card(cron.comment, list_id)
		print(cron.comment)
