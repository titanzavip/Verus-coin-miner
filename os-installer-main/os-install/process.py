import os, time, json

def ubuntuc():
    try:
        os.system("chmod +x ubun.sh")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install git -y")
        os.system("apt-get install wget -y")
        os.system("apt-get install proot -y")
        os.system("git clone https://github.com/MFDGaming/ubuntu-in-termux")
        os.system("sh ubuntuc.sh")
        time.sleep(1)
        puts = {
            'status': "on"
        }
        with open(f'status/ubuntuc.json', 'w') as file:
            json.dump(puts, file)
        time.sleep(2)
        print("\n\n\nติดตั้งสำเร็จ")
        time.sleep(2)
    except:
        print("เกิดข้อผิดพลาด!!")

def installer(pkg_name):
    pkg = f"proot-distro install {pkg_name}"
    os.system(pkg)
    puts = {
            'status': "on"
        }
    with open(f'status/{pkg_name}.json', 'w') as file:
        json.dump(puts, file)
    time.sleep(2)
    print("\n\n\nติดตั้งสำเร็จ")
    time.sleep(2)