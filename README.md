# 036raspberry

Configuration Scripts for Arch Linux/Raspberry OS Lite and Oracle for Raspberry Pi 4

![Alt text](brandwhite.png?raw=true "Title")

- :warning: **If you want to install Oracle Linux in your raspberry for first time, please read the Oracle Linux secttion below**

## Prerequisites of use

- Medium understanding of GNU/Linux
- Some binaries, depending on the script
- Obviously, a Raspberry Pi 4

## Getting Started

- :bulb: **Features for config scripts**
  - Format, prepare and install in your SD Card with Arch Linux ARM automatically (archrpi4-install)
  - [yay](https://github.com/Jguer/yay): AUR Helper (Only Arch Linux)
  - [OhMyZsh](https://ohmyz.sh/): Best Framework for zsh
  - Aarch64 (arm64) Systems for performance
  - XFCE, GNOME, KDE menu options for install (Only Arch Linux)
  - Some Optimizations
  - Extra Software

- :warning: **Only Raspberry Pi aarch64**
  - armhf/armv7 not works

## archrpi4-install?

- :information_source: The objective of this script is detect your SD Card in a USB SD Reader, this will make partitions and format in that card, and this script downloads the latest Arch Linux ARM tarball for unpack and get your Arch system ready, it puts the archrpi4-config script in the home of root user, only for Raspberry Pi aarch64

- :warning: **Only Works in GNU/Linux**

  - Other UNIX systems may not work

- :warning: **Please install this software**

  - This scripts works in all GNU/Linux distros but you need this binaries
    - `dialog parted wget bsdtar (libarchive)`

## What About With Arch Linux ARM

The default login credentials is root / root

archpi4-install puts archrpi4-config script for run

```bash
cd /root/
./arch-config
```

If you don't have that script for any reason, you must update the Arch Linux ARM repositories, like this and clone

```bash
pacman-key --init
pacman-key --populate archlinuxarm
pacman -Sy git
git clone https://github.com/victor7w7r/036raspberry
cd 036raspberry
chmod +x arch-config
./arch-config
```

If you need to change to another timezone, use this order

- `ln -sf /usr/share/zoneinfo/REGION/CITY /etc/localtime"`

If you need to change to another locales, use this changes below, if you want more commands, please visit [Arch Linux Guide](https://wiki.archlinux.org/title/installation_guide)

```bash
#edit /etc/locale.gen 
vi /etc/locale.gen
#unmark your desired locale
#Save that file and use
locale-gen
```

## What About With Raspberry Pi OS Lite

The default login credentials is pi / raspberry

- :warning: **Only Works in Raspberry Pi OS Lite with aarch64**
  - This script may not work if you have a Raspberry Pi OS with the default desktop, if you don't have any idea to download the Lite version, [click here](https://downloads.raspberrypi.org/raspios_lite_arm64/images/)

- :warning: **Sid Sid Sid**
  - This script use Debian Sid repositories for install, at this moment, i didn't have problems with Sid packages while testing, but this repository is some unstable, if you have problems in system packages, wait some days and try to run the script again

You must update the repositories and install git, like this (run as superuser)

```bash
apt update
apt install git
git clone https://github.com/victor7w7r/036raspberry/
cd 036raspberry
chmod +x raspios-config
./raspios-config #(If you are not superuser, use with sudo)
```

## What About With Oracle Linux Config

The default login credentials is root / oracle

- :warning: **BEFORE START**
  - Run these commands, the objective is grow the root filesystem in your SD card and reboot

```bash
growpart /dev/mmcblk1 3
btrfs filesystem resize max /
reboot
```

- :bulb: **Features**

  - [Cockpit](https://cockpit-project.org/): Web Control for your server
  - XFCE as a default graphic environment with EPEL repository
  - KVM Hypervisor Suite
  - XRDP remote control

- :warning: **Only Works in Oracle Linux 8**
  - YUM commands don't work

You must update the repositories like this and install git, like this (run as superuser)

```bash
dnf update -y
dnf install git -y
git clone https://github.com/victor7w7r/036raspberry/
cd 036bootstrap
chmod +x olrpi4-config
./olrpi4-config #(If you are not superuser, use with sudo)
```

## Spanish Folder?

I born and live in Ecuador, of course i made a spanish scripts version, sorry for my bad english. :blush:

## TODO

- [ ] Code Optimization

## Development Suite

- Editor: [vscode](https://code.visualstudio.com/)
- Lint and Syntax Check: [ShellCheck](https://marketplace.visualstudio.com/items?itemName=timonwong.shellcheck)
- Operating System Tests: [Arch Linux ARM](https://archlinuxarm.org/)

## Thanks at this repositories for code snippets

- [Desktopify](https://github.com/wimpysworld/desktopify) (Convert Ubuntu Server for Raspberry Pi to a Desktop.)
- [ZeroTierOne](https://github.com/zerotier/ZeroTierOne) (Free VPN)
