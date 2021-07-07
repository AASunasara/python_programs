'''
9: Script to ping and check whether any given IPs are active, also whether given set of
software are installed in the existing system ( like java, kubectl, aws etc)
'''
import ipaddress, sys
from shutil import which


def check_ip():
    try:
        ip = input("Enter the ip address : \n")
        ipaddress.ip_address(ip)
        print(f"{ip} is a active/valid IP Address !")
    except Exception as e:
        print(e.__str__())

def check_software():
    softwares = input("Enter the name of software(java, python) etc. \nNote: multiple names should seperate by blank space (python java ruby).\n")
    for soft in softwares.split():
        exist = which(soft)
        if exist:
            print(f"{soft} installed at : {exist}.")
        else:
            print(f"{soft} not installed in the syatem.")


def main():
    while True:
        ans = input("'1' for : to check active/not active IP address ?\n'2' for : to check softwares installed in the system or not !\n'q' for quite!\n")
        if ans == '1' :
            check_ip()
            break
        elif ans == '2':
            check_software()
            break
        elif ans == 'q':
            sys.exit()

        else:
            print("Choose right option 1/2/q! \n")
            continue

if __name__ == "__main__":
    main()