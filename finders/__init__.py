from finders.doc_finder import doc_finder
from finders.python_finder import python_finder
from finders.java_finder import java_finder

import discord

class finder:

	def get(identifier: discord.Message) -> doc_finder:

		return {
				'-python': python_finder,
				'-java': java_finder,
				'-c': None,
				'-c++': None,
				'-c#': None
			}.get(identifier.content)(identifier.channel)