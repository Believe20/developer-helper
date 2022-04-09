import discord
import config

from urllib.request import urlopen
python_docs_url = 'https://www.python.org/doc/versions/'

client = discord.Client()

@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
	if message.author == client.user:
		return

	if message.content.startswith('-hello'):
		await message.channel.send('Hi.')
	
	await check_message(message)

async def check_message(message: discord.Message):
	if message.content.startswith('-python'):

		def get_versions(html: str):
			start_index = html.find('docs.python.org/release/')
			end_index = html.find('docs.python.org/release/2.5.4/')

			versions = []
			for i in range(start_index, end_index):
				if html[i] == 'P' and html[i:i+6] == 'Python':
					phrase = html[i: i+20]
					phrase_end = phrase.find('<')
					versions.append(phrase[i:i+phrase_end])

			return versions

		page = urlopen(python_docs_url)
		html_bytes = page.read()
		html = html_bytes.decode("utf-8")
		versions = get_versions(html)
		versions_string = '\n - '.join(versions)
		await message.channel.send('Python selected! Which version do you need to know about?\n - ' + versions_string)

client.run(config.TOKEN)