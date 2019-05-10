#!/usr/bin/env python3

from slackclient import SlackClient 
import os

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#random",
  text="Hello from Python Slack Client! :tada:"
)


