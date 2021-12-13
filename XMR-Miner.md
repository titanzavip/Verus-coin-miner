* XMR Miner
* Run Commands

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
git clone https://github.com/mantvmass/os-installer
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
pkg install update
```
```
pkg install upgrade
```
```
apt install git
```
```
apt install wget
```
```
apt install proot
```
```
termux-setup-storage
```
```
git clone https://github.com/Neo-Oli/termux-ubuntu 
```
```
cd termux-ubuntu
```
```
apt update
```
```
apt upgrade
```
```
Install cmake
```
```
git clone https://github.com/xmrig/xmrig
```
```
cd xmrig
```
```
mkdir build
```
```
cd build
```
```
cmake-DWITH_HWLOC%3DOFF ..
```
```
make
```
```
/xmrig -o xmr-au1.nanopool.org:14433 -u 89z81VijZjFXaABwBAZ8W94X8h6zihFcbMHGDwCrGQSkf8hzwJUoZT9cGQzwtsMVakg1qwd5n3nS1hhErZnqFVsjTA7RSZP-tls-coin monero
```
