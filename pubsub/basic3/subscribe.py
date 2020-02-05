#! /usr/bin/env python 

import sys
import time
import datetime
from time import sleep

from google.cloud import firestore
import google.cloud.exceptions
from google.cloud import pubsub_v1

#def fire(data):
# db = firestore.Client().from_service_account_json('service-account.json')
# print(db)
 
 # [START add_from_dict]
# data = {u'name': u'Los Angeles',u'state': u'CA',u'country': u'USA'}
 
 # Add a new doc in collection 'cities' with ID 'LA'
# db.collection(u'users').document(u'data1').set(data)
 # [END add_from_dict]


def sub(project_id, subscription_name):

 """Receives messages from a Pub/Sub subscription."""

 client = pubsub_v1.SubscriberClient()
 subscription_path = client.subscription_path(project_id, subscription_name)

 def callback(message):
  #print('Received message {} of message_id {}'.format(message, message.message_id))
  print(message)

  print("\n Calling Firestore Now \n")      
  
#  fire(message)

  # Unacked messages will be redelivered.
  message.ack()
 
 client.subscribe(subscription_path, callback=callback)
   
 print('Listening for messages on {}'.format(subscription_path))

 while True:
 # The subscriber is non-blocking. We must keep the main thread from
 # exiting so it can process messages asynchronously in the background.
  time.sleep(60)


if __name__ == '__main__':

    _, p, s = sys.argv
    sub(p,s)
