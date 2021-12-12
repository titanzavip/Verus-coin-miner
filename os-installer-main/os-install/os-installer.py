# Project start date 08/10/2021
# Created by.Phumin-Dev,mantvmass,mobile-mining (I'm the sameperson in all these names)
# Can be further developed without limitations.
# Donate: KasikornThai  : 0608905863
#         Litecoin(LTC) : LTT2X57ervCMpfNva5uo1JBzT2UJVBiEZu
#         Dogecoin(Doge): DFwUqKS3j3RMMkqQF8z6kbYZ652M8VCFVs
#Thank you

import os, sys, time, json
from process import *

def banner():
    os.system("clear")
    banner = f""" \033[93mos-installer version\033[00m: {version}
┌─┐┌─┐   ┬┌┐┌┌─┐┌┬┐┌─┐┬  ┬  ┌─┐┬─┐
│ │└─┐───││││└─┐ │ ├─┤│  │  ├┤ ├┬┘
└─┘└─┘   ┴┘└┘└─┘ ┴ ┴ ┴┴─┘┴─┘└─┘┴└─"""

    print(banner,f"\nCreated by.mobile-mining\n")
    print("---------------------------------------------------")
    print("\033[96mสนับสนุนนักพัมนา\033[00m\n"
        + f" กสิกรไทย: {kasikorn}\n"
        + f"     LTC:  {litecoin}\n"
        + f"    DOGE:  {dogecoin}")
    print("---------------------------------------------------\n")

def main():
    banner()
    print("[ MENU ] \n"
        + "[1] Ubuntu Linux(clone)     " + f"{alert_ubuntuc}\n"
        + "[2] Ubuntu Linux(hirste)    " + f"{alert_ubuntu}\n"
        + "[3] Alpine Linux(edge)      " + f"{alert_alpine}\n"
        + "[4] Archlinux Linux         " + f"{alert_archlinux}\n"
        + "[5] Debian Linux(bullseye)  " + f"{alert_debian}\n"
        + "[6] Fedora(34)              " + f"{alert_fedora}\n"
        + "[7] Gentoo                  " + f"{alert_gentoo}\n"
        + "[8] OpenSUSE(Tumbleweed)    " + f"{alert_opensuse}\n"
        + "[9] Void Linux              " + f"{alert_void}\n"
        + "[0] ออก")
    option = 0
    try:
        option = int(input("เลือกเมนู >> "))
        if option > 9:
            raise Exception()
    except:
        time.sleep(2)
        print("\nเกิดข้อผิดพลาด!!")
        main()
    os_list = ["exit","ubuntuc","ubuntu","alpine","archlinux","debian","fedora","gentoo","opensuse","void"]
    select_list = os_list[option]
    if select_list == "exit":
        banner()
        print("\nออก")
        time.sleep(2)
        sys.exit()
    elif select_list == "ubuntuc":
        banner()
        if os.path.isfile("status/ubuntuc.json") == False:
            ubuntuc()
        elif os.path.isfile("status/ubuntuc.json") == True:
            os.system("sh ubun.sh")
        else:
            print("\nเกิดข้อผิดพลาด!!")
            time.sleep(2)
    elif option >= 2 and option <= 9:
        banner()
        if os.path.isfile(f"status/{select_list}.json") == False:
            installer(select_list)
        elif os.path.isfile(f"status/{select_list}.json") == True:
            with open(f"status/{select_list}.json") as loads:
                load = loads.read()
                fig = json.loads(load)
                status = fig["status"]
                if status == "on":
                    os.system(f"proot-distro login {select_list}")
                else:
                    print("เริ่มการติดตั้งใหม่...")
                    time.sleep(2)
                    installer(select_list)
        else:
            print("\nเกิดข้อผิดพลาด!!")
            time.sleep(2)
    else:
        print("\nเกิดข้อผิดพลาด!!")
        time.sleep(2)

while True:

    # check status
    if os.path.isdir("status") == False:
        os.system("mkdir status")

    # check install ubuntu(clone)
    if os.path.isfile("status/ubuntuc.json") == False:
        alert_ubuntuc = "\033[91mยังไม่ติดตั้ง\033[00m"
    else:
        with open('status/ubuntuc.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            status_ubuntuc = fig['status']
        if status_ubuntuc == "on":
            alert_ubuntuc = "\033[92mติดตั้งแล้ว\033[00m"
        elif status_ubuntuc == "off":
            alert_ubuntuc = "\033[91mยังไม่ติดตั้ง\033[00m"
        else:
            alert_ubuntuc = "\033[91mเกิดข้อผิดพลาด!\033[00m"

    # check install ubuntu
    if os.path.isfile("status/ubuntu.json") == False:
        alert_ubuntu = "\033[91mยังไม่ติดตั้ง\033[00m"
    else:
        with open('status/ubuntu.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            status_ubuntu = fig['status']
        if status_ubuntu == "on":
            alert_ubuntu = "\033[92mติดตั้งแล้ว\033[00m"
        elif status_ubuntu == "off":
            alert_ubuntu = "\033[91mยังไม่ติดตั้ง\033[00m"
        else:
            alert_ubuntu = "\033[91mเกิดข้อผิดพลาด!\033[00m"

    # check install alpine
    if os.path.isfile("status/alpine.json") == False:
        alert_alpine = "\033[91mยังไม่ติดตั้ง\033[00m"
    else:
        with open('status/alpine.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            status_alpine = fig['status']
        if status_alpine == "on":
            alert_alpine = "\033[92mติดตั้งแล้ว\033[00m"
        elif status_alpine == "off":
            alert_alpine = "\033[91mยังไม่ติดตั้ง\033[00m"
        else:
            alert_alpine = "\033[91mเกิดข้อผิดพลาด!\033[00m"

    # check install archlinux
    if os.path.isfile("status/archlinux.json") == False:
        alert_archlinux = "\033[91mยังไม่ติดตั้ง\033[00m"
    else:
        with open('status/archlinux.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            status_archlinux = fig['status']
        if status_archlinux == "on":
            alert_archlinux = "\033[92mติดตั้งแล้ว\033[00m"
        elif status_archlinux == "off":
            alert_archlinux = "\033[91mยังไม่ติดตั้ง\033[00m"
        else:
            alert_archlinux = "\033[91mเกิดข้อผิดพลาด!\033[00m"

    # check install debian
    if os.path.isfile("status/debian.json") == False:
        alert_debian = "\033[91mยังไม่ติดตั้ง\033[00m"
    else:
        with open('status/debian.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            status_debian = fig['status']
        if status_debian == "on":
            alert_debian = "\033[92mติดตั้งแล้ว\033[00m"
        elif status_debian == "off":
            alert_debian = "\033[91mยังไม่ติดตั้ง\033[00m"
        else:
            alert_debian = "\033[91mเกิดข้อผิดพลาด!\033[00m"

    # check install fedora
    if os.path.isfile("status/fedora.json") == False:
        alert_fedora = "\033[91mยังไม่ติดตั้ง\033[00m"
    else:
        with open('status/fedora.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            status_fedora = fig['status']
        if status_fedora == "on":
            alert_fedora = "\033[92mติดตั้งแล้ว\033[00m"
        elif status_fedora == "off":
            alert_fedora = "\033[91mยังไม่ติดตั้ง\033[00m"
        else:
            alert_fedora = "\033[91mเกิดข้อผิดพลาด!\033[00m"

    # check install gentoo
    if os.path.isfile("status/gentoo.json") == False:
        alert_gentoo = "\033[91mยังไม่ติดตั้ง\033[00m"
    else:
        with open('status/gentoo.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            status_gentoo = fig['status']
        if status_gentoo == "on":
            alert_gentoo = "\033[92mติดตั้งแล้ว\033[00m"
        elif status_gentoo == "off":
            alert_gentoo = "\033[91mยังไม่ติดตั้ง\033[00m"
        else:
            alert_gentoo = "\033[91mเกิดข้อผิดพลาด!\033[00m"

    # check install opensuse
    if os.path.isfile("status/opensuse.json") == False:
        alert_opensuse = "\033[91mยังไม่ติดตั้ง\033[00m"
    else:
        with open('status/opensuse.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            status_opensuse = fig['status']
        if status_opensuse == "on":
            alert_opensuse = "\033[92mติดตั้งแล้ว\033[00m"
        elif status_opensuse == "off":
            alert_opensuse = "\033[91mยังไม่ติดตั้ง\033[00m"
        else:
            alert_opensuse = "\033[91mเกิดข้อผิดพลาด!\033[00m"

    # check install void
    if os.path.isfile("status/void.json") == False:
        alert_void = "\033[91mยังไม่ติดตั้ง\033[00m"
    else:
        with open('status/void.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            status_void = fig['status']
        if status_void == "on":
            alert_void = "\033[92mติดตั้งแล้ว\033[00m"
        elif status_void == "off":
            alert_void = "\033[91mยังไม่ติดตั้ง\033[00m"
        else:
            alert_void = "\033[91mเกิดข้อผิดพลาด!\033[00m"



    if os.path.exists("../../../home/storage") == False:
        os.system("sh storage.sh")

    if os.path.isfile("config.json") == False:
        puts = {
            'Version': "0.0.2 beta",
            'Kasikorn': "0608905863",
            'Litecoin': "LTT2X57ervCMpfNva5uo1JBzT2UJVBiEZu",
            'Dogecoin': "DFwUqKS3j3RMMkqQF8z6kbYZ652M8VCFVs"
        }
        with open('config.json', 'w') as file:
            json.dump(puts, file, indent=4)
            with open('config.json', encoding='utf-8') as loads:
                load = loads.read()
                fig = json.loads(load)
                version = fig['Version']
                kasikorn = fig['Kasikorn']
                litecoin = fig['Litecoin']
                dogecoin = fig['Dogecoin']
                main()
    else:
        with open('config.json', encoding='utf-8') as loads:
            load = loads.read()
            fig = json.loads(load)
            version = fig['Version']
            kasikorn = fig['Kasikorn']
            litecoin = fig['Litecoin']
            dogecoin = fig['Dogecoin']
            main()

