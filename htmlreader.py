from urllib.request import urlopen

document_commands = ['-python', '-java', '-c', '-c++', '-c#']
doc_urls = ['https://www.python.org/doc/versions/', 'https://docs.oracle.com/en/java/javase/index.html']

class htmlreader:

	def __init__(self, version):
		
		if version == document_commands[0]:
			url = doc_urls[0]
		
		if version == document_commands[1]:
			url = doc_urls[1]

		if version == document_commands[2]:
			url = doc_urls[2]

		if version == document_commands[3]:
			url = doc_urls[3]
		
		if version == document_commands[4]:
			url = doc_urls[4]
		
		page = urlopen(url)
		html_bytes = page.read()
		self.html = html_bytes.decode("utf-8")