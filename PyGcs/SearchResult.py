# -*- coding: utf-8 -*-

class SearchResult:

	kind = ""
	title = ""
	display_link = ""
	html_title = ""
	formatted_url = ""
	html_formatted_url = ""
	# hogehoge
	snippet = ""
	html_snippet = ""
	link = ""
	# hogehoge2

	def __init__(self, data):
		self.set_kind(data["kind"])
		self.set_title(data["title"])
		self.set_display_link(data["displayLink"])
		self.set_html_title(data["htmlTitle"])
		self.set_formatted_url(data["formattedUrl"])
		self.set_html_formatted_url(data["htmlFormattedUrl"])
		self.set_snippet(data["snippet"])
		self.set_html_snippet(data["htmlSnippet"])
		self.set_link(data["link"])

	def get_kind(self):
		return self.kind

	def set_kind(self, kind):
		self.kind = kind

	def get_title(self):
		return self.title

	def set_title(self, title):
		self.title = title

	def get_display_link(self):
		return self.display_link

	def set_display_link(self, display_link):
		self.display_link = display_link

	def get_html_title(self):
		return self.html_title

	def set_html_title(self, html_title):
		self.html_title = html_title

	def get_formatted_url(self):
		return self.formatted_url

	def set_formatted_url(self, formatted_url):
		self.formatted_url = formatted_url

	def get_html_formatted_url(self):
		return self.html_formatted_url

	def set_html_formatted_url(self, html_formatted_url):
		self.html_formatted_url = html_formatted_url

	def get_snippet(self):
		return self.snippet

	def set_snippet(self, snippet):
		self.snippet = snippet

	def get_html_snippet(self):
		return self.html_snippet

	def set_html_snippet(self, html_snippet):
		self.html_snippet = html_snippet

	def get_link(self):
		return self.link

	def set_link(self, link):
		self.link = link