import platform
import subprocess
from random import randint
import requests
import socket
from contextlib import closing
from colorama import Style, Fore
from concurrent.futures import ThreadPoolExecutor


def clear():
    if platform.system() == "Windows":
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)


groen = Fore.GREEN
geel = Fore.YELLOW
rood = Fore.RED
blauw = Fore.BLUE
reset = Style.RESET_ALL

class IpsGenerator:
    def __init__(self):
        self.
    def gen(self):
        iplist = []
        ruimte = range(0, how_many)
        count = 0
        for r in ruimte:
            count += 1
            a = randint(0, 256)
            b = randint(0, 256)
            c = randint(0, 256)
            d = randint(0, 256)
            ip = ('{}.{}.{}.{}'.format(a, b, c, d))
            iplist.append(ip)
        return iplist


cijfer = randint(1, 10000)


def ips(ip):
    if "443" in port:
        checken = "https://"
    else:
        checken = "http://"
    try:
        ip = ip.strip().replace("\n", "").replace("\r", "")
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(5)
            if sock.connect_ex((ip, int(port))) == 0:
                url = f"{checken}{ip}:{port}"
                print(url)
                zoeken = requests.get(url, timeout=5, allow_redirects=False)
                code = zoeken.status_code
                if code == 200:
                    schrijven = open(f"GOOOD_GENERATED_IPS_{cijfer}.txt", "a")
                    schrijven.write(url + "\n")
                    schrijven.close()
                    print(f"{geel}{url}{reset} {groen}GOOD_IP{reset}{geel}+{reset}{groen}WEB_UP{reset}!")
                    return True
                else:
                    schrijven1 = open(f"CAN_BE_SHITTY_{cijfer}.txt", "a")
                    schrijven1.write(url + "\n")
                    schrijven1.close()
                    print(f"{geel}{url}{reset} {groen}GOOD_IP{reset}{geel}+{reset}{groen}WEB_MAYBE_UP{reset}"
                          f" {geel}STATUS{reset}{groen}: {rood}{code}")
                    return True
            else:
                print(f"{geel}{ip}{reset} {rood}BAD_IP{reset}{geel}&{reset}{rood}BAD_PORT{reset}!")
                return False
    except Exception as e:
        print(f"{geel}{ip}{reset} {rood}BAD_IP{reset}{geel}&{reset}{rood}BAD_PORT{reset}!")
        return False


if __name__ == '__main__':
    clear()
    print(f"{geel}EMPERORSTOOLSSHOP LEGACY{reset}\n{groen}https://t.me/freshesleadsb{reset}\n{geel}"
          f"@Freshesleadsever{reset}\n{blauw}AUTO GENERATE{geel} & {reset}{blauw}PORT{groen}+{reset}{blauw}"
          f"WEB_STATUS SCANNER{reset}"
          f" {geel}V1{reset}\n")
    try:
        how_many = int(input(f"{geel}How many Ips{groen}?{rood}:{reset} "))
        clear()
        threads = int(input(f"{geel}How Many Threads{groen}?{rood}:{reset} "))
        clear()
        try:
            timeout = input(f"{blauw}SET YOUR OWN TIMEOUT FOR PORT EN WEB{reset}\n{geel}How many seconds timeout"
                            f"{reset}{groen}?{reset}{rood}:{reset} ")
        except:
            timeout = 5
        port = input(f"{geel}What{reset} {groen}Port Are We Looking For{reset}{geel}?{reset}{rood}:{reset} ")
        start = ThreadPoolExecutor(max_workers=threads)
        start.map(ips, gen())
    except:
        exit(f"{rood}You{reset} {geel}STUPID{reset}?")
