
import amino

import os

import time

Yellow = '\033[1;33m'
green = '\033[4;32m'
red = '\033[0;31m'
blue = '\033[4;34m'
white = '\033[0;37m'
os.system("clear")
print("                                                  .--                              ")
print("                                                /MMMy      -mNh                      ")
print("                                                 sMMs      `/+:                        ")
print("                                  -+oo+.        oMMs     `/oso/`                         ")
print("                            -/:    omoyMMy       oMMs   `yMy-+mMM+                        ")
print("                           -MMN`       yMMy      oMMs   oMMs  `MMM.                       ")
print("                            dMM+        hMMs     oMMs   .dMMhssNMM.                       ")
print("                            +MMm:........hMMd:.  sMMm:....-/+/:MMd                        ")
print("                            :MMddmmmmmmmmmmmmms  ydohdmmmmmmmmdho`                        ")
print("                            oMh      :+/         .                                        ")
print("                       .dmNMh/      `dNd.                                                 ")
print("                         ..                                                               ")







print ("" +Yellow)
print("                         /shh-                                `.` -:-                ")
print("                         :NMM.                                dmm-dNd`               ")
print("                          mMM.                                -:-.--`                ")
print("                     `    mMM.             ```         ``     -sysdmh+               ")
print("                  `shdo   mMM.    .--  `:ohdmdy:`     ydm.   /NM/ .yMMo              ")
print("                `.`+MMN   mMM.   -NNd.ohy+-.:yMMh`    sMMo   +MMh:-/MMd              ")
print("               /mmo dMM-  mMM:   :MMNy/.      +MMh    -MMm`   :syyssMMy              ")
print("            .y `::. oMM:  NmmmhhhmMMNhhhhhhhhhhNmy`    NMMdhhhhhhhhdNh.             ")
print("            -M+`    sMd`  o..-------------------`      NM+----------.             ")
print("             sNdsoosmy.                           /ooshd/                       ")
print("              ./ooo/.                             -oo+:`                      ")

time.sleep(3)


print ("\n\n\n\n\n")

mail=input ("Your Mail : ")
pas=input ("Your Password : ")
os.system("clear")

client = amino.Client()
inf=input("Com Url : ")
infoo=client.get_from_code(inf)

cid=infoo.path[1:infoo.path.index("/")]

print ("\n")
print (" [1] Online")
print ("\n")
print (" [2] Ofline")
print ("\n")
i=input("Type Number : ")

if i == '1' :


    client = amino.Client()
    client.login(email=mail, password=pas)
    subclient = amino.SubClient(comId=cid, profile=client.profile)
    subclient.activity_status('1')     

if i == '2' :


    client = amino.Client()
    client.login(email=mail, password=pas)
    subclient = amino.SubClient(comId=cid, profile=client.profile)
    subclient.activity_status('2')






