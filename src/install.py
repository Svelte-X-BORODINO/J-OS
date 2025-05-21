import argparse
import os
import random
import time
from typing import Dict, Any, List
from colorama import Fore, init

# Инициализация colorama
init(autoreset=True)

# Глобальные переменные
users = []  # Список пользователей
current_user = "root"  # Текущий пользователь

# Полный список процессов (дописанный)
processes = [
    "sysj_init", "kthreadd", "ksoftirqd", "rcu_gp", "rcu_par_gp",
    "kworker", "migration", "cpuhp", "kdevtmpfs", "netns",
    "khungtaskd", "oom_reaper", "writeback", "kcompactd", "kswapd",
    "sysj_init-journald", "sysj_init-udevd", "sysj_init-networkd",
    "sysj_init-resolved", "sysj_init-timesyncd", "dbus-daemon",
    "sysj_init-logind", "polkitd", "accounts-daemon", "udisksd",
    "upowerd", "sysj_init-userdbd", "sysj_init-coredump",
    "sysj_init-oomd", "avahi-daemon", "cupsd", "bluetoothd",
    "geoclue", "ModemManager", "NetworkManager", "gdm", "gnome-shell",
    "Xorg", "xfce4-session", "xfwm4", "xfdesktop", "xfce4-panel",
    "gnome-terminal", "xfce4-terminal", "nautilus", "thunar",
    "gnome-software", "gnome-keyring", "gvfsd", "tracker-miner",
    "evolution-alarm", "gsd-keyboard", "gsd-power", "gsd-print-notifications",
    "gsd-color", "gsd-media-keys", "xdg-desktop-portal", "xdg-document-portal",
    "xdg-permission-store", "pipewire", "pulseaudio", "gnome-shell-calendar-server",
    "firefox", "chromium", "discord", "telegram", "spotify", "steam",
    "vlc", "code", "thunderbird", "dropbox", "syncthing", "nextcloud",
    "keepassxc", "qbittorrent", "transmission-daemon", "openvpn",
    "wireguard", "timeshift", "deja-dup", "redshift", "conky",
    "variety", "flameshot", "cron", "sysj_init-timers", "syslog-ng",
    "fwupd", "thermald", "irqbalance", "lm_sensors", "smartd",
    "ntpd", "sshd", "cups-browsed", "samba", "nmbd", "winbindd",
    "docker", "containerd", "libvirtd", "virtlogd", "vmtoolsd",
    "packagekitd", "flatpak-session-helper", "kworker-u", "iprt-VBox",
    "nvidia-persistenced", "acpid"
]


def grubinstall() -> None:
    """Установка GRUB"""
    print("Resolving dependencies... ")
    time.sleep(0.05)
    print(r"""
        To install:
        pygrub-1.0.6-package.kernel
    """)
    print("Checking database...")
    time.sleep(0.07)
    print("Updating cache...")
    time.sleep(1)
    print("Finished.")


def disk_parting(args: Dict[str, Any]) -> None:
    """Функция для работы с дисками"""
    print("\nPartitioning configuration:")
    print(f"• Mountpoint: {args.get('mountpoint', 'Not specified')}")
    print(f"• Filesystem: {args.get('filesystem', 'ext4')}")
    print(f"• Mode: {'Automatic' if args.get('auto') else 'Manual'}")
    if args.get('all'):
        print("• Scope: All disks")
    print("\nPartitioning completed successfully!")


def handle_parted_command(user_input: str) -> None:
    """Обработчик команды parted"""
    try:
        parser = argparse.ArgumentParser(prog='parted', add_help=False)
        parser.add_argument('-mp', '--mountpoint', help='Set mountpoint')
        parser.add_argument('-fs', '--filesystem',
                            choices=['jfs', 'btrfs', 'ext4'],
                            default='ext4',
                            help='Filesystem type')
        parser.add_argument('--all', action='store_true', help='Use all disks')
        parser.add_argument('--auto', action='store_true', help='Auto mode')

        args = parser.parse_args(user_input.split()[1:])

        if args.all and not args.auto:
            print("Error: --all requires --auto")
            return

        disk_parting(vars(args))

    except SystemExit:
        print("\nUsage: parted --auto --all -mp / -fs [jfs|btrfs|ext4]")


def user_add(username: str) -> None:
    """Добавление нового пользователя"""
    global users

    if not username:
        print("Error: Username required")
        return

    if username in users:
        print(f"Error: User '{username}' already exists")
        return

    users.append(username)
    print(f"User '{username}' created successfully")
    print(f"Current users: {', '.join(users)}")


def su_command(username: str) -> None:
    """Команда переключения пользователя"""
    global current_user

    if username == current_user:
        print(f"Already logged in as {username}")
        return

    if username not in users:
        print(f"su: user {username} does not exist")
        return

    password = input(f"Password for {username}: ")
    # В реальной системе здесь должна быть проверка пароля
    current_user = username
    print(f"Switched to user {username}")


def init_sys() -> None:
    """Инициализация системы"""
    print("Booting JKernel.. ok. Starting SYS_Init() ...")
    time.sleep(3)
    print("Stage: [Initializing SysJ_PROC] ...")
    time.sleep(2)
    print("RAM OK")
    time.sleep(0.3)
    print("CPU OK")
    time.sleep(0.3)
    print("VIDEO OK")
    time.sleep(1)
    print("Stage: [init_system]")
    time.sleep(5)
    print("Stage: [initializing JFS]")
    time.sleep(6)
    print(Fore.CYAN + "Welcome to the " + Fore.GREEN + "J OS 1.0!")
    time.sleep(2)

    for process in processes:
        choice = random.choice(["Initializing", "Starting"])
        print(f"{choice} {process}")
        time.sleep(0.05)

    time.sleep(5)
    print("Checking Network ...")
    time.sleep(0.7)
    print("ok.")
    print("Checking FS ...")
    time.sleep(0.7)
    print("ok.")
    print("Checking AHCI ...")
    time.sleep(0.7)
    print("ok.")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Starting JShell ...")


def main_shell():
    """Основной цикл командной оболочки"""
    while True:
        try:
            user_input = input(f"({current_user})%root $ ").strip()
            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0]
            args = parts[1:] if len(parts) > 1 else []

            if command == 'grub-install':
                if not args:
                    print("Installing GRUB to default device...")
                    grubinstall()
                elif args[0].startswith('/dev/'):
                    print(f"Installing GRUB to {args[0]}...")
                    grubinstall()
                else:
                    print("Invalid device format. Use: grub-install /dev/sdX")

            elif command == 'parted':
                handle_parted_command(user_input)

            elif command == 'useradd':
                if len(args) < 1:
                    print("Usage: useradd <username>")
                else:
                    user_add(args[0])

            elif command == 'su':
                if len(args) < 1:
                    print("Usage: su <username>")
                else:
                    su_command(args[0])

            elif command == 'poweroff':
                exit()

            elif command == 'help':
                print("""
Available commands:
    grub-install [device] - Installs bootloader
    parted - Disk partitioning tool
    useradd <username> - Create new user
    su <username> - Switch user
    poweroff - Shutdown system
    help - Show this help
""")
            else:
                print("Invalid command or arguments.")

        except KeyboardInterrupt:
            print("\nUse 'poweroff' to shutdown")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == '__main__':
    init_sys()
    main_shell()