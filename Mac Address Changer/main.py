import random
import string
import os
import re
import argparse


def banner(interface, current_mac, new_mac):
    print("""
    █▀█ █▄█ ▀█▀ █░█ █▀█ █▄░█   █▀▀ █▀█ █▀█   █░█ █░█ █▀▀ █▄▀ █▀█ █▀
    █▀▀ ░█░ ░█░ █▀█ █▄█ █░▀█   █▀░ █▄█ █▀▄   █▀█ ▀▀█ █▄▄ █░█ █▀▄ ▄█

                                            𝖌𝖎𝖙𝖍𝖚𝖇 𝖆𝖑𝖎𝖎76𝖙𝖙
    """)
    print("-"*67)
    print(f"""
        𝕄𝕒𝕔 𝔸𝕕𝕕𝕣𝕖𝕤𝕤 ℂ𝕙𝕒𝕟𝕘𝕖𝕣\n
        Interface: {interface}
        Current Mac Address: {current_mac}
        New Mac Address: {new_mac}
    """.center(50))
    print("-"*67)


def getRandomMac():
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("72468ABC")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")


def ChangeMacAddress(interface, new_mac):
    if not new_mac:
        new_mac = getRandomMac()

    current_mac = getCurrentMac(interface)
    banner(interface, current_mac, new_mac)

    os.popen(f"ifconfig {interface} down")
    os.popen(f"ifconfig {interface} hw ether {new_mac}")
    os.popen(f"ifconfig {interface} up")



def getCurrentMac(interface):
    output = os.popen(f"ifconfig {interface}")
    output = list(output)
    return re.search("ether (.+) ", str(output)).group().split()[1].strip()


ap = argparse.ArgumentParser(add_help=False)
ap.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                help="""python main.py -i <interface> -m <new_mac>""")
ap.add_argument('-i', '--interface', dest='interface',
                help="Enter interface.")
ap.add_argument('-m', '--mac', dest='new_mac',
                help="Enter new mac address. Default(random mac address)")


args = vars(ap.parse_args())
if args['interface']:
    try:
        ChangeMacAddress(args['interface'], args['new_mac'])
        print("[~] End: The processing has been finished. Mac Address Changed!")
    except KeyboardInterrupt:
        print("\n[~] End: You have pressed ctrl-c button.")
else:
    print(ap.print_help())
