from finders.doc_finder import doc_finder
from bot_enums import *

import discord

class java_finder(doc_finder):

	doc_url = 'https://docs.oracle.com/javase/'
	language = Language.Java

	def __init__(self, channel: discord.channel):
		super().__init__(channel)

	def get_versions(self):
		versions = []

		start_index = self.html.find('JDK')
		end_index = self.html.find('index.html">JDK 7')

		for i in range(start_index, end_index):
			if self.html[i] == 'h' and self.html[i:i+4] == 'href':
				phrase_start = self.html.find(' ',i)
				phrase_end = self.html.find(' ',phrase_start + 1)
				phrase = self.html[phrase_start + 1:phrase_end]
				versions.append(phrase)

		return versions