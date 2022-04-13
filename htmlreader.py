from bot_enums import *

from urllib.request import urlopen

doc_urls = {
			Language.Python: 'https://www.python.org/doc/versions/',
			Language.Java: 'https://docs.oracle.com/en/java/javase/index.html'
		}

class htmlreader:

	def __init__(self, language):
		
		self.url = doc_urls.get(language, None)
		
		if self.url != None:
			page = urlopen(self.url)
			html_bytes = page.read()
			self.html = html_bytes.decode("utf-8")
		else:
			self.html = None