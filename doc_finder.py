from wait_response import wait_response

from enum import Enum
import discord
from urllib.request import urlopen
import re

python_docs_url = 'https://www.python.org/doc/versions/'

Language = Enum('Language', 'Python Java C C_Plus_Plus C_Sharp')

class doc_finder(wait_response):

	Versionselect = False

	def __init__(self, identifier: discord.Message):
		super().__init__()
		self.language = {
			'-python': Language.Python,
			'-java': Language.Java,
			'-c': Language.C,
			'-c++': Language.C_Plus_Plus,
			'-c#': Language.C_Sharp
		}.get(identifier.content)

		page = urlopen(python_docs_url)
		html_bytes = page.read()
		self.html = html_bytes.decode("utf-8")

		self.versions = self.get_versions(self.language)
		self.channel = identifier.channel
		

	def get_versions(self, language: Language):
		versions = []

		if language == Language.Python:
			start_index = self.html.find('docs.python.org/release/')
			end_index = self.html.find('docs.python.org/release/1.4/')

			x = 0
			for i in range(start_index, end_index):
				if self.html[i] == 'P' and self.html[i:i+6] == 'Python':
					phrase_end = self.html.find('<',i)
					phrase = self.html[i+7:phrase_end]
					versions.append(phrase)

		return versions

	async def send_initial_message(self):
		lang = {
			Language.Python: 'Python',
			Language.Java: 'Java',
			Language.C: 'C',
			Language.C_Plus_Plus: 'C++',
			Language.C_Sharp: 'C#'
		}.get(self.language)
		await self.channel.send(f'{lang} selected! Which version do you need to know about?')

	async def send(self, message: discord.Message):
		
		self.waiting = False

		if self.language == Language.Python:
			mcon = re.sub('[^\d\.]', '', message.content)
			if message.content in self.versions:
				await self.channel.send('https://docs.python.org/release/' + mcon + '/\n')