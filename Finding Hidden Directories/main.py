#!/usr/bin/python

import datetime
import argparse
from colorama import Fore, init
from pathlib import Path
import requests


init(autoreset=False)
LINE_CLEAR = '\x1b[2K'  # <-- ANSI sequence


def banner(url, wordlist):
    print("""
    █▀█ █▄█ ▀█▀ █░█ █▀█ █▄░█   █▀▀ █▀█ █▀█   █░█ █░█ █▀▀ █▄▀ █▀█ █▀
    █▀▀ ░█░ ░█░ █▀█ █▄█ █░▀█   █▀░ █▄█ █▀▄   █▀█ ▀▀█ █▄▄ █░█ █▀▄ ▄█

                                            𝖌𝖎𝖙𝖍𝖚𝖇 𝖆𝖑𝖎𝖎76𝖙𝖙
    """)
    print("-"*67)
    print(f"""
                    𝙵𝚒𝚗𝚍𝚒𝚗𝚐 𝙷𝚒𝚍𝚍𝚎𝚗 𝙳𝚒𝚛𝚎𝚌𝚝𝚘𝚛𝚒𝚎𝚜\n
        START_TIME: {datetime.datetime.ctime(datetime.datetime.now())}
        URL_BASE: {url}
        WORDLIST_FILES: {wordlist.name}
    """)
    print("-"*67)
    print(f"--> Scanning URL: {url} <--")


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


def findHiddenUrl(url, wordlist):
    if wordlist:
        wordlist = open(wordlist, "r")
    else:
        wordlist = open("common.txt", "r")
    banner(url, wordlist)
    global found
    found = 0
    for line in wordlist:
        word = line.strip("\n")
        full_url = url + "/" + word

        print(Fore.WHITE + f"--> Testing: {full_url}", end="\r")
        print(end=LINE_CLEAR)

        response = request(full_url)

        if response:
            found += 1
            print(Fore.GREEN + " " * 10 + "[+] Found: http://" + full_url +
                  f" (CODE:{response.status_code}|SIZE:{len(response.content)})")


ap = argparse.ArgumentParser(add_help=False)
ap.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                help="""WordList (-w): Enter your wordlist (use `-w -` for stdin)\n[*] Url/Domain (-u): Must be specified\npython main.py -u test.com -w <wordlist>""")
ap.add_argument('-u', '--url', dest='url',
                help="Enter target url.")
ap.add_argument('-w', '--wordlist', type=Path, dest='wordlist',
                help="Enter your wordlist. Default(common.txt)")

args = vars(ap.parse_args())
if args['url']:
    try:
        findHiddenUrl(args['url'], args['wordlist'])
        print(f"END_TIME: {datetime.datetime.ctime(datetime.datetime.now())}")
        print("FOUND: ", found)
        print(Fore.LIGHTCYAN_EX + "[~] End: The processing has been finished.")
    except FileNotFoundError:
        print(Fore.RED +
              f"[~] Error: -FileNotFoundError- Please check your wordlist path. Wordlist: {args['wordlist']}")
    except KeyboardInterrupt:
        print(Fore.LIGHTCYAN_EX + "\n[~] End: You have pressed ctrl-c button.")
else:
    print(Fore.LIGHTRED_EX + """WordList (-w): Enter your wordlist (use `-w -` for stdin)\n[*] Url/Domain (-u): Must be specified\npython main.py -u test.com -w <wordlist>""")
