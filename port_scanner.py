import os
import sys
import socket
from datetime import datetime
import pyfiglet

while True:
    def port_tarama():
        if os.name == "nt":
            os.system("cls")
        else:
            print(clear)
        ascii_banner = pyfiglet.figlet_format("PORT SCANNER\nby TheFierroS")
        print(ascii_banner)

        target = input("Taramak İstediğiniz Site Adresini Giriniz -> ")
        port = int(input("Port Giriniz -> "))
        targetIP = socket.gethostbyname(target)
        print("-" * 60)
        print("Lütfen Bekleyin, Hedef Taranıyor -> ", targetIP)
        print("-" * 60)

        t1 = datetime.now()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((targetIP, port))
        if result == 0:
            print(f"Port {port} -> Açık")
            print("-" * 60)
            t2 = datetime.now()
            total = t2 - t1
            print("Tarama {} İçinde Tamamlandı".format(total))
            print("-" * 60)
            sock.close()
            another = input("Başka Bir Site Taramak İstermisiniz E/H : ")
            if another == "E" or another == "e":
                port_tarama()
            elif another == "H" or another == "h":
                input("Çıkış Yapmak İÇİn Bir Tuşa Basın")
                sys.exit()
            else:
                print("Hatalı Tuşlama...")
                sys.exit()
        else:
            print(f"{port} Portu Kapalı")
            print("-" * 60)
            t2 = datetime.now()
            total = t2 - t1
            print("Tarama {} İçinde Tamamlandı".format(total))
            print("-" * 60)
            another = input("Başka Bir Site Taramak İstermisiniz E/H : ")
            if another == "E" or another == "e":
                port_tarama()
            elif another == "H" or another == "h":
                input("Çıkış Yapmak İÇİn Bir Tuşa Basın")
                sys.exit()
            else:
                print("Hatalı Tuşlama...")
                sys.exit()
    port_tarama()
