"""
                                                                
Authors: Beebkips

"""
import os
import time
import json
import requests
import time
from slackclient import SlackClient

slack_client = SlackClient('xoxb-351889272070-zXiJx3HmraK9kwpFB4i2DQbA')

def handle_command(command, channel, user):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    oc = command
    response = "Something happened" 
    
    # "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
    #            "* command with numbers, delimited by spaces."
    
    # example command
    if command.startswith('!HotSpot'):
        content = command.split(' ')
        response = "I have scheduled a meeting for " +  content[2] + " with " + content[4]

        pack = {"Method" : "Slack", "Organizer" : user, "Time" : int(content[2]), "RequestTime" : int(time.time()), "Members" : [content[4]]}
        requests.post('https://iothackhotspots.herokuapp.com/schedule', json=pack)

    response = "`"  + response + "`"
    
    # return the response
    print('USER: ' + user, '\nCHANNEL: ' + channel, '\nMESSAGE: ' + oc)
    print('=====')
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    # if(len(output_list) > 0):
    #     print output_list

    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and output['text'].startswith('!'):
                return output['text'], \
                       output['channel'], \
                       output['user']
            
    return None, None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("HusciiBot connected and running!")
        while True:
            command, channel, user = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel, user)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")