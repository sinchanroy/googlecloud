#! /usr/bin/env python 

import json
import sys
from datetime import datetime

from google.cloud import pubsub_v1

def get_callback(api_future, data = []):
	"""Wraps message data in the context of the callback."""
	def callback(api_future):
		if api_future.exception():
			print("There was a problem with message {}".format(data))
		else:
			for msg in data:
				print("Published message {} now has message_id {}".format(msg, api_future.result()))
	return callback

def pub(project_id, topic_name):
	
 """Publishes multiple messages to a Pub/Sub topic."""
 client = pubsub_v1.PublisherClient()
 topic_path = client.topic_path(project_id, topic_name)    # Data must be a bytestring
 lst = []
 for i in range(1,100):
  lst = { 'index' : i, 'name' : 'sinchan'+str(i), 'score':  {'maths': 100+i, 'science': 200+i} }   

 # When you publish a message, the client returns a future.
  
  data = json.dumps(lst)
  data = data.encode('utf-8')
  api_future = client.publish(topic_path, data=data)
  api_future.add_done_callback(get_callback(api_future, data))


if __name__ == '__main__':
	_, p, t = sys.argv
	pub(p, t)
