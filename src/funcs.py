from time import *
import random
from colorama import init, Fore, Style
import platform
import psutil # type: ignore
init(autoreset=True)

def stage(text):
    print(f'[ {text} ]')

def printl(text):
    print(f'[ LOG ] {text}')

def printk(text):
    a = random.randint(1, 1000)
    b = random.randint(728, 10000)
    print(f'[ {a}.{b} ] {text}')

from colorama import Fore, Style

from colorama import Fore, Style

def printok(*args):
    # Собираем весь текст в одну строку
    full_text = ' '.join(str(arg) for arg in args)
    
    # Разделяем на первое слово и остальной текст
    first_space = full_text.find(' ')
    if first_space == -1:  # Если только одно слово
        first_word, rest = full_text, ''
    else:
        first_word = full_text[:first_space]
        rest = full_text[first_space:]
    
    # Формируем цветной вывод
    ok_part = f"[ {Fore.GREEN}OK{Style.RESET_ALL} ]"
    first_word_part = f"{Fore.LIGHTBLACK_EX}{first_word}{Style.RESET_ALL}"
    
    print(f"{ok_part} {first_word_part}{rest}")



def run():
    ram = psutil.virtual_memory()

    print("Uncompressing jkernel ... ok. Booting system ...")
    sleep(4)
    stage('Checking Components')
    sleep(0.4)
    printl(f'CPU: {platform.processor()}')
    printl(f'RAM: {ram.total // (1024 ** 3)} GB')
    sleep(2)
    processes = [
    "sysj-init",
    "sysj-init-journald",
    "sysj-init-udevd",
    "dbus-daemon",
    "NetworkManager",
    "dhcpcd",
    "wpa_supplicant",
    "sysj-init-networkd",
    "sysj-init-resolved",
    "agetty",
    "login",
    "bash",
    "sh",
    "zsh",
    "fish",
    "sshd",
    "gdm",
    "lightdm",
    "sddm",
    "Xorg",
    "wayland",
    "sway",
    "i3",
    "plasma",
    "gnome-shell",
    "xfce4-session",
    "mate-session",
    "cinnamon-session",
    "budgie-panel",
    "lxqt-session",
    "openbox",
    "bspwm",
    "dwm",
    "awesome",
    "polybar",
    "conky",
    "picom",
    "redshift",
    "pulseaudio",
    "pipewire",
    "wireplumber",
    "alsa",
    "jackd",
    "bluetoothd",
    "cupsd",
    "avahi-daemon",
    "chronyd",
    "ntpd",
    "systemd-timesyncd",
    "crond",
    "atd",
    "syslog-ng",
    "rsyslogd",
    "journalctl",
    "udisksd",
    "upowerd",
    "polkitd",
    "accounts-daemon",
    "geoclue",
    "modemmanager",
    "thermald",
    "tlp",
    "fwupd",
    "gvfsd",
    "udisks2",
    "colord",
    "rtkit-daemon",
    "systemd-logind",
    "elogind",
    "acpid",
    "lm_sensors",
    "smartd",
    "cron",
    "anacron",
    "sysj-init-user-sessions",
    "sysj-init-machined",
    "sysj-init-nspawn",
    "sysj-init-homed",
    "sysj-init-sysctl",
    "sysj-init-modules-load",
    "sysj-init-random-seed",
    "sys-backlight",
    "sysj-init-rfkill",
    "sysj-init-localed",
    "sysj-init-timedated",
    "sysj-init-hostnamed",
    "sysj-init-userdbd",
    "sysj-init-pstore",
    "sysj-init-boot-check-no-failures",
    "sysj-init-coredump",
    "sysj-init-notify",
    "sysj-init-ask-password",
    "sysj-init-repart",
    "sysj-init-sysext",
    "sysj-init-stub",
    "sysj-init-sleep",
    "sysj-init-shutdown",
    "kworker",
    "ksoftirqd",
    "migration",
    "rcu_sched",
    "watchdogd",
    "irqbalance",
    "haveged",
    "rngd",
    "tpm2d",
    "fprintd",
    "bolt"
    ]
    for process in processes:
        choice = random.choice(["Initializing", "Starting"])
        printok(f"{choice} {process}")
        sleep(0.05)
    
