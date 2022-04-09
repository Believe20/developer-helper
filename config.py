import json

TOKEN = ''

try:
	file = open('config.json', 'r')
except FileNotFoundError:
	print('Config file not created. Please run config.py.')
	file = None

if file != None:

	configs = json.load(file)

	if 'TOKEN' in configs:
		TOKEN = configs['TOKEN']

	file.close()

if __name__ == '__main__':

	key = input('Enter your discord bot token or press the Enter key to exit.\n> ')
	if key != '':
		configs = {
			'TOKEN': key
		}
		with open('config.json', 'w') as file:
			file.write(json.dumps(configs))