#! /usr/bin/env python 

import sys

from google.cloud import pubsub_v1


def get_callback(api_future, data):
    """Wraps message data in the context of the callback."""
    def callback(api_future):
       if api_future.exception():
            print("There was a problem with message {}".format(data))
       else:
            print("Published message {} now has message_id {}".format(
                data, api_future.result()))
    return callback

def pub(project_id, topic_name):
    """Publishes multiple messages to a Pub/Sub topic."""
    client = pubsub_v1.PublisherClient()
    topic_path = client.topic_path(project_id, topic_name)    # Data must be a bytestring

    data = "Hello, World!"
    data = data.encode('utf-8')

    # When you publish a message, the client returns a future.
    api_future = client.publish(topic_path, data=data)
    api_future.add_done_callback(get_callback(api_future, data))


if __name__ == '__main__':
    _, p, t = sys.argv
    pub(p, t)

