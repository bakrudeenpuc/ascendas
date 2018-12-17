from flask import Flask
import json
from flask import request
import time
import re
import os
import sys
import logging
import redis
import urllib.request, urllib.parse, urllib.error
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello',methods=['GET'])
def hello_world_get():
	try:		 
		return "Hello Worssld!"
	except Exception as e :		 
		print ("Exception in user button handler",e)

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=2500)
