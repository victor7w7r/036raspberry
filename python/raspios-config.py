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

LANGUAGE: int = 0;  SUDOUSER: str = ""

def main() -> None: 
    utils.clear(); language(); cover(); verify(); packages()
    newuser(); graphical(); ohmyzsh(); software(); finisher()
    
def printer(type: str, position: int) -> None:
    
    GREEN = '\033[92m';  WARNING = '\033[93m'; FAIL = '\033[91m';  ENDC = '\033[0m'

    DICTIONARY_ENG=(
        "Your Operating System is not GNU/Linux, exiting",
		"This script is only intended to run on aarch64 Devices.",
		"This script is only intended to run on Raspberry Pi 4 Devices.",
		"APT is not available in this system, this system isn't Debian?",
		"This Debian disto doesn't have a raspi-config app, please use Raspberry Pi OS Lite, exiting",
		"Ok, is Raspbery Pi OS, but this is not a Raspberry Pi OS Lite, exiting",
		"This PC doesn't have internet connection, please check",
		"Updating Debian repositories...",
		"lsb_release is not available in this system, installing",
		"Your Operating System is not Debian, exiting",
		"dialog is not available in this system, installing",
		"All dependencies is ok!",
		"=============== SYSTEM UPDATE  =============== \n",
		"=============== ROOT PASSWORD FOR YOUR SYSTEM =============== \n",
		"=============== CHANGE TO A SID REPOSITORIES AND DIST UPGRADE =============== \n",
		"=============== INSTALL CORE PACKAGES =============== \n",
		"=============== ADD A USER TO A SUDO GROUP =============== \n",
		"We create a script called omz.sh in your home directory, after reboot, use chmod +x at omz.sh",
		"READY!!!, Your RPI4 is succesfully configured, if you have errors, please report at 036raspberry in GitHub",
        "Your Python versión is less than 3.5, exiting",
        "You are not superuser, please run as root"
	)

    DICTIONARY_ESP=(
		"Este sistema no es GNU/Linux, saliendo",
		"Este script sólo se ejecuta en procesadores de aarch64",
		"Este script sólo se ejecuta en Raspberry Pi 4",
		"APT no está disponible, ¿Acaso esto no es Debian?",
		"Este distro de Debian no tiene la aplicación raspi-config, por favor use Raspberry Pi OS Lite, saliendo",
		"Bien, este es Raspberry Pi OS, pero no es Raspberry Pi OS Lite, saliendo",
		"No tienes conexión a internet, por favor revisa e inténtalo de nuevo",
		"Actualizando repositorios de Debian...",
		"lsb_release no está disponible, instalando",
		"Tu sistema operativo no es Debian, saliendo",
		"dialog is no está disponible, instalando",
		"Todo ok!",
		"=============== ACTUALIZACIÓN DEL SISTEMA =============== \n",
		"=============== CONTRASEÑA DE ROOT PARA EL SISTEMA =============== \n",
		"=============== CAMBIO A LOS REPOSITORIOS DE SID Y ACTUALIZACIÓN DE DIST =============== \n",
		"=============== INSTALACIÓN DE PAQUETES BASE =============== \n",
		"=============== AGREGAR UN USUARIO DE SUDO =============== \n",
		"Hemos creado un script llamado omz.sh en tu carpeta de home, después de reiniciar, usa chmod +x omz.sh",
		"LISTO!!!, Tu RPI4 fue configurado exitosamente, si tienes errores, repórtalo a 036raspberry",
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
		"The raspi-config app will be open, please change your configurations",
		"Write your new user: ",
		"More Sofware!!",
		"This script has a little pack of software, Do you like it?\n",
		"READY!!!, Your RPI4 is succesfully configured, if you have errors, please report at 036raspberry in GitHub"
	)

    DICTIONARY_ESP=(
        "Presione Enter para continuar...",
		"La aplicación de raspi-config se va a abrir, por favor cambia las configuraciones pertinentes",
        "Escribe tu nuevo usuario: ",
		"Más Sofware!!",
		"Este script tiene un pequeño pack de software, ¿Te gusta?\n",
		"LISTO!!!, Tu RPI4 fue configurado exitosamente, si tienes errores, reportalo a 036raspberry"
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
    if not commandverify("apt"):
        utils.clear(); printer("error",3); exit(1)
    if not commandverify("raspi-config"):
        utils.clear(); printer("error",4); exit(1)
    if commandverify("openbox-lxde-session"):
        utils.clear(); printer("error",5); exit(1)
    try: urlopen('http://google.com')
    except: utils.clear(); printer("error",6); exit(1)

    if not commandverify("lsb_release"):
        printer("print",8)
        system("apt install -y lsb-release &> /dev/null")
        
    LSB: str = Popen("lsb_release -is", 
                shell=True, stdout=PIPE).stdout.read().decode('utf-8').replace("\n", "")
        
    if LSB != "Debian":
        utils.clear(); printer("error",9); exit(1)
            
    if not commandverify("dialog"):
        printer("print",10)
        system("apt install -y dialog &> /dev/null")
        
    printer("print",11)     
    
    spinner = utils.spinning()
    for _ in range(15):
        stdout.write(next(spinner))
        stdout.flush(); sleep(0.1)  
        stdout.write('\b')

def packages() -> None:
    
    utils.clear()
    system(r"sed -i 's/^#PermitRootLogin\s.*$/PermitRootLogin yes/' /etc/ssh/sshd_config &> /dev/null")
    printer("print",12)
    system("apt upgrade -y")
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))
    utils.clear(); printer("print",13)
    system("passwd")
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))
    utils.clear(); printer("print",15)
    system("apt install -y cockpit git net-tools wget vim rsync neofetch \
		screen unrar p7zip vim network-manager-gnome zsh python3-pip libgles1 libopengl0 libxvmc1 libgpiod-dev python3-libgpiod")
    system("systemctl enable NetworkManager.service")
    with open('/etc/NetworkManager/NetworkManager.conf', 'a') as f:
        f.write("\nSet managed=true")
    system("systemctl disable dhcpcd.service")
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))
    d.msgbox(reader(1),7,50); system("raspi-config")
    
def newuser() -> None:
    
    global SUDOUSER

    utils.clear(); printer("print",16)
    SUDOUSER = input(reader(2))
    system(f"adduser {SUDOUSER}")
    system(f"usermod -aG sudo {SUDOUSER}")
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))

def graphical() -> None:
    
    utils.clear()
    print("=============== XFCE =============== \n")
    system("apt install -y xserver-xorg xfce4 xfce4-goodies xfce4-indicator-plugin \
		blueman ttf-ubuntu-font-family nemo cinnamon-l10n gdm3")
    system("touch /root/.xinitrc")
    with open('/root/.xinitrc', 'w') as f:
        f.writelines([
            "export XAUTHORITY=${HOME}/.Xauthority\n",
            "xfce4-session"
        ])  
    
    system(f"touch /home/{SUDOUSER}/.xinitrc")
    with open(f"/home/{SUDOUSER}/.xinitrc", 'w') as f:
        f.writelines([
            "export XAUTHORITY=${HOME}/.Xauthority\n",
            "xfce4-session"
        ])
        
    system(f"chown {SUDOUSER} /home/{SUDOUSER}/.xinitrc")
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
    printer("print",17)
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))
    
def software() -> None:
    
    system("systemctl mask lvm2-monitor")
    
    with open('/boot/config.txt', 'a') as f: 
        f.writelines([
            "\ndisable_overscan=1\n",
            'hdmi_drive=2',
        ])  
        
    if d.yesno(reader(4)+"""\n -> Pi-Apps \n -> baobab \n -> ntfs-3g \n -> exfat-utils \n -> xrdp \n -> xarchiver \n -> synaptic \n -> neofetch \n -> vlc \n -> gdebi \n -> numix-gtk-theme-git \n -> numix-icon-theme
            """ ,20,65) == d.OK:
        utils.clear()
        print("=============== SOFTWARE =============== \n")
    
        system("apt install -y xrdp gdebi synaptic aptitude neofetch vlc libwnck-common libwnck22 \
		baobab ntfs-3g exfat-fuse exfat-utils xarchiver numix-gtk-theme numix-icon-theme-circle")
        
        system(f"sudo -u {SUDOUSER} bash -c 'wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash'")
    
        system("adduser xrdp ssl-cert")
        system("systemctl enable xrdp")
        system("systemctl enable xrdp-sesman")
    
        print(" ")
        print("=============== OK =============== \n")
        input(reader(0))
        
    else: utils.clear(); return

def finisher() -> None:
    
    utils.clear(); d.msgbox(reader(5),7,50)
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