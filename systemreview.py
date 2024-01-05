import os
import psutil
import getpass
import wmi
import platform
import shutil
import screeninfo
import socket
import uuid

c = wmi.WMI()
my_system = c.Win32_ComputerSytem()[0]
my_system_plat = platform.uname()

#Get the user hostname
hostname = os.uname()

#Get the username
username = os.getlogin()

#Get the password
password = getpass.getpass()

#Get computer brand
manufacturer = my_system.Manufacturer

#Get the system model
model = my_system.Model

#Get the operating System
my_os = my_system_plat.system

#Get System version
my_version = my_system_plat.version

#get system architecture
archi = my_system.SystemType

#Get the information about the CPU
cpu_model = my_system_plat.processor

#Get the information about the Ram
ram_model = psutil.virtual_memory

#Get the HDD
hdd_total,hdd_used,hdd_free = shutil.disk_usage("/")
hdd_total = hdd_total//(2**30)
hdd_used = hdd_used//(2**30)
hdd_free = hdd_free//(2**30)

#Get Network Card
network_card = psutil.net_if_addrs()


#Get Graphic card info
graphical_card = c.win32_VideoController()[0]

#Get Sound Card info 
Sound_card 

#Get Screen size
screen_size = screeninfo.get_monitors()

#Get the Domain
Nom_Domaine = socket.getfqdn()

#Get Computer Ip Address
ip_adress = spcket.IPAddr

#Get computer MacAddress
Mac_address = hex(uuid.get_node())

file_name = input("Entrez le nom de l'ordinateur en question!")
f = open(file_name+".pdf","x")
#Exporting the data into a pdf file...
f.write("Nom Machine: "+hostname)
f.write( "Nom Utilisateur: "+username)
#Password:...................../
f.write("Brand: Manufacturer")
f.write("Model: "+model)
f.write("Os: "+ my_os + "Model: " + my_version)
f.write("Architecture: "+ archi)
f.write("Cpu:"+cp_model+"Nbr Coeur:........./")
#Graphical Card:......................./
#Sound Card:.........................../
#Screen Size:........................../
#If domain ajoute nom de domaine
#Else write pas de domaine
#Domain Name
#Ip Address:........................../
#Mac Address:........................./
# 

