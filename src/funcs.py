from time import *
import random
from colorama import init, Fore
import platform
import psutil
init(autoreset=True)

def stage(text):
    print(f'[ {text} ]')

def printl(text):
    print(f'[ LOG ] {text}')

def printk(text):
    a = random.randint(1, 1000)
    b = random.randint(728, 10000)
    print(f'[ {a}.{b} ] {text}')



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
    "systemd",
    "systemd-journald",
    "systemd-udevd",
    "dbus-daemon",
    "NetworkManager",
    "dhcpcd",
    "wpa_supplicant",
    "systemd-networkd",
    "systemd-resolved",
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
    "systemd-user-sessions",
    "systemd-machined",
    "systemd-nspawn",
    "systemd-homed",
    "systemd-sysctl",
    "systemd-modules-load",
    "systemd-random-seed",
    "systemd-backlight",
    "systemd-rfkill",
    "systemd-localed",
    "systemd-timedated",
    "systemd-hostnamed",
    "systemd-userdbd",
    "systemd-pstore",
    "systemd-boot-check-no-failures",
    "systemd-coredump",
    "systemd-notify",
    "systemd-ask-password",
    "systemd-repart",
    "systemd-sysext",
    "systemd-stub",
    "systemd-sleep",
    "systemd-shutdown",
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
        printk(f"{choice} {process}")
        sleep(0.05)
    
