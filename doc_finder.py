from wait_response import wait_response
from htmlreader import htmlreader
from bot_enums import *

import discord
from urllib.request import urlopen
import re


class doc_finder(wait_response):

	def __init__(self, identifier: discord.Message):
		super().__init__()
		self.language = {
			'-python': Language.Python,
			'-java': Language.Java,
			'-c': Language.C,
			'-c++': Language.C_Plus_Plus,
			'-c#': Language.C_Sharp
		}.get(identifier.content)

		html = htmlreader(self.language)
		self.html = html.html

		if self.html != None:
			self.versions = self.get_versions(self.language)
			self.channel = identifier.channel
		else:
			self.waiting = False
		

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

		if language == Language.Java:
			start_index = self.html.find('JDK')
			end_index = self.html.find('index.html">JDK 7')

			x = 0
			for i in range(start_index, end_index):
				if self.html[i] == 'h' and self.html[i:i+4] == 'href':
					phrase_start = self.html.find(' ',i)
					phrase_end = self.html.find(' ',phrase_start + 1)
					phrase = self.html[phrase_start + 1:phrase_end]
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
		mcon = re.sub('[^\d\.]', '', message.content)

		if self.language == Language.Python:
			if mcon in self.versions:
				await self.channel.send('https://docs.python.org/release/' + mcon + '/\n')

		if self.language == Language.Java:	
			if mcon in self.versions:
				await self.channel.send('https://docs.oracle.com/javase/' + mcon + '/')