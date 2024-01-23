from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from http import HTTPStatus
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

import slack_sdk as slacker
import os
import logging 
import csv

slack_token = os.environ.get('SLACK_TOKEN')
client = slacker.WebClient(token=slack_token)


# get the status of a website
def get_website_status(url):
    # handle connection errors
    try:
        # open a connection to the server with a timeout
        with urlopen(url, timeout=10) as connection:
            # get the response code, e.g. 200
            code = connection.getcode()
            return code
    except HTTPError as e:
        return e.code
    except URLError as e:
        return e.reason
    except:
        return e
 
# interpret an HTTP response code into a status
def get_status(code):
    if code == HTTPStatus.OK:
        return 'OK'
    else:
        return 'ERROR'
 
# check status of a list of websites
def check_status_urls(urls):
    # create the thread pool
    with ThreadPoolExecutor(len(urls)) as executor:
        # check the status of each url
        results = executor.map(get_website_status, urls)
        # enumerate the results in the same order as the list of urls
        for i,code in enumerate(results):
            # get the url
            url = urls[i]
            #website_url = urls[i].lstrip("https://")
            website_url = urls[i] 
            website_url = website_url[8:]
            # interpret the status
            status = get_status(code)
            # report status
            sitefile = website_url+'.txt'
            if status != 'OK': 
                #sitefile = website_url+'.txt'
                if os.path.isfile(sitefile): 
                    #do nothing
                    print('hi')
                else:  
                    try: 
                        response = client.chat_postMessage(
                            channel="C0226ELG6R4",
                            text=(f"Please verify that {urls[i]} is working. It appears to be down right now.")
                        ) 
                    except slacker.errors.SlackApiError as e: 
                        assert e.response["error"]   
                    with open(sitefile, 'a', newline='') as file: 
                        writer = csv.writer(file)
                        writer.writerow(['failed'])
                    file.close() 
            else: 
                if os.path.isfile(sitefile): 
                    os.remove(sitefile)
            
                #print(f"Good News, {website_url} is up")

            print(f'{url:20s}\t{status:5s}\t{code}')
 
# list of urls to check
URLS = ['https://chaoss.community',
        'https://eightknot.chaoss.tv',
        'https://ai.chaoss.io']
# check all urls
check_status_urls(URLS)