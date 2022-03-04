from subprocess import call, PIPE, Popen
from sys import stdin, stdout, platform, version_info
from os import system
from urllib.request import urlopen
from termios import tcgetattr, tcsetattr, TCSADRAIN
from time import sleep
from tty import setcbreak
from dialog import Dialog

d = Dialog(dialog="dialog")
d.set_background_title("036 Creative Studios")

def main() -> None: 
    utils.clear(); language(); cover(); verify(); usbverify(); diskmenu()
    
def printer(type: str, position: int) -> None:
    
    GREEN = '\033[92m';  WARNING = '\033[93m'; FAIL = '\033[91m';  ENDC = '\033[0m'

    DICTIONARY_ENG=(
        "Your Operating System is not GNU/Linux, exiting",
		"This PC doesn't have internet connection, please check",
		"dialog is not available in this system, please install it",
		"parted is not available in this system, please install it",
		"wget is not available in this system, please install it",
		"bsdtar is not available in this system (libarchive), please install it",
		"All dependencies is ok!",
		"=============== NEW PARTITION TABLE TO SD CARD =============== \n",
		"=============== FORMAT/MOUNT ROOT AND BOOT FILESYSTEMS =============== \n",
		"=============== INSTALL ROOT AND BOOT FILESYSTEMS, PLEASE WAIT  =============== \n",
		"There's no USB drives connected in this PC, please connect your SD Card in a USB SD Card Reader",
        "Your Python versión is less than 3.5, exiting",
        "You are not superuser, please run as root"
	)

    DICTIONARY_ESP=(
        "Este sistema no es GNU/Linux, saliendo",
		"No tienes conexión a internet, por favor revisa e inténtalo de nuevo",
		"dialog no está disponible en tu sistema, por favor instálalo",
		"parted no está disponible en tu sistema, por favor instálalo",
		"wget no está disponible en tu sistema, por favor instálalo",
		"bsdtar no está disponible en tu sistema (libarchive), por favor instálalo",
		"Todo ok!",
		"=============== NUEVA TABLA DE PARTICIÓN EN LA TARJETA SD =============== \n",
		"=============== FORMATEAR Y MONTAR LOS SISTEMAS DE RAIZ Y ARRANQUE =============== \n",
		"=============== INSTALAR LOS SISTEMAS DE RAÍZ Y ARRANQUE, POR FAVOR ESPERE  =============== \n",
		"No hay USBs conectados en tu PC, por favor conecta tu tarjeta SD en un lector USB",
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
        "ATTENTION!!! Your SD card would be listed as a USB device, ensure that your SD is empty and ready for format",
		"Format a Device",
		"Choose a device",
		"DANGER ZONE!!!",
		"This device will be format Continue? \n",
		"Press Enter to continue...",
		"At the superuser home directory, we put a configurer script if you want",
		"READY!!!, Your SD was installed with Arch Linux ARM for Raspberry Pi 4, login as root/root, if you have errors, please report at 036raspberry in GitHub"
	)

    DICTIONARY_ESP=(
        "ATENCIÓN!!! Tu tarjeta SD debe ser mostrado como un dispositivo USB, verifica que tu SD está vacía y lista para formatear",
		"Tarjeta SD",
		"Elige un dispositivo para formatear",
		"Este dispositivo se va a formatear ¿Continuar? \n",
		"Presione Enter para continuar...",
		"En la carpeta home de root está disponible el script de configuración, si lo deseas",
		"LISTO!!!, Tu SD fue instalada con Arch Linux ARM para la Raspberry Pi 4, inicia sesión como root/root, si tienes errores, repórtalo a 036raspberry"
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

def usbverify() -> None:
    VERIFYUSB: str = Popen(r"""find /dev/disk/by-id/ -name 'usb*' | sort -n | sed 's/^\/dev\/disk\/by-id\///
                    """, shell=True, stdout=PIPE).stdout.read().decode('utf-8').replace("\n", "")
    if(VERIFYUSB == ""): utils.clear(); printer("error",10); exit(1)

def verify() -> None:
    if version_info < (3, 5):
        utils.clear(); printer("error",11); exit(1)
    if platform != "linux":
        utils.clear(); printer("error",0); exit(1)
    try: urlopen('http://google.com')
    except: utils.clear(); printer("error",1); exit(1)
    if not commandverify("dialog"):
        utils.clear(); printer("error",2); exit(1)
    if not commandverify("parted"):
        utils.clear(); printer("error",3); exit(1)    
    if not commandverify("wget"):
        utils.clear(); printer("error",4); exit(1)            
    if not commandverify("bsdtar"):
        utils.clear(); printer("error",5); exit(1)     
        
    printer("print",6)       
                
    spinner = utils.spinning()
    for _ in range(15):
        stdout.write(next(spinner))
        stdout.flush(); sleep(0.1)  
        stdout.write('\b')

def diskmenu() -> None:  

    utils.clear(); usbverify()
    d.msgbox(reader(0),7,70)
    DIRTYDEVS: list = []; BLOCK: list = []
    COUNT: int = 0; MODEL: int = 0; BLOCKCOUNT: int = 0
    DEVICE: int = 0; ARGSUSB: list = []

    USB = Popen(r"""find /dev/disk/by-id/ -name 'usb*' | sort -n | sed 's/^\/dev\/disk\/by-id\///'
                    """, shell=True, stdout=PIPE).stdout.read().decode('utf-8').rstrip().split('\n')
    
    for DEVICE in USB:
        DIRTYDEVS.append(Popen(f'readlink "/dev/disk/by-id/{DEVICE}"', shell=True, 
                            stdout=PIPE).stdout.read().decode('utf-8').rstrip().split("\n")[0])
        
    DIRTYDEVS = list(filter(('').__ne__, DIRTYDEVS))
    for DEV in DIRTYDEVS:
        ABSOLUTEPARTS = Popen(f"""
                            echo {DEV} | sed 's/^\.\.\/\.\.\//\/dev\//' | sed '/.*sd[[:alpha:]]$/d'""", 
                            shell=True, stdout=PIPE).stdout.read().decode('utf-8').rstrip()
        
        if ABSOLUTEPARTS == "":
            BLOCK.append(Popen(f"""
                                echo {DEV} | sed 's/^\.\.\/\.\.\///'""", 
                                shell=True, stdout=PIPE).stdout.read().decode('utf-8').rstrip().split("\n")[0])
            BLOCKCOUNT += 1
            
    for PART in BLOCK:
        DEVICE: str = f"/dev/{PART}"
        BLOCKSTAT = BLOCK[COUNT]
        MODEL: str = Popen(f'''
            cat /sys/class/block/{BLOCKSTAT}/device/model''',
            shell=True, stdout=PIPE).stdout.read().decode('utf-8').rstrip()
        SIZE: str = Popen(f"lsblk -no SIZE /dev/{PART} | head -1 | sed s/..//", 
                        shell=True, stdout=PIPE).stdout.read().decode('utf-8').rstrip()
        ARGSUSB.append([DEVICE, MODEL+ " " +SIZE]); COUNT += 1
        response = d.menu(reader(2), 15, 50, 4, ARGSUSB) 
        if(response[0] == "ok"): diskformat(response[1])
        
def diskformat(disk: str) -> None:
    if disk != "": utils.clear(); exit(0)
    if d.yesno(reader(4),7,60) == d.OK:
        printer("print",7)
        utils.live_tasker(f"parted --script {disk} mklabel msdos mkpart primary fat32 1MiB 200MiB set 1 boot on mkpart primary ext4 200MiB 100% print")
        print(" ")
        print("=============== OK =============== \n")
        input(reader(5)); utils.clear()
        
        printer("print",8)
        utils.live_tasker(f"mkfs.ext4 {disk}2")
        utils.live_tasker(f"mkfs.fat -F32 {disk}1")
        call("mkdir /mnt/boot",shell=True); call("mkdir /mnt/root",shell=True)
        call(f"mount {disk}2 /mnt/root",shell=True); call(f"mount {disk}1 /mnt/boot",shell=True)
        print(" ")
        print("=============== OK =============== \n")
        input(reader(5)); utils.clear(); baseinstall()
    else: utils.clear(); exit(1)
    
def baseinstall() -> None:
    printer("print",8)
    utils.live_tasker("wget http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-aarch64-latest.tar.gz -P /mnt/root/")
    call("bsdtar -xpf /mnt/root/ArchLinuxARM-rpi-aarch64-latest.tar.gz -C /mnt/root/")
    call("sync"); call("rm /mnt/root/ArchLinuxARM-rpi-aarch64-latest.tar.gz")
    call("mv /mnt/root/boot/* /mnt/boot/")
    call("sed -i 's/mmcblk0/mmcblk1/g' /mnt/root/etc/fstab")
    call("sed -i 's/^#PermitRootLogin\s.*$/PermitRootLogin Yes/' /mnt/root/etc/ssh/sshd_config &> /dev/null")
    utils.live_tasker("wget https://raw.githubusercontent.com/victor7w7r/036raspberry/master/archrpi4-config -P /mnt/root/root/")
    call("chmod +x /mnt/root/root/archrpi4-config"); call("umount /mnt/boot"); call("umount /mnt/root")
    call("rm -rf /mnt/boot"); call("rm -rf /mnt/root")
    
    print(" ")
    print("=============== OK =============== \n")
    input(reader(5)); utils.clear(); finisher()
    
def finisher() -> None:
    utils.clear(); d.msgbox(reader(6),8,50)
    d.msgbox(reader(6),10,50)
    utils.clear(); exit(0)
    
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
    
    def live_tasker(cmd: str) -> int:
        task = Popen(cmd, stdout=PIPE, stderr=PIPE, encoding='utf8', shell=True)
        try:  
            while task.poll() is None:
                for line in task.stdout:
                    task.stdout.flush()
                    print(line.replace("\n", ""))
            return task.poll()
        except: return 1
    
    def spinning():
        while True:
            for cursor in '|/-\\':
                yield cursor

if __name__ == "__main__":
    main()