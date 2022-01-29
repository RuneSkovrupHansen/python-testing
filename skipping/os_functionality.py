import sys
import distro

def do_stuff_windows() -> bool:
    return sys.platform == "windows"

def do_stuff_linux() -> bool:
    return sys.platform == "linux"

def do_stuff_ubuntu() -> bool:
    return distro.name() == "Ubuntu"

def do_stuff_debian() -> bool:
    return distro.name() == "Debian GNU/Linux"

def do_stuff_deprecated() -> bool:
    # Do some stuff, deprecated so should no longer be used
    return True

def main():
    pass

if __name__ == "__main__":
    main()