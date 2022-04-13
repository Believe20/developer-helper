from wait_response import wait_response
from htmlreader import htmlreader
from bot_enums import *

import discord
from urllib.request import urlopen
import re


class doc_finder(wait_response):

	doc_url = None
	language = None

	def __init__(self, channel: discord.channel):
		super().__init__()
		

		html = htmlreader(self.language)
		self.html = html.html

		if self.html != None:
			self.versions = self.get_versions()
			self.channel = channel
		else:
			self.waiting = False
		
	def get_versions(self):
		return []

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

		if mcon in self.versions:
			await self.channel.send(self.doc_url + mcon + '/\n')