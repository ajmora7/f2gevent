#!/usr/bin/python

import sys
import facebook
import requests
import configparser
import os

full_path = os.path.dirname(os.path.realpath(__file__))
current_path, current_directory = os.path.split(full_path)

config = configparser.RawConfigParser()
config.read(os.path.join(full_path, 'events.cfg'))

my_access_token = config.get('user_info', 'my_access_token')
my_user_id = config.get('user_info', 'my_user_id')

def main():
  graph = facebook.GraphAPI(access_token=my_access_token, version="2.1")

  friends = graph.get_object(id=my_user_id, fields='friends')
  total_friends = friends['friends']['summary']['total_count']
  print('I have {} friends on Facebook!'.format(total_friends))

  events = graph.get_object(id=my_user_id, fields='events')
  print('I have {} events on my calendar right now!'.format(len(events['events']['data'])))
  print('They are:\n')
  for event in events['events']['data']:
    print('{}, {}'.format(event['name'], event['start_time']))
    print('{}\n'.format(event['rsvp_status']))

if __name__ == '__main__':
  main()
