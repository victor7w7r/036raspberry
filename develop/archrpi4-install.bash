#!/usr/bin/env bash

if [ "$(id -u)" -ne 0 ]; then
	echo "ERROR: You need to be root."
	exit 1
fi

rm /tmp/diskmenutemp.sh* 2> /dev/null
	
DISKMENUTEMP=/tmp/diskmenutemp.sh.$$

function cleanup { rm $DISKMENUTEMP; $; exit; }

trap cleanup; SIGHUP SIGINT SIGTERM

function core { clear; cover; sleep 1s; verify; usbstat; diskmenu; }

function cover {
	echo '          					    ``...`                                                    '
	echo '                                      `..:/+++/--/shdmmmmmhy+:.`                                              '
	echo '                                  `-+ydmMMMMMMMMMMMMMMMMMMMMMMNds:`                                           '
	echo '                               `/ymMMMMMNmNMMMMMMMMMMMMNhooyNNMMMMmy:`                                        '
	echo '                             -yNMMMMMNy//hMMMMMMMNyymMMMMNdhm-:sNMMMMd/                                       '
	echo '                           .yMMMMMMNo.`oMMMMMMMMod: .ydMMMMMM+.``omMMMMh.                                     '
	echo '                         `oNMMMMMMo` -MMMMMMMMMmdmMNNmyNMMMMMMMNy/`oNMMMN/                                    '
	echo '                        /mMMMMMMs.  oMMMMMMMNo.  :Mo:hMMs:mMMMMNMMmyhMMMMMo-`                                  '
	echo '                      -hMMMMMMy. .sdMMMMMMMh.o/-/sy:+NMNhys+/:-......--:/+oshddyo/-`                           '
	echo '                    `sNMMMMMh: ` +MMMMMMMMo` .dshs yMh.` `.-..               ``-/oydds/.                       '
	echo '                   /mMMMMMm/`  odMMMMMMMm- s::ydomsMy``+o+:-:/++/`                 `./sdds/.                   '
	echo '                 `yMMMMMMs`   -mMMMMMMMh.  +y+/:-hMs `h-       `:y.                    `.+hmh+.               '
	echo '                -dMMMMMm:  `.:NMMMMMMMs` ./hyso/dMo  :y   //:/-  :y                        ./hmh/`            '
	echo '               :mMMMMMd.   `+NMMMMMMN+ .-ohyyhhhMo   `h.  :: `y   N                           .odmo.           '
	echo '              +NMMMMMy`  `./NMMMMMMN/   `+/-:/yMo     .o:.`.-+-  -d                             `/dNs.        '
	echo '             oMMMMMMs`  o-+MMMMMMMN:`::/oo-  +Ms        -----`  -y-                               `oNm/       '
	echo '           `sMMMMMMo   +yoNMMMMMMm-`o/`-oyh`+Ms          `````-oo`                                  -dMy`     '
	echo '          `yMMMMMN/    /yNMMMMMMd. -h--h+-ysMy          `-////:`                                     `dMh`    '
	echo '          yMMMMMN:  -+:oMMMMMMMd````y++o++sNh`                                                        `mMy    '
	echo '        /MMMMMy`   /+ooMMMMMMh`  ./+N:-+oNm`                                                            mMd   '
	echo '       .NMMMMs  `+ +++MMMMMMy   so++s++oNNs+oooo/-       `/oysyyso/.                                    yMM   '
	echo '       dMMMM+    :s `mMMMMMs `o +++o.-:mN.     `-o-     -h+-`   `-/sh+                                  yMM   '
	echo '      /MMMM+  -/o msoMMMMMo   :y `-s-`dN-                            `                                  hMN    '
	echo '      dMMM+   +oooy:mMMMMo ./o`do:+y/yM/                  `:/`                                         `NMh    '
	echo '     /MMMs  --:+s+osMMMM+  :sy/d//+hNM+            `/   .  `:y                                         sMM:    '
	echo '     mMMd` .mss+`hoyMMM+  `./ss++oohMo             .+  `y+/:+:                                        :MMy     '
	echo '    /MMN. o+mhym/yyNMMs  syo+./y. +Ny               -:::. ``                                         :NMd`     '
	echo '    dMM/`-ysoshh.`+MMm``-yhhdohysyMM:                                                               /NMd.      '
	echo '   :MMy.-sd:oy+y.`dMM/ :od+dhs./oNmmNh/.                                                          `oMMs`      '
	echo '   yMN.-/oy.+yys-hMMd -hy:yy+o `dm.`/ymdyysooo+///::--.......................--::////////+++++oooshNmo   	    '
	echo '  `MMy/+yyosy/-/dMMM/:/ss-oys/`dN-    `.--:://++ooosssyyyyyhyyyyhhhhhhhyyyhyyyssoo++++++///////::::-`         '
	echo '  +Mm`.+dy+sy.-mmNMm`.oys/yyo+hN:                                                                             '
	echo '  yMo/m+.`.-o/Nd-MMo+hho:oh``yM/                                                                               '
	echo '  hMd+ysy+:/yMy`:Mm :+ysoo+ yM/                                                                                '
	echo '  yM/h+-h``hMo  +My+d:`- :syM+                                                                                '
	echo '  oMds+ms+Nm-   +Mm/yyd//:hM/                                                                                  '
	echo '  -Mh  :dNs`    /Mod+:h``dN:                                                                                  	'
	echo '   oNdmms.      -Mmhody/mm-                                                                                    '
	echo '    .--`         mN. -yMy.                                                                                     '
	echo '                  /Nhsmd/                                                                                       '
	echo '                  -/+-`                     '
	echo '.oPYo. .oPYo. .pPYo.   .oPYo.                       o   o                 .oPYo.   o              8  o                '
	echo '8  .o8     `8 8        8    8                       8                     8        8              8                   '
	echo '8 .P`8   .oP` 8oPYo.   8      oPYo. .oPYo. .oPYo.  o8P o8 o    o .oPYo.   `Yooo.  o8P o    o .oPYo8 o8 .oPYo. .oPYo.  '
	echo '8.d` 8    `b. 8`  `8   8      8  `` 8oooo8 .oooo8   8   8 Y.  .P 8oooo8       `8   8  8    8 8    8  8 8    8 Yb..   '
	echo '8o`  8     :8 8.  .P   8    8 8     8.     8    8   8   8 `b..d` 8.            8   8  8    8 8    8  8 8    8   `Yb. '
	echo '`YooP` `YooP` `YooP`   `YooP` 8     `Yooo` `YooP8   8   8  `YP`  `Yooo`   `YooP`   8  `YooP` `YooP`  8 `YooP` `YooP. '
	echo ':.....::.....::.....::::.....:..:::::.....::.....:::..::..::...:::.....::::.....:::..::.....::.....::..:.....::.....:'
	echo ':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
	echo ':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
}

function usbstat {

	VERIFYUSB=$(find /dev/disk/by-id/ -name 'usb*' | sort -n | sed 's/^\/dev\/disk\/by-id\///')
	if [ "$VERIFYUSB" == "" ]; then
		clear
		echo "ERROR: There's no USB drives connected in this PC, please connect your SD Card in a USB SD Card Reader"
		exit 1
	fi
}

function whichverify() {
	stat=$(which "$1" 2>&1)
	if [[ "$stat" =~ which:* ]]; then 
		return 1
	else
		return 0
	fi
}

function verify {

    OPERATING=$(uname -o)

	SELECTOR=""

	if [ "$OPERATING" != "GNU/Linux" ]; then
		clear
		echo 'ERROR: Your Operating System is not GNU/Linux, exiting'
		exit 1
	fi

	SELECTOR="fsck.f2fs"
	whichverify "$SELECTOR"
	local res=$?
	if [ $res -eq 1 ]; then
        clear
		echo "f2fs-tools is not available in this system, please install it"
		exit 1
	fi

    PING=$(ping -c 1 8.8.8.8 2>&1) 

    if [[ "$PING" =~ unreachable* ]]; then
		clear
		echo "ERROR: This PC doesn't have internet connection, please check"
		exit 1
	fi

	SELECTOR="dialog"
	whichverify "$SELECTOR"
	local res=$?

	if [ $res -eq 1 ]; then
		echo "dialog is not available in this system, please install it"
		exit 1
	fi
	
	SELECTOR="parted"
	whichverify "$SELECTOR"
	local res=$?

	if [ $res -eq 1 ]; then
		echo "parted is not available in this system, please install it"
		exit 1
	fi
	
	SELECTOR="wget"
	whichverify "$SELECTOR"
	local res=$?

	if [ $res -eq 1 ]; then
		echo "wget is not available in this system, please install it"
		exit 1
	fi
	
	SELECTOR="bsdtar"
	whichverify "$SELECTOR"
	local res=$?

	if [ $res -eq 1 ]; then
		echo "bsdtar is not available in this system (libarchive), please install it"
		exit 1
	fi

	echo "All dependencies is ok!"

	START=$(date +%s)
	CHARS="/-\|"

	while [[ $(($(date +%s) - START)) -lt 2 ]]; do
		for (( i=0; i<${#CHARS}; i++ )); do
			sleep 0.08
			echo -en "${CHARS:$i:1}" "\r"
		done
	done

}

function diskmenu {

	clear
	usbstat

	dialog --msgbox "ATTENTION!!! Your SD card would be listed as a USB device, ensure that your SD is empty and ready for format" 7 70

	clear

	DIRTYDEVS=()
	BLOCK=()

	USBS=$(find /dev/disk/by-id/ -name 'usb*' | sort -n | sed 's/^\/dev\/disk\/by-id\///') # usb-USB3.0_high_speed_000000123AFF-0:0 ...

	for DEVICE in $USBS; do
		DIRTYDEVS[$COUNT]=$(readlink "/dev/disk/by-id/$DEVICE") # ../../sda ../../sda1 ... 
		COUNT=$(( COUNT + 1 ))
	done

	for DEV in "${DIRTYDEVS[@]}"; do

		ABSOLUTEPARTS=$(echo "$DEV" | sed 's/^\.\.\/\.\.\//\/dev\//' | sed '/.*sd[[:alpha:]]$/d') #/dev/sda1 /dev/sda2 ...

		if [ "$ABSOLUTEPARTS" == "" ]; then
			BLOCK[$BLOCKCOUNT]=$(echo "$DEV" | sed 's/^\.\.\/\.\.\///') #sda sdb 
			BLOCKCOUNT=$(( BLOCKCOUNT + 1 ))
		fi
	done

	COUNT=0
	MODEL=0
	DEVICE=0
	ARGSUSB=()

	for PART in "${BLOCK[@]}"; do
		DEVICE="/dev/$PART"
		BLOCKSTAT="${BLOCK[$COUNT]}"
		SIZE=$(lsblk -no SIZE /dev/"$PART" | head -1 | sed s/..//)
		MODEL="$(cat /sys/class/block/"$BLOCKSTAT"/device/model)" #KINGSTON 
		ARGSUSB+=("$DEVICE" "$MODEL $SIZE")
		COUNT=$(( COUNT + 1 ))
	done

	dialog --clear --backtitle "036 Creative Studios" --title "Format a Device" \
		--menu "Choose a device"\
		15 50 4 "${ARGSUSB[@]}" 2>"${DISKMENUTEMP}"

	CHOICE=$(<"${DISKMENUTEMP}")

	case $CHOICE in
		"$CHOICE") diskformat "$CHOICE";;
		*) clear;;
	esac

}

function diskformat() {
	
	if [ "$1" == "" ]; then
		clear
		exit 0
	fi

	dialog --title "DANGER ZONE!!!" --backtitle "036 Creative Studios" \
		--yesno "This device will be format Continue? \n $1" 7 60

	clear
	response=$?

	if [ $response -eq 0 ]; then
	
		echo -e "=============== NEW PARTITION TABLE TO SD CARD =============== \n" 

		parted --script "$1" \
			mklabel msdos \
			mkpart primary fat32 1MiB 200MiB \
			set 1 boot on \
			mkpart primary f2fs 200MiB 100% \
			print

		echo " "
		echo -e "=============== OK =============== \n" 
		read -r -p "Press Enter to continue..."
		clear

		echo -e "=============== FORMAT/MOUNT ROOT AND BOOT FILESYSTEM =============== \n" 

		mkfs.f2fs -f "$1"2
		mkfs.fat -F32 "$1"1
		mkdir /mnt/boot 
		mkdir /mnt/root
		mount "$1"2 /mnt/root
		mount "$1"1 /mnt/boot

		echo " "
		echo -e "=============== OK =============== \n" 
		read -r -p "Press Enter to continue..."
		clear

		baseinstall

	else
		clear
		exit 1
	fi

}
function baseinstall {

	echo -e "=============== NEW PARTITION TABLE TO SD CARD =============== \n" 

	wget http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-aarch64-latest.tar.gz -P /mnt/root/
	bsdtar -xpf /mnt/root/ArchLinuxARM-rpi-aarch64-latest.tar.gz -C /mnt/root/
	sync
	rm /mnt/root/ArchLinuxARM-rpi-aarch64-latest.tar.gz
	mv /mnt/root/boot/* /mnt/boot/
	sed -i 's/mmcblk0/mmcblk1/g' /mnt/root/etc/fstab
	sed -i 's/^#PermitRootLogin\s.*$/PermitRootLogin Yes/' \
		/mnt/root/etc/ssh/sshd_config &> /dev/null

	umount /mnt/boot 
	umount /mnt/root 
	rm -rf /mnt/boot 
	rm -rf /mnt/root

	echo " "
	echo -e "=============== OK =============== \n" 
	read -r -p "Press Enter to continue..."
	clear

	finisher

}

function finisher {
	clear
	dialog --msgbox 'READY!!!, Your SD was installed with Arch Linux ARM for Raspberry PI 4, if you have errors, please report at 036raspberry in GitHub' 7 50
	clear
	echo "Please reboot yout server to make changes"
	exit 0
}

core

[ -f $DISKMENUTEMP ] && rm $DISKMENUTEMP