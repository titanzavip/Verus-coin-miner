# OPEN TERMUN AUTO FILE ONE
[ Download Hibernator ](https://raw.githubusercontent.com/titanzavip/Verus-coin-miner/main/Hibernator%20v2.22.3%20%5BPremium%5D-M.apk)
<br>
[ Download No Screen Off ](https://raw.githubusercontent.com/titanzavip/Verus-coin-miner/main/No%20Screen%20Off_v1.16_apkpure.com.apk)  
<br>
* STEP 1
```
termux-setup-storage
```
```
pkg install nano
```
```
mkdir .termux/boot
```
```
cd .termux/boot
```
```
nano boot.sh
```
เพิ่มข้อมูลนี้ใน boot.sh
```
#!/data/data/com.termux/files/usr/bin/sh
termux-wake-lock
. $PREFIX/etc/profile
```
รอ RE-Termux 
```
cd /data/data/com.termux/files/usr/etc
```
```
nano profile
```
เพิ่มข้อมูลนี้ใน profile บรรทัดสุดท้าย
```
cd && cd /data/data/com.termux/files/usr/etc/os-install
sh ubun.sh
```
```
cd
```
* STEP 2
```
pkg install git
```
```
git clone https://github.com/titanzavip/os-installer.git
```
```
cd os-installer
```
```
chmod +x os-installer
```
```
sh build.sh
```
* STEP 3  
```
apt-get update
```
```
apt-get install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential git nano
```
```
git clone https://github.com/mantvmass/auto-file-two
```
```
cd auto-file-two
```
```
chmod +x edit-miner
```
```
chmod +x run-miner
```
```
sh setup.sh
```
```
run-miner
```
```
cd && cd ../etc
```
```
nano bash.bashrc
```
* เพิ่มบรรทัดแรกเป็น
```
run-miner
```
```
cd && cd ../etc/auto_miner/ccminer
```
```
chmod +x build.sh
```
```
chmod +x configure.sh
```
```
chmod +x autogen.sh
```
```
./build.sh
```
```
edit-miner
```
```
run-miner
```
* STEP 4
* Pool
```
stratum+tcp://verushash.asia.mine.zergpool.com:3300
```
* Wallet
```
DRkNn7KAtpiRk2ySwtxKWHMHTLPndREFW9
```
* -p 
```
c=DOGE,mc=VRSC,ID=Miner-001
```
