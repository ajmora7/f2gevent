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
  print('hello world!')
  graph = facebook.GraphAPI(access_token=my_access_token, version="2.1")

  post = graph.get_object(id=my_user_id, fields='friends')
  total_friends = post['friends']['summary']['total_count']
  print('I have {} friends on Facebook!'.format(total_friends))



if __name__ == '__main__':
  main()
