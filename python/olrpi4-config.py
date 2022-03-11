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

LANGUAGE: int = 0; XRDPTOGGLE=1; SUDOUSER: str = ""

def main() -> None: 
    utils.clear(); language(); cover(); verify(); packages(); hostnamer(); localer()
    cockpit(); newuser(); graphical(); remote(); kvm(); ohmyzsh(); software(); finisher()
    
def printer(type: str, position: int) -> None:
    
    GREEN = '\033[92m';  WARNING = '\033[93m'; FAIL = '\033[91m';  ENDC = '\033[0m'

    DICTIONARY_ENG=(
        "Your Operating System is not GNU/Linux, exiting",
		"This script is only intended to run on Oracle Linux",
		"This script is only intended to run on aarch64 devices.",
		"This script is only intended to run on Raspberry Pi 4 Devices.",
		"DNF is not available in this system, this system isn't Oracle Linux, please use Oracle Linux 8?",
		"This PC doesn't have internet connection, please check",
		"Updating Oracle Linux Repositories... Please Wait",
		"dialog is not available in this system, installing",
		"All dependencies is ok!",
		"=============== INSTALL CORE PACKAGES =============== \n",
		"=============== COCKPIT SERVICE (IP:9090) =============== \n",
		"=============== ADD A USER TO A SUDO GROUP =============== \n",
		"We create a script called omz.sh in your home directory, after reboot, use chmod +x at omz.sh",
		"Please reboot your server to make changes",
        "Your Python versión is less than 3.5, exiting",
        "You are not superuser, please run as root"
	)

    DICTIONARY_ESP=(
        "Este sistema no es GNU/Linux, saliendo",
		"Este script sólo permite ejecutarse en Oracle Linux",
		"Este script sólo se ejecuta en procesadores de aarch64",
		"Este script sólo se ejecuta en Raspberry Pi 4",
		"DNF no está disponible, ¿este sistema no es Oracle Linux?, instala Oracle Linux 8",
		"No tienes conexión a internet, por favor revisa e inténtalo de nuevo",
		"Actualizando repositorios de Oracle Linux... Por favor, espere",
		"dialog no está disponible, instalando",
		"Todo ok!",
		"=============== PAQUETES BASE =============== \n",
		"=============== SERVICIO DE COCKPIT (IP:9090) =============== \n",
		"=============== AGREGAR UN USUARIO DE SUDO =============== \n",
		"Hemos creado un script llamado omz.sh en tu carpeta de home, después de reiniciar, usa chmod +x omz.sh",
		"Por favor reiniciar tu servidor para hacer los cambios",
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
		"Please write your hostname (ex: A036-oracle)",
		"America/Guayaquil is the timezone by default, if you want to change, here is the command\n\n timedatectl set-timezone REGION/CITY",
		"Choose your keyboard layout and locale",
		"Write your new user: ",
		"Graphical",
		"Install XFCE as Desktop Environment?",
		"Install Oracle Linux KVM Suite?",
		"More Sofware!!",
		"This script has a little pack of software, Do you like it?\n",
		"READY!!!, Your RPI4 is succesfully configured, if you have errors, please report at 036raspberry in GitHub"
	)

    DICTIONARY_ESP=(
		"Presione Enter para continuar...",
		"Por favor escriba su hostname (ex: A036-oracle)",
		"America/Guayaquil es el timezone por defecto, si quieres cambiarlo por algun otro, aqui esta la orden\n\n timedatectl set-timezone REGION/CITY",
		"Elige tu distribución de teclado y tu locale",
		"Escribe tu nuevo usuario: ",
		"Entorno Grafico",
		"¿Instalar XFCE como Entorno grafico?",
		"¿Instalar el Suite de Oracle KVM?",
		"Mas Sofware!!",
		"Este script tiene un pequeño pack de software, ¿Te gusta?",
		"LISTO!!!, Tu RPI4 fue configurado exitosamente, si tienes errores, repórtalo a 036raspberry",
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
    
    ORACLE: str = Popen(r"""cat /etc/os-release | head -n 1 | cut -d "=" -f2
                        """, shell=True, stdout=PIPE).stdout.read().decode('utf-8').replace("\n", "")
    
    PI: str = Popen(r"""cat /sys/firmware/devicetree/base/model
                    """, shell=True, stdout=PIPE).stdout.read().decode('utf-8').replace("\n", "")
    
    if version_info < (3, 5):
        utils.clear(); printer("error",14); exit(1)
    if platform != "linux":
        utils.clear(); printer("error",0); exit(1)
    if getuid() != 0:
        utils.clear(); printer("error",15); exit(1)
    if not search("\"Oracle.* ",ORACLE):
        utils.clear(); printer("error",1); exit(1)
    if machine() != "aarch64":
        utils.clear(); printer("error",2); exit(1)
    if not search("^Raspberry\sPi\s4.*",PI):
        utils.clear(); printer("error",3); exit(1)
    if not commandverify("dnf"):
        utils.clear(); printer("error",4); exit(1)
    try: urlopen('http://google.com')
    except: utils.clear(); printer("error",5); exit(1)
    
    printer("print",6)      
    system("dnf update --assumeyes &> /dev/null")
    
    if not commandverify("dialog"):
        printer("print",7)
        system("dnf install dialog --assumeyes &> /dev/null")
        
    printer("print",8)     
    
    spinner = utils.spinning()
    for _ in range(15):
        stdout.write(next(spinner))
        stdout.flush(); sleep(0.1)  
        stdout.write('\b')
    
def packages() -> None:
    
    utils.clear(); printer("print",8)
    system("dnf install rsync sudo nano git net-tools wget nano e2fsprogs \
		cockpit glibc-all-langpacks glibc-langpack-es zsh -y")
    print("=============== OK =============== \n")
    input(reader(0))
    
def hostnamer() -> None:
    
    response = d.inputbox(reader(1), 8, 80)
    if response[0] == "ok":
        system("hostnamectl set-hostname " + response[1])
    elif response[0] == "cancel": exit(0) 
    
def localer() -> None:
    
    choices = [("Spanish/Español","es"),("English","us")]
    d.msgbox(reader(2),9,50)
    system("timedatectl set-timezone America/Guayaquil")
    response = d.menu(reader(0), 15, 50, 4, choices)
    if response[0] == "ok" and response[1] == "Spanish/Español":
        system("localectl set-keymap es")
        system("localectl set-locale LANG=es_ES.UTF-8")
    elif response[0] == "ok" and response[1] == "English":
        system("localectl set-keymap us")
        system("localectl set-locale LANG=en_US.UTF-8")
    else: utils.clear(); exit(0)
    
def cockpit() -> None:
    
    utils.clear(); printer("print",10)
    system("systemctl enable --now cockpit.socket")
    system("systemctl start cockpit.socket")
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))
    
def newuser() -> None:
    
    global SUDOUSER
    utils.clear(); printer("print",11)
    SUDOUSER = input(reader(4))
    system(f"adduser {SUDOUSER}")
    system(f"passwd {SUDOUSER}")
    system(f"usermod -aG wheel {SUDOUSER}")
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))

def graphical() -> None:
    
    global XRDPTOGGLE
    
    if d.yesno(reader(6),7,60) == d.OK:
        XRDPTOGGLE=1; utils.clear()
        print("=============== EPEL & XFCE =============== \n")
        system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm --assumeyes")
        system("dnf update --assumeyes")
        system('dnf groupinstall "base-x" --assumeyes')
        system('dnf groupinstall "xfce" --assumeyes')
        system("dnf install xfce4-whiskermenu-plugin --assumeyes")
        system("touch /root/.xinitrc")
        with open(f"/root/.xinitrc", 'w') as f: f.write('xfce4-session')
        system(f"touch /home/{SUDOUSER}/.xinitrc")
        with open(f"/home/{SUDOUSER}/.xinitrc", 'w') as f: f.write('xfce4-session')
        print(" ")
        print("=============== OK =============== \n")
        input(reader(0))
    else:
        utils.clear()
        print("=============== EPEL =============== \n")
        system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm --assumeyes")
        print(" ")
        print("=============== OK =============== \n")
        input(reader(0))

def remote() -> None:
    
    global XRDPTOGGLE

    utils.clear()
    if XRDPTOGGLE == 1:
        print("=============== XRDP ===============  \n")
        system('dnf install xrdp --assumeyes')
        system(f"touch /home/{SUDOUSER}/.Xclients")
        with open(f'/home/{SUDOUSER}/.Xclients', 'w') as f: f.write('xfce4-session')
        system(f'chmod a+x /home/{SUDOUSER}/.Xclients')
        system(f'chown {SUDOUSER} /home/{SUDOUSER}/.Xclients')
        system('systemctl enable xrdp')
        system('systemctl enable xrdp-sesman')
        system('chcon --type=bin_t /usr/sbin/xrdp')
        system('chcon --type=bin_t /usr/sbin/xrdp-sesman')
        print(" ")
        print("=============== OK =============== \n")
        input(reader(0))

def kvm() -> None:
    
    utils.clear()
    if d.yesno(reader(7),8,60) == d.OK:
        utils.clear()
        print("=============== KVM ===============  \n" )
        system('dnf module install virt -y')
        system('dnf install virt-install virt-viewer virt-manager cockpit-machines -y')
        system('virt-host-validate qemu')
        system('systemctl enable libvirtd')
        system('systemctl start libvirtd')
    else: utils.clear(); return

def ohmyzsh() -> None:
    
    utils.clear()
    print("=============== OMZ =============== \n" )
    system(f"touch /home/{SUDOUSER}/omz.sh")
    with open(f'/home/{SUDOUSER}/omz.sh', 'w') as f: 
        f.writelines([
            "#!/bin/bash\n",
            'sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"\n',
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
            'sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"\n',
            'sed -i -e \'s/ZSH_THEME=.*/ZSH_THEME=\\\"pmcgee\\\"/\' .zshrc\n',
            "sed -i -e '/^source $ZSH.*/i ZSH_DISABLE_COMPFIX=true' .zshrc\n",
            r"git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting",
            "\n",
            r"git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions",
            "\n",
            "sed -i -e 's/plugins=(.*/plugins=(git zsh-syntax-highlighting zsh-autosuggestions)/' .zshrc"
        ])
    
    system(f'chmod +x /root/omz.sh')
    printer("print",12)
    print(" ")
    print("=============== OK =============== \n")
    input(reader(0))

def software() -> None:
    
    utils.clear()
    if d.yesno(reader(10)+"""\n -> baobab \n -> ntfs-3g \n -> nautilus \n -> gedit \n -> tar \n -> yum-utils \n -> numix-gtk-theme \n -> numix-icon-theme \n -> numix-icon-theme-circle
            """ ,20,65) == d.OK:
        utils.clear()
        print("=============== SOFTWARE =============== \n")
        system('dnf install baobab ntfs-3g exfatprogs nautilus gedit tar yum-utils --assumeyes')
        system('dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm --assumeyes')
        system('dnf install numix-gtk-theme --assumeyes')
        system('dnf install http://mirror.centos.org/centos/7/os/x86_64/Packages/gnome-icon-theme-3.12.0-1.el7.noarch.rpm --assumeyes')
        system('dnf install numix-icon-theme --assumeyes')
        system('dnf install numix-icon-theme-circle --assumeyes')
        system('dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm --assumeyes')
        print(" ")
        print("=============== OK =============== \n")
        input(reader(0))
        
    else: utils.clear(); return

def finisher() -> None:
    
    utils.clear(); d.msgbox(reader(10),7,50)
    utils.clear(); printer("print", 13); exit(0)

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