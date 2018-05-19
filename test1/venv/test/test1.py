import socket
socket.setdefaulttimeout(2)
s=socket.socket()
s.connect(("192.168.11.11",2121))
ans=s.recv(1024)
if ("Freefloat Ftp server(Version 1.00)" in ans):
    print("[+] Freefloat FTP Server is vulnerable")
elif    ("3Com 3CDaemon FTP Server Version 2.0" in banner):
    print ( "[+] 3CDaemon FTP Server is vulnerable.")

