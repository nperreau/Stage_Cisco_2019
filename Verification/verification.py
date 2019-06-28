import sys
import time
import json
import requests
import colorama
from termcolor import colored


colorama.init()


TIMEOUT = 120 # Seconds
while True:
    json_file = input("Enter a JSON file that contain all the URL to verify or type .[url] to check only one Web page ")

    if json_file == "exit":
        sys.exit(0)
    if json_file == "help":
        print(colored("Web Checker help", 'cyan', attrs=['blink']))
        print("What do you need help with?")
        cmd = input("Json or the commands? (j/c)")
        if cmd == "j":
            print('You simply need to create a json list named "url" that contain all the URLs that you want to check \nYou also can set the Timeout (Take a look at the "example.json" file to see how it works ! ')
        if cmd == "c":
            print("Enter a json file, we recomend that this file is in the same folder than Web checker")
            print("Type . + an URL to check only one URL (exemple : .https://google.com)")
            print('The "help" command display some help about Web Check')
        sys.exit(0)
        

    def print_url_code(url):
        """
        Return True if url is resolved, False otherwise.
        """
        t0 = time.time()
        while True:
            try:
                r = requests.get(url)
                break
            except:
                if time.time() - t0 < TIMEOUT: 
                    print(colored(url + " Retrying...", 'red', attrs=['blink']))
                    time.sleep(5)
                else:
                    print("Page unreachable, timeout exceeded.")
                    return False    
                

        if r.status_code == 200:
            print(colored(url + " Nothing to report", 'green', attrs=['blink']))
            return True
        elif r.status_code == 404:
            print(colored(url + " This page doesnt exist !", 'red', attrs=['blink']))
        elif r.status_code == 301:
            print(colored(url + " Permanent redirection", 'green', attrs=['blink']))
        elif r.status_code == 302:
            print(colored(url + " Temporary redirection", 'green', attrs=['blink']))
        elif r.status_code == 403:
            print(colored(url + " Access denied", 'red', attrs=['blink']))
        elif r.status_code == 504:
            print(colored(url + " The server did not respond", 'red', attrs=['blink']))
            return False

        


    if json_file.find('.') == 0:
        url = json_file.split(".", 1)
        print_url_code(url[1])
    else :
        result = {}
        url_nbr = 0
        json_url = json.load(open(json_file, "r"))
        url_list = json_url['url']
        TIMEOUT = json_url['timeout']
        for url in url_list:
            result[url] = print_url_code(url)

        print(result)