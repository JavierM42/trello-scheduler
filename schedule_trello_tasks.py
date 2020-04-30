import requests
from pathlib import Path
import cronex
import time

# constants
input_file_path = 'tasks.txt'

trello_key = '11322ff4ec5de9332fd310f66fc8f314'
trello_token = '8907a912c0c4230642f98aaaa83f4b69fae16ce6e81f2763c60f594481e1ba9f'

list_id = '5e80acbec0a8ab66bb2a3fac'

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
