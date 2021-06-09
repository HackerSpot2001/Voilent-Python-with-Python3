#! /usr/bin/python3
import ftplib

def AnonFTPLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login("root","owaspbwa")
        print("[{}] Anonymous FTP Login Succeeded".format(hostname))
        ftp.quit()
        return True
    except Exception as e:
        print(e)
        print("{} Anonymous FTP Login Failed".format(hostname))
        return False


if __name__ == "__main__":
    host = "192.168.0.112"
    AnonFTPLogin(host)