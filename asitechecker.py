import requests
import slack_sdk as slacker
import os
import logging 
import csv

slack_token = os.environ.get('SLACK_TOKEN')
client = slacker.WebClient(token=slack_token)

#try: 
#    response = client.chat_postMessage(
#        channel="C0226ELG6R4",
#        text="health notifier test"
 #   )
#except slacker.errors.SlackApiError as e: 
#    assert e.response["error"]

website_url = "https://eightknot.chaoss.tv"

#website_url = "http://192.168.0.95:5038"

r = requests.get(f'{website_url}', verify=False, timeout=5)

if r.status_code != 200:
    if os.path.isfile('./fail.txt'): 
        #do nothing
        print('hi')
    else:  
        try: 
            response = client.chat_postMessage(
                channel="C0226ELG6R4",
                text=(f"Please verify that {website_url} is working. It appears to be down right now.")
            ) 
        except slacker.errors.SlackApiError as e: 
            assert e.response["error"]   
        with open('./fail.txt', a, newline='') as file: 
            writer = csv.writer(file)
            writer.writerow(['failed'])
        file.close() 
    
else:
    if os.path.isfile('./fail.txt'): 
        os.remove('./fail.txt')
       
    print(f"Good News, {website_url} is up")