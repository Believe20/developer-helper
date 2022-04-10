from doc_finder import doc_finder
from wait_response import wait_response

import discord
import config

from typing import List

python_docs_url = 'https://www.python.org/doc/versions/'

client = discord.Client()
document_commands = ['-python', '-java', '-c', '-c++', '-c#']
finders: List[wait_response] = []

@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
	global finders

	if message.author == client.user:
		return

	message.content = message.content.lower()

	for f in finders:
		if f.waiting:
			await f.send(message)
		else:
			finders.remove(f)

	if message.content in document_commands:
		d = doc_finder(message)
		finders.append(d)
		await d.send_initial_message()

	else:

		if message.content.startswith('-hello'):
			await message.channel.send('Hi.')

client.run(config.TOKEN)