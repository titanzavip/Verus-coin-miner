โปรแกรม

termux-setup-storage

pkg install nano


mkdir .termux/boot

cd .termux/boot

nano boot.sh


#!/data/data/com.termux/files/usr/bin/sh
termux-wake-lock
. $PREFIX/etc/profile

(ให้เรากดคำว่า( CTRLต่อด้วยXตามด้วยY)

(หลังจากนั้นรีสตาทเครื่องและรอจนกว่าtermux จะขึ้นเอง ถ้าหากขึ้นแล้วก็รันคำสั่งต่อไป)


cd /data/data/com.termux/files/usr/etc

nano profile


cd && cd /data/data/com.termux/files/usr/etc/os-install
sh ubun.sh

(ให้เรากดคำว่า CTRLต่อด้วยXตามด้วยY)


cd

pkg install git


git clone https://github.com/mantvmass/os-installer

cd os-installer


chmod +x os-installer


sh build.sh

(เดี๋ยวจะมีถาม( ? )ให้เรากด (enter 2 )ครั้งแล้วก็รออัพเดทเสร็จ
แล้วก็ต่อด้วย( 1 enter) รอกอัพเดทเสร็จ
แล้วก็ต่อด้วย( Y enter) รออัพโหลดเสร็จ
แล้วตามด้วย ( 1 enter อีกครั้ง)

apt-get update



apt-get install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential git nano

(ให้เราตอบ (Y)
แล้วก็รออัพเกรดอัพเดทใหม่)

git clone https://github.com/mantvmass/auto-file-two

cd auto-file-two

chmod +x edit-miner

chmod +x run-miner

sh setup.sh

(มีคำถามให้เราใส่)
(6)ต่อ(12)ต่อ(12)ต่อ(12)

run-miner


cd && cd ../etc


nano bash.bashrc

run-miner

(ให้กด CTRLแล้วก็ X มันจะขึ้น yes & no
ให้เราตอบ y)


cd && cd ../etc/auto_miner/ccminer

chmod +x build.sh

chmod +x configure.sh

chmod +x autogen.sh

./build.sh

(แล้วก็รออัพเดทอัพเกรดเสร็จแล้วให้เราออกจากโปรแกรม termux แล้วก็เข้าใหม่
เพื่อที่จะเอาโปรแกรม Pool กับกระเป๋ามาใส่ครับ)
