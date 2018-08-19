import socket
import sys

# Init

if "--debug" in sys.argv:
    debug = 1
else:
    debug = 0

service_list = [
    "20", "ftp (data transfer)",
    "21", "ftp (control)",
    "22", "ssh (secure shell)",
    "80", "http(s)",
    "118", "sql",
    "135", "Microsoft EPMAP",
    "443", "http(s)",
    "445", "Microsoft-DS Active Directory / Microsoft-DS SMB",
    "8080", "http(s)",
    "9418", "git",
    "19132", "Minecraft Bedrock Server",
    "25565", "Minecraft PC Server"
    ]

def getSandardService(port):
    if str(port) in service_list:
        if debug:
            print("standard service known")
        i = 0
        while i <= len(service_list):
            if debug:
                print("if "+str(port)+" == "+service_list[i])
            if str(port) == service_list[i]:
                if debug:
                    print("TRUE")
                return service_list[i + 1]
            else:
                if debug:
                    print("FALSE")
            i += 2
    else:
        return "Unknown"

def main():
    anti_error = 1
    while anti_error:
        try:
            ip = input("\nIP for scan : ")
            for port in range(1, 65535):
                if debug:
                    print("scan : "+str(port))
                conf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                co = conf.connect_ex((ip, port))
                conf.close()
                if co == 0:
                    print("[+] Port : {} | Standard : {}".format(port,getSandardService(port)))
            anti_error = 0
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    main()
