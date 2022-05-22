#!/usr/bin/python
from pathlib import Path
from colorama import Fore, init
import hashlib
import datetime
import argparse
init(autoreset=False)
LINE_CLEAR = '\x1b[2K'  # <-- ANSI sequence


def banner(hash, hash_type, wordlist):
    print("""
    █▀█ █▄█ ▀█▀ █░█ █▀█ █▄░█   █▀▀ █▀█ █▀█   █░█ █░█ █▀▀ █▄▀ █▀█ █▀
    █▀▀ ░█░ ░█░ █▀█ █▄█ █░▀█   █▀░ █▄█ █▀▄   █▀█ ▀▀█ █▄▄ █░█ █▀▄ ▄█

                                            𝖌𝖎𝖙𝖍𝖚𝖇 𝖆𝖑𝖎𝖎76𝖙𝖙
    """)
    print("-"*67)
    print(f"""
                    Ｈａｓｈ Ｃｒａｃｋｅｒ\n
        START_TIME: {datetime.datetime.ctime(datetime.datetime.now())}
        Hash: {hash}
        Hash Type: {hash_type.__name__}     
        WORDLIST_FILES: {wordlist.name}
        """)
    print("-"*67)


def hashCracker(hash, hash_type, wordlist=None):
    # Supported Formats: 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'
    match hash_type:
        case "md5":
            hash_type = hashlib.md5
        case "sha1":
            hash_type = hashlib.sha1
        case "sha224":
            hash_type = hashlib.sha224
        case "sha256":
            hash_type = hashlib.sha256
        case "sha384":
            hash_type = hashlib.sha384
        case "sha512":
            hash_type = hashlib.sha512
        case default:
            print(Fore.RED + "[~] Error: Please enter correct hash type.")

    if wordlist:
        wordlist = open(wordlist, "r", encoding="utf-8")
    else:
        wordlist = open("wordlist.txt", "r", encoding="utf-8")

    banner(hash, hash_type, wordlist)

    if hash_type:
        for password in wordlist:
            password = str(password.strip("\n"))

            print(Fore.WHITE + f"--> Testing: {password}", end="\r")
            print(end=LINE_CLEAR)

            line_hash = hash_type(password.encode()).hexdigest()
            if str(line_hash) == str(hash.lower()):
                print(Fore.GREEN +
                    f"[+] Hash Found: ", password)


ap = argparse.ArgumentParser(add_help=False)
ap.add_argument('-i', '--info', action='help', default=argparse.SUPPRESS,
                help="""[*] python main.py -h <hash> -t <type> -w <wordlist>""")
ap.add_argument('-h', '--hash', dest='hash',
                help="Enter hash.")
ap.add_argument('-t', '--type', dest='hash_type',
                help="Enter hash type.")
ap.add_argument('-w', '--wordlist', type=Path, dest='wordlist',
                help="Enter your wordlist.")

args = vars(ap.parse_args())
if args['hash'] and args['hash_type']:
    try:
        hashCracker(args['hash'], args['hash_type'], args["wordlist"])
        print(
            f"END_TIME: {datetime.datetime.ctime(datetime.datetime.now())}")
    except FileNotFoundError:
        print(Fore.RED +
              f"[~] Error: -FileNotFoundError- Please check your wordlist path. Wordlist: {args['wordlist']}")
    except KeyboardInterrupt:
        print(Fore.LIGHTCYAN_EX + "\n[~] End: You have pressed ctrl-c button.")
else:
    print(Fore.LIGHTRED_EX +
          """[*] Hash (-h): Must be specified.\n[*] Hash Type (-t): Must be specified\n-----------\nUsage: python main.py -h <hash> -t <type> -w <wordlist>""")
