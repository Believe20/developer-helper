from finders.doc_finder import doc_finder
from bot_enums import *

import discord

class python_finder(doc_finder):

	doc_url = 'https://docs.python.org/release/'
	language = Language.Python

	def __init__(self, channel: discord.channel):
		super().__init__(channel)

	def get_versions(self):
		versions = []

		start_index = self.html.find('docs.python.org/release/')
		end_index = self.html.find('docs.python.org/release/1.4/')

		for i in range(start_index, end_index):
			if self.html[i] == 'P' and self.html[i:i+6] == 'Python':
				phrase_end = self.html.find('<',i)
				phrase = self.html[i+7:phrase_end]
				versions.append(phrase)

		return versions

	