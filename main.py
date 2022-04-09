from asyncio.windows_events import NULL
from email.message import Message
import discord
import config

from urllib.request import urlopen
python_docs_url = 'https://www.python.org/doc/versions/'

client = discord.Client()
Versionselect = False
versions = []

@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
	global Versionselect

	if message.author == client.user:
		return

	if message.content.startswith('-hello'):
		await message.channel.send('Hi.')
	
	if Versionselect == True:
		await version_message(message)
	else:
		await check_message(message)

async def check_message(message: discord.Message):
	if message.content.startswith('-python'):
		
		global Versionselect		
		global versions

		Versionselect = True
		def get_versions(html: str):
			start_index = html.find('docs.python.org/release/')
			end_index = html.find('docs.python.org/release/1.4/')

			x = 0
			for i in range(start_index, end_index):
				if html[i] == 'P' and html[i:i+6] == 'Python':
					phrase_end = html.find('<',i)
					phrase = html[i:phrase_end]
					#if phrase[phrase.find('.',phrase.find('.')+1)] == '.' and phrase[phrase.find('.',phrase.find('.')+1)+1] == '0' or len(phrase) < 11:
					if phrase[phrase.find('.')+1] != x:
						versions.append(html[i:phrase_end])
						x = phrase[phrase.find('.')+1]

			return versions

		page = urlopen(python_docs_url)
		html_bytes = page.read()
		html = html_bytes.decode("utf-8")
		versions = get_versions(html)
		versions_string = '\n - '.join(versions)
		await message.channel.send('Python selected! Which version do you need to know about?\n - ' + versions_string)

	if message.content.startswith('-java SE'):

		global Versionselect
		global versions

		


async def version_message(message: discord.Message):
	global Versionselect
	global versions

	mcon = message.content
	if Versionselect == True:
		for i in range(len(versions)): 
			if message.content == versions[i]:
				await message.channel.send('https://docs.python.org/release/' + mcon[mcon.find(' ') + 1 : len(mcon)] + '/\n')
				Versionselect = False
				versions = []
				return




client.run(config.TOKEN)