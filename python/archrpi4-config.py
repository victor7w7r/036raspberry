from subprocess import call, PIPE, Popen
from sys import stdin, stdout, platform, version_info
from platform import machine
from os import getuid, system
from re import search
from urllib.request import urlopen
from termios import tcgetattr, tcsetattr, TCSADRAIN
from time import sleep
from tty import setcbreak
from dialog import Dialog

d = Dialog(dialog="dialog")
d.set_background_title("036 Creative Studios")

SUDOUSER: str = ""

def main() -> None: 
    utils.clear(); language(); cover(); verify(); packages(); hostnamer()
    localer(); newuser(); graphical(); aur(); swapper(); ohmyzsh(); software(); finisher()
    
def printer(type: str, position: int) -> None:
    
    GREEN = '\033[92m';  WARNING = '\033[93m'; FAIL = '\033[91m';  ENDC = '\033[0m'

    DICTIONARY_ENG=(
        "Your Operating System is not GNU/Linux, exiting",
		"This script is only intended to run on aarch64 Devices.",
		"This script is only intended to run on Raspberry Pi 4 Devices.",
		"Arch Linux pacman is not available in this system, this system isn't Arch Linux?",
		"This PC doesn't have internet connection, please check",
		"Populating Arch ARM Keys..",
		"Updating Arch ARM Repositories...",
		"lsb_release is not available in this system, installing",
		"Your Operating System is not Arch Linux, exiting",
		"dialog is not available in this system, installing",
		"All dependencies is ok!",
		"=============== SYSTEM UPDATE AND INSTALL CORE PACKAGES =============== \n",
		"=============== ROOT PASSWORD FOR YOUR SYSTEM =============== \n",
		"=============== ADD A USER TO A SUDO GROUP =============== \n",
		"=============== BLUETOOTH AND SOUND =============== \n",
		"=============== AUR (YAY ASKS YOU YOUR PASSWORD, PAY ATTENTION) ===============  \n",
		"We create a script called omz.sh in your home directory, after reboot, use chmod +x at omz.sh",
		"We create a script called software.sh in your home directory, after reboot, use chmod +x at software.sh",
		"Please reboot your rpi4 to make changes",
        "Your Python versión is less than 3.5, exiting",
        "You are not superuser, please run as root"
	)

    DICTIONARY_ESP=(
        "Este sistema no es GNU/Linux, saliendo",
		"Este script solo se ejecuta en procesadores de aarch64",
		"Este script solo se ejecuta en Raspberry Pi 4",
		"Arch Linux pacman no está disponible, ¿Acaso esto no es Arch Linux?",
		"No tienes conexión a internet, por favor revisa e inténtalo de nuevo",
		"Llenando llaves de Arch ARM...",
		"Actualizando repositorios de Arch...",
		"lsb_release no está disponible, instalando",
		"Tu sistema operativo no es Arch Linux, saliendo",
		"dialog is no está disponible, instalando",
		"¡Todo ok!",
		"=============== ACTUALIZACIÓN DEL SISTEMA E INSTALAR PAQUETES BASE =============== \n",
		"=============== CONTRASEÑA DE ROOT PARA EL SISTEMA =============== \n",
		"=============== AGREGAR UN USUARIO DE SUDO =============== \n",
		"=============== BLUETOOTH Y SONIDO =============== \n",
		"=============== AUR (YAY PREGUNTA POR TU CONTRASEÑA, ESTATE ATENTO) ===============  \n",
		"Hemos creado un script llamado omz.sh en tu carpeta de home, después de reiniciar, usa chmod +x omz.sh",
		"Hemos creado un script llamado software.sh en tu carpeta de home, después de reiniciar, usa chmod +x software.sh",
		"Por favor reinicia tu rpi4 para realizar los cambios",
        "Tu versión de Python es menor que 3.5, saliendo",
        "Tú no eres superusuario, por favor ejecuta como root"
	)

    if LANGUAGE == 1:
        if type == "print": print(f"{DICTIONARY_ENG[position]}")
        elif type == "info": print(f"[{GREEN}+{ENDC}] INFO: {DICTIONARY_ENG[position]}")
        elif type == "warn": print(f"[{WARNING}*{ENDC}] WARNING: {DICTIONARY_ENG[position]}")
        elif type == "error": print(f"[{FAIL}!{ENDC}] ERROR: {DICTIONARY_ENG[position]}")
        else: print(f"[?] UNKNOWN: {DICTIONARY_ENG[position]}")
    else:
        if type == "print": print(f"{DICTIONARY_ESP[position]}")
        elif type == "info": print(f"[{GREEN}+{ENDC}] INFO: {DICTIONARY_ESP[position]}")
        elif type == "warn": print(f"[{WARNING}*{ENDC}] WARNING: {DICTIONARY_ESP[position]}")
        elif type == "error": print(f"[{FAIL}!{ENDC}] ERROR: {DICTIONARY_ESP[position]}")
        else: print(f"[?] UNKNOWN: {DICTIONARY_ESP[position]}")

def reader(position: int) -> str:
    
    DICTIONARY_ENG=(
        "Press Enter to continue...",
		"Please write your hostname (ex: A036-rpi4)",
		"America/Guayaquil is the timezone by default, if you want to change, here is the command\n ln -sf /usr/share/zoneinfo/REGION/CITY /etc/localtime",
		"Choose your locale, if you want to change to other locales, check the README of the Github of this project",
		"Write your new user: ",
		"Graphical Environment",
		"Choose a GUI, these are the common used, this script recommends XFCE",
		"More Sofware!!",
		"This script has a little pack of software, Do you like it?",
		"READY!!!, Your RPI4 is succesfully configured, if you have errors, please report at 036raspberry in GitHub",
	)

    DICTIONARY_ESP=(
        "Presione Enter para continuar...",
		"Por favor escriba su hostname (ej: A036-rpi4)",
		"America/Guayaquil es el timezone por defecto, si quieres cambiarlo por algun otro, aquí está la orden\n ln -sf /usr/share/zoneinfo/REGION/CITY /etc/localtime",
		"Elige tu Locale, si quieres cambiar a otros, revisa el README dentro del GitHub de este proyecto",
		"Escribe tu nuevo usuario: ",
		"Entorno Grafico",
		"Selecciona un GUI, estos son los mas usados, Este script recomienda XFCE",
		"Más Sofware!!",
		"Este script tiene un pequeño pack de software, ¿Te gusta?",
		"LISTO!!!, Tu RPI4 fue configurado exitosamente, si tienes errores, reportalo a 036raspberry",
	)

    if LANGUAGE == 1: return DICTIONARY_ENG[position]
    else: return DICTIONARY_ESP[position]

def commandverify(cmd: str) -> bool:
    return call("type " + cmd, shell=True, stdout=PIPE, stderr=PIPE) == 0

def language() -> None:
    
    global LANGUAGE
    
    print("Bienvenido /  Welcome")
    print("Please, choose your language / Por favor selecciona tu idioma")
    print("1) English"); print("2) Espanol")
    option: str = utils.char()
    if option == "1": LANGUAGE=1
    elif option == "2": LANGUAGE=2
    else: exit(1)

def cover() -> None:
    
    utils.clear()
    print(r'''                                     `"~>v??*^;rikD&MNBQku*;`                                           ''')
    print(r'''                                `!{wQNWWWWWWWWWWWWWWWNWWWWWWNdi^`                                       ''')
    print(r'''                              .v9NWWWWNRFmWWWWWWWWWWWWga?vs0pNWWWMw!                                    ''')
    print(r'''                            !9WWWWWWU>`>&WWWWWWUH!_JNWWWWWQz  ^EWWWWg|                                  ''')
    print(r'''                           _SWWWWWNe: /RWWWWWWNNHBRuyix&WWWWWg2?-"VNWWW6_                               ''')
    print(r'''                         "kWWWWWNz. .zNWWWWWWw=, ^NsLQNW**MWWWW&WQJuNWWWNr.                             ''')
    print(r'''                       .FNWWWWNu. rL&WWWWWWg!!*;^Jo!*BN0aFx)>|!;;;;;!~\r)xFwaao?|,                      ''')
    print(r'''                     .sNWWWWMi` -,#WWWWWWNi"` Siwu UWv  .;^|^;`               .!*lUSF*;                 ''')
    print(r'''                    )BWWWWWo.   9NWWWWWW0; ;PvLc*aU&^ |L=-``.;>*=                   ;)wmkL_             ''')
    print(r'''                  _QWWWWWq"   .aWWWWWWWs`  rF<>\^gQ, /i   ,;;.  !2                      ,*k0F\`         ''')
    print(r'''                 *NWWWWNv   ,/&WWWWWWNr "!SL92l)BU.  ^x   x. L,  I_                        `>P&F;       ''')
    print(r'''               `2WWWWWg;    !BWWWWWWD"   .s;!\xNa     /L,   !L`  P,                           .?&gr     ''')
    print(r'''              ,QWWWWWS`  >;LWWWWWWWk`_;!\u|  ^Ml        ;~!^,  `iv                              `?Ng^   ''')
    print(r'''             ^BWWWWWi   *i7NWWWWWWc "a;;?ii"~NV             `;?},                                 ,9WF  ''')
    print(r'''            >WWWWWB!  ` ;8WWWWWWM=  r>`;F/2wNc          .;||!,                                      oW#.''')
    print(r'''           ?WWWWW#"  `2;7NWWWWW&_ =_=u%ir`>Wi                                                        PW6''')
    print(r'''          rWWWWWc   `||>WWWWWWU.  r^?7;!v*W)                                                         ,WW|''')
    print(r'''         ^NWWWB!  ! \jrmWWWWWw  `vL.k*\vkW$>rr*r;`        ;rL{7)>!`                                   mWF''')
    print(r'''        .BWWW$,   ,u. PWWWWW) ,r`)|)!__LWv     `;L"     |s>:```._|JuL                                 qWE''')
    print(r'''        uWWWH` .vi"Fo*WWWWN>   ^v  r*`>W}                                                             &Ws ''')
    print(r'''       ;WWWP`  `=*ox_pWWWB; ^)i`9xr,#7W*            .     ,\*`                                       |WW! ''')
    print(r'''       SWWD` >LLr^_y*NWWQ"  ,<?P~|iF0W}            ~;   v_ `o;                                      .0WU''')
    print(r'''      ^WW0,.!F2xULFi5WW0` >7vr!!z_`*Wv             `|;;^!,~!`                                      .8W8.''')
    print(r'''      dWN;`>JyrkIr`!NWN! ,uFia!9?*2WI                                                             ;QWD.''')
    print(r'''     =WW7`_S)~Fxv| xWWi ;}drqa=;=uWRNmL,                                                         rWWt`  ''')
    print(r'''     DWP`;LiL;}c*rsWW&`,Po_e7L/ =Nc `>oD$aaw%ouic7)*r>=|^^~!;;;;;;;;;;;;;~^\>rvL{JctxiiiiuusoF2kgBS/  ''')
    print(r'''    ;WN\\Uy>*rF.,pWWWr-;?J"vov^^Nu         `.,"_;!~^\=>r*v?LL{}Jjjjjjj}}7?vr>\^!;____-""",,,..``    ''')
    print(r'''    iW?_**>^;>"~&EeWg=|liv*s!~?NL''')
    print(r'''    wWc*$>*~~L6Ni QW! \Uursx >WJ''')
    print(r'''    2M)o*_F "R0; .Wd~U7,``;*iN>''')
    print(r'''    xWe?vI7cMu`  ,W&>xssr~=PB|''')
    print(r'''    "W% ,cBZ_    `M2l\/i,,QQ,''')
    print(r'''     |U$di_       UBu>i)yBy`''')
    print(r'''                  ^Wx,rDR!''')
    print(r'''                   \ZUl^''')
    print(r'''.oPYo. .oPYo. .pPYo.   .oPYo.                       o   o                 .oPYo.   o              8  o                ''')
    print(r'''8  .o8     `8 8        8    8                       8                     8        8              8                   ''')
    print(r'''8 .P`8   .oP` 8oPYo.   8      oPYo. .oPYo. .oPYo.  o8P o8 o    o .oPYo.   `Yooo.  o8P o    o .oPYo8 o8 .oPYo. .oPYo.  ''')
    print(r'''8.d` 8    `b. 8`  `8   8      8  `` 8oooo8 .oooo8   8   8 Y.  .P 8oooo8       `8   8  8    8 8    8  8 8    8 Yb..   ''')
    print(r'''8o`  8     :8 8.  .P   8    8 8     8.     8    8   8   8 `b..d` 8.            8   8  8    8 8    8  8 8    8   `Yb. ''')
    print(r'''`YooP` `YooP` `YooP`   `YooP` 8     `Yooo` `YooP8   8   8  `YP`  `Yooo`   `YooP`   8  `YooP` `YooP`  8 `YooP` `YooP. ''')
    print(r''':.....::.....::.....::::.....:..:::::.....::.....:::..::..::...:::.....::::.....:::..::.....::.....::..:.....::.....:''')
    print(r''':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::''')
    print(r''':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::''')

def verify() -> None:
    
    PI: str = Popen(r"""cat /sys/firmware/devicetree/base/model
                    """, shell=True, stdout=PIPE).stdout.read().decode('utf-8').replace("\n", "")
    
    if version_info < (3, 5):
        utils.clear(); printer("error",19); exit(1)
    if platform != "linux":
        utils.clear(); printer("error",0); exit(1)
    if getuid() != 0:
        utils.clear(); printer("error",20); exit(1)
    if machine() != "aarch64":
        utils.clear(); printer("error",1); exit(1)
    if not search("^Raspberry\sPi\s4.*",PI):
        utils.clear(); printer("error",2); exit(1)
    if not commandverify("pacman"):
        utils.clear(); printer("error",3); exit(1)
    try: urlopen('http://google.com')
    except: utils.clear(); printer("error",4); exit(1)
    printer("print",5)
    system("pacman-key --init &> /dev/null")
    system("pacman-key --populate archlinuxarm &> /dev/null ")
    printer("print",6) 
    system("pacman -Sy &> /dev/null")
    if not commandverify("lsb_release"):
        printer("print",7)
        system("pacman -S lsb-release --noconfirm &> /dev/null")
    
    IS_ARCH = Popen("lsb_release -is", shell=True, stdout=PIPE).stdout.read().decode('utf-8').replace("\n", "")
    
    if IS_ARCH != "Arch":
        utils.clear(); printer("error",8); exit(1)
    if not commandverify("dialog"):
        printer("error",9)
        system("pacman -S dialog --noconfirm &> /dev/null")
        
    system("pacman -S ncurses --noconfirm &> /dev/null")
    printer("print",10)
    
    spinner = utils.spinning()
    for _ in range(15):
        stdout.write(next(spinner))
        stdout.flush(); sleep(0.1)  
        stdout.write('\b')
    
def packages() -> None:
    
    utils.clear(); printer("print",11)
    system("systemctl enable sshd")
    system("systemctl start sshd")
    system("pacman -Syyu --noconfirm")
    system("pacman -S sudo git wget rsync networkmanager neofetch screen unrar p7zip vim zsh python-pip --noconfirm")
    print("=============== OK =============== \n")
    input(reader(0))
    utils.clear(); printer("print",12)
    system("passwd")
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))
    
def hostnamer() -> None:
    
    response = d.inputbox(reader(1), 8, 80)
    if response[0] == "ok":
        with open('/etc/hostname', 'w') as f:
            f.write(response[1])
        with open('/etc/hosts', 'a') as f:
            f.write(f"\n127.0.1.1        {response[1]}")
    elif response[0] == "cancel": exit(0) 

def localer() -> None:
    
    utils.clear(); d.msgbox(reader(2),11,50)
    system("ln -sf /usr/share/zoneinfo/America/Guayaquil /etc/localtime")
    system("hwclock --systohc")
    
    choices = [("Spanish/Espanol","es_ES"),("English","en_US")]
    response = d.menu(reader(3), 15, 50, 4, choices)
    if response[0] == "ok" and response[1] == "Spanish/Espanol":
        utils.clear()
        system("sed -i 's/^#es_ES.UTF-8 UTF-8/es_ES.UTF-8 UTF-8/' /etc/locale.gen")
        system("locale-gen")
        with open('/etc/locale.conf', 'w') as f:
            f.writelines([
                'LANG="es_ES.UTF-8"\n',
                'LC_TIME="es_ES.UTF-8"\n',
                'LANGUAGE="es_EC:es_ES:es"'
            ])
    elif response[0] == "ok" and response[1] == "English":
        utils.clear()
        system("sed -i 's/^#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen")
        system("locale-gen")
        with open('/etc/locale.conf', 'w') as f:
            f.writelines([
                'LANG="en_US.UTF-8"\n',
                'LC_TIME="en_US.UTF-8"\n',
                'LANGUAGE="es_US:en"'
            ])
    else: utils.clear(); exit(0)

def newuser() -> None:
    
    global SUDOUSER
    utils.clear(); printer("print",13)
    SUDOUSER = input(reader(4))
    system(f"useradd --create-home {SUDOUSER}")
    system(f"passwd {SUDOUSER}")
    system(f"usermod -aG wheel,storage,power {SUDOUSER}")
    system("userdel alarm")
    system("sed -i 's/^#.*%wheel ALL=(ALL:ALL) ALL$/%wheel ALL=(ALL:ALL) ALL/' /etc/sudoers &> /dev/null")
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))
    
def graphical() -> None:
    
    utils.clear()
    choices = [
        ("XFCE","Xfce Desktop Environment"),
        ("GNOME","GNOME Desktop Environment"),
        ("KDE","KDE Desktop Environment"),
        ("XORG","Minimal xorg Desktop"),
        ("NOGUI","No GUI")
    ]
    response = d.menu(reader(6), 15, 50, 4, choices)
    if(response[0] == "ok" and response[1] == "XFCE"):
        utils.clear()
        print("=============== XFCE =============== \n")
        system("pacman -S xorg-server xf86-video-fbdev xorg-xinit --noconfirm")
        system("pacman -S xfce4 gdm xfce4-goodies ttf-ubuntu-font-family gtk-engines gtk-engine-murrine --noconfirm")
        system("pacman -S gnome-themes-standard xdg-user-dirs ttf-dejavu gvfs xfce4-notifyd network-manager-applet volumeicon --noconfirm")
        system("systemctl enable gdm")
        system(f"touch /HOME/{SUDOUSER}/.xinitrc")
        system(f"touch /root/.xinitrc")
        with open(f'/HOME/{SUDOUSER}/.xinitrc', 'w') as f: 
            f.writelines([
                'export XAUTHORITY=${HOME}/.Xauthority\n',
                'exec dbus-run-session -- startxfce4',
            ])
        with open(f'/root/.xinitrc', 'w') as f: 
            f.writelines([
                'export XAUTHORITY=${HOME}/.Xauthority\n',
                'exec dbus-run-session -- startxfce4',
            ])
        print(" ")
        print("=============== OK =============== \n")
        input(reader(0))
    elif(response[0] == "ok" and response[1] == "GNOME"):
        utils.clear()
        print("=============== GNOME =============== \n")
        system("pacman -S xorg-server xf86-video-fbdev xorg-xinit --noconfirm")
        system("pacman -S gnome gdm gnome-themes-standard network-manager-applet --noconfirm")
        system("systemctl enable gdm")
        print(" ")
        print("=============== OK =============== \n")
        input(reader(0))
    elif(response[0] == "ok" and response[1] == "KDE"):
        utils.clear()
        print("=============== KDE =============== \n")
        system("pacman -S xorg-server xf86-video-fbdev xorg-xinit --noconfirm")
        system("pacman -S plasma plasma-wayland-session kde-applications network-manager-applet network-manager-applet volumeicon --noconfirm")
        system("systemctl enable sddm.service")
        print(" ")
        print("=============== OK =============== \n")
        input(reader(0))
    elif(response[0] == "ok" and response[1] == "XORG"):
        utils.clear()
        print("=============== XORG ONLY =============== \n")
        system("pacman -S xorg-server xf86-video-fbdev xorg-xinit --noconfirm")
        print(" ")
        print("=============== OK =============== \n")
        input(reader(0))
        
    elif(response[0] == "ok" and response[1] == "NOGUI"): return
    else: exit(0)
    utils.clear(); printer("print",14)
    system("pacman -S alsa-utils alsa-firmware alsa-lib alsa-plugins pulseaudio-alsa pulseaudio-bluetooth bluez-utils libmm-glib modemmanager blueman --noconfirm")
    system("sudo systemctl enable ModemManager")
    system("sudo systemctl enable bluetooth")
    system("sudo systemctl start ModemManager")
    system("sudo systemctl start bluetooth")
    
    with open('/boot/config.txt', 'w') as f: 
        f.writelines([
            "enable_uart=1\n",
            "dtparam=audio=on\n",
            "hdmi_drive=2\n",
            "audio_pwm_mode=2\n",
            "disable_overscan=1\n",
            "gpu_mem=64\n",
            "cma=512\n",
            "dtoverlay=vc4-fkms-v3d\n",
            "max_framebuffers=2"
        ])
        
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))
    
def aur() -> None:
    
    utils.clear(); printer("print",15)
    system("pacman -S --needed base-devel fakeroot packer --noconfirm")
    system(f"sudo -u {SUDOUSER} bash -c 'cd; git clone https://aur.archlinux.org/yay-bin.git'")    
    system(f"sudo -u {SUDOUSER} bash -c 'cd; cd yay-bin; makepkg -si'") 
    system(f"sudo -u {SUDOUSER} bash -c 'cd; rm -rf yay-bin'") 
    
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))
    
def swapper() -> None:
    
    utils.clear()
    print("=============== SWAPPING =============== \n")
    system(f"sudo -u {SUDOUSER} bash -c 'cd; git clone https://aur.archlinux.org/zramswap.git'")
    system(f"sudo -u {SUDOUSER} bash -c 'cd; cd zramswap; makepkg -si'") 
    system(f"sudo -u {SUDOUSER} bash -c 'cd; rm -rf zramswap'")
    system("systemctl enable zramswap.service")
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))
    
def ohmyzsh() -> None:
    
    utils.clear()
    print("=============== OMZ =============== \n" )
    system(f"touch /home/{SUDOUSER}/omz.sh")
    with open(f'/home/{SUDOUSER}/omz.sh', 'w') as f: 
        f.writelines([
            "#!/bin/bash\n",
            'sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"\n',
            'sed -i -e \'s/ZSH_THEME=.*/ZSH_THEME=\\\"pmcgee\\\"/\' .zshrc\n',
            "sed -i -e '/^source $ZSH.*/i ZSH_DISABLE_COMPFIX=true' .zshrc\n",
            r"git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting",
            "\n",
            r"git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions",
            "\n",
            "sed -i -e 's/plugins=(.*/plugins=(git zsh-syntax-highlighting zsh-autosuggestions)/' .zshrc"
        ])
    
    system(f'chown {SUDOUSER} /home/{SUDOUSER}/omz.sh')
    system(f'chmod +x /home/{SUDOUSER}/omz.sh')
    system("touch /root/omz.sh'")
    with open('/root/omz.sh', 'w') as f: 
        f.writelines([
            "#!/bin/bash\n",
            'sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"\n',
            'sed -i -e \'s/ZSH_THEME=.*/ZSH_THEME=\\\"pmcgee\\\"/\' .zshrc\n',
            "sed -i -e '/^source $ZSH.*/i ZSH_DISABLE_COMPFIX=true' .zshrc\n",
            r"git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting",
            "\n",
            r"git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions",
            "\n",
            "sed -i -e 's/plugins=(.*/plugins=(git zsh-syntax-highlighting zsh-autosuggestions)/' .zshrc"
        ])
    
    system(f'chmod +x /root/omz.sh')
    
    printer("print",16)

    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))

def software() -> None: 
    
    system('systemctl mask lvm2-monitor')
    
    if d.yesno(reader(8)+"""\n -> baobab \n -> ntfs-3g \n -> exfatprogs \n -> exfat-utils \n -> xrdp \n -> xarchiver \n -> xorgxrdp \n -> visual-studio-code \n -> rpi-eeprom-git \n -> rpi-imager \n -> numix-gtk-theme-git \n -> numix-icon-theme \n -> preload
        """ ,20,65) == d.OK:
        utils.clear()
        system(f'touch /home/{SUDOUSER}/software.sh')
        print("=============== SOFTWARE =============== \n")
        with open('/etc/X11/Xwrapper.config', 'w') as f: f.write('allowed_users=anybody')
        with open(f'/home/{SUDOUSER}/software.sh', 'w') as f:
            f.writelines([
                "#!/bin/bash\n",
                "yay -S baobab ntfs-3g exfatprogs exfat-utils\\\n",
                "xarchiver gparted xrdp \\\n",
                "xorgxrdp pi-bluetooth visual-studio-code-bin preload \\\n",
                "rpi-eeprom rpi-imager box64 \\\n",
                "systemctl enable xrdp\n",
                "systemctl enable xrdp-sesman\n",
                "systemctl enable preload\n",
            ])
        system(f"chown {SUDOUSER} /home/{SUDOUSER}/software.sh")
        system(f"chmod +x /home/{SUDOUSER}/software.sh")
        printer("print",17)
        print(" ")
        print("=============== OK =============== \n")
        input(reader(0))

def finisher() -> None:
    
    utils.clear(); d.msgbox(reader(9),7,50)
    utils.clear(); printer("print", 18); exit(0)

class utils:
    
    def clear() -> None: system('clear')
    
    def char() -> str:
        fd = stdin.fileno()
        oldSettings = tcgetattr(fd)
        try:
            setcbreak(fd)
            answer = stdin.read(1)
        finally:
            tcsetattr(fd, TCSADRAIN, oldSettings)
        return answer

    def spinning():
        while True:
            for cursor in '|/-\\':
                yield cursor

if __name__ == "__main__":
    main()