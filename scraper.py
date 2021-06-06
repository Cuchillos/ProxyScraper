#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from requests.structures import CaseInsensitiveDict
import time
import os

print()
print("░█████╗░██╗░░░██╗░█████╗░██╗░░██╗██╗██╗░░░░░██╗░░░░░░█████╗░")
print("██╔══██╗██║░░░██║██╔══██╗██║░░██║██║██║░░░░░██║░░░░░██╔══██╗")
print("██║░░╚═╝██║░░░██║██║░░╚═╝███████║██║██║░░░░░██║░░░░░██║░░██║")
print("██║░░██╗██║░░░██║██║░░██╗██╔══██║██║██║░░░░░██║░░░░░██║░░██║")
print("╚█████╔╝╚██████╔╝╚█████╔╝██║░░██║██║███████╗███████╗╚█████╔╝")
print("░╚════╝░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝░╚════╝░")
print()
print("               By: cuchillo#7116 (Discord)")
print()

print('Tipos de proxy: ')
time.sleep(0.6)
print()
print('    [1] HTTP/S')
print('    [2] SOCKS4')
print('    [3] SOCKS5')
print()
time.sleep(1)
ProxyType = int(input('Escoje un tipo de proxy: '))

if ProxyType == 1:

    url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http"

    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["Cache-Control"] = "max-age=0"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.279"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["Sec-Fetch-Site"] = "none"
    headers["Sec-Fetch-Mode"] = "navigate"
    headers["Sec-Fetch-User"] = "?1"
    headers["Sec-Fetch-Dest"] = "document"
    headers["Accept-Language"] = "es-ES,es;q=0.9"

    http = requests.get(url, headers=headers)

    print()
    print()
    print("  Scraping proxies http/s ...")
    time.sleep(3)
    print()
    print(http.text)
    time.sleep(1.5)
    print()
    print()
    httpstxt = open('Http-s proxies.txt', "a+")
    for lines in http.text:
        httpstxt.write(lines.rstrip('\n'))
    httpstxt.close()

    proxies = 0
    txt = open('Http-s proxies.txt', "r")
    txt = txt.readlines()
    for x in txt:
        proxies += 1

    print(f"PROXIES OBTENIDAS: {proxies}")
    print()
    print("SE HA CREADO UN ARCHIVO .TXT CON LOS PROXIES HTTP/S")
    time.sleep(7)

elif ProxyType == 2:
    url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4"

    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["Cache-Control"] = "max-age=0"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.279"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["Sec-Fetch-Site"] = "none"
    headers["Sec-Fetch-Mode"] = "navigate"
    headers["Sec-Fetch-User"] = "?1"
    headers["Sec-Fetch-Dest"] = "document"
    headers["Accept-Language"] = "es-ES,es;q=0.9"

    socks4 = requests.get(url, headers=headers)

    print()
    print()
    print("  Scraping proxies socks4 ...")
    time.sleep(3)
    print()
    print(socks4.text)
    time.sleep(1.5)
    print()
    socks4txt = open('Socks4 proxies.txt', "a+")
    for lines in socks4.text:
        socks4txt.write(lines.rstrip('\n'))
    socks4txt.close()

    proxies = 0
    txt = open('Socks4 proxies.txt', "r")
    txt = txt.readlines()
    for x in txt:
        proxies += 1

    print(f"PROXIES OBTENIDAS: {proxies}")
    print()
    print("SE HA CREADO UN ARCHIVO .TXT CON LOS PROXIES SOCKS4")
    time.sleep(7)

elif ProxyType == 3:
    url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5"

    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["Cache-Control"] = "max-age=0"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.279"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["Sec-Fetch-Site"] = "none"
    headers["Sec-Fetch-Mode"] = "navigate"
    headers["Sec-Fetch-User"] = "?1"
    headers["Sec-Fetch-Dest"] = "document"
    headers["Accept-Language"] = "es-ES,es;q=0.9"

    socks5 = requests.get(url, headers=headers)

    print()
    print()
    print("  Scraping proxies socks5 ...")
    time.sleep(3)
    print()
    print(socks5.text)
    time.sleep(1.5)
    print()
    socks5txt = open('Socks5 proxies.txt', "a+")
    for lines in socks5.text:
        socks5txt.write(lines.rstrip('\n'))
    socks5txt.close()

    proxies = 0
    txt = open('Socks5 proxies.txt', "r")
    txt = txt.readlines()
    for x in txt:
        proxies += 1

    print(f"PROXIES OBTENIDAS: {proxies}")
    print()
    print("SE HA CREADO UN ARCHIVO .TXT CON LOS PROXIES SOCKS5")
    time.sleep(7)

else:
    print()
    time.sleep(0.6)
    print("PON UN NÚMERO DEL 1 AL 3 :V")
    time.sleep(5)
