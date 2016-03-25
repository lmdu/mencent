#!/usr/bin/env python
import htmlPy

class Engine(htmlPy.Object):
	def __init__(self, app):
		super(BackEnd, self).__init__()
		self.app = app
	
	@htmlPy.Slot()
	def say_hello_world(self):
		self.app.html = u"hello,world"