#!/usr/bin/env python
import os
import htmlPy
from PySide import QtGui
from core import Engine

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = htmlPy.AppGUI(title=u"Reference")

app.template_path = os.path.join(BASE_DIR, 'templates/')
app.static_path = os.path.join(BASE_DIR, 'static/')

app.window.setWindowIcon(QtGui.QIcon(os.path.join(BASE_DIR, "/static/icon.png")))

app.bind(Engine(app))

app.template = ("index.html", {})

if __name__ == '__main__':
	app.start()