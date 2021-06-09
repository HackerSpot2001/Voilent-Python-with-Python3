#!/usr/bin/python3
import os
import sqlite3
from platform import system,platform
from shutil import copytree


def get_history_from_google_chrome(file_path):
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    cursor.execute("SELECT * from urls")
    # This is for finding column names in table
    # names = list(map(lambda X:X[0], cursor.description))
    results = cursor.fetchall()
    print("System: {}\n".format(str(platform())))
    for (myid,url,title,visit_count,typed_count,last_visit_time,hidden) in results:
        print("[+] id: {}".format(myid))
        print("[+] URL: {}".format(url))
        print("[+] Title: {}".format(title))
        print("[+] Visit Count: {}".format(visit_count))
        print("[+] Typed Count: {}".format(typed_count))
        print("[+] Last visit time: {}".format(last_visit_time))
        print("[+] Hidden: {}\n".format(hidden))

    print("[*] {} Total History Founded in your Google Chrome Database".format(len(results)))




if __name__ == "__main__":
    login_name = os.getlogin()
    find_platform = system()

    if find_platform == 'Linux':
        print(find_platform)
        if os.path.exists("/home/{}/.config/google-chrome/Default/History".format(login_name)):
            try:
                os.mkdir("/home/{}/Google_Chrome_History")
            except:
                pass
            src_path = "/home/{}/.config/google-chrome/Default".format(login_name)
            dest_path = "/home/{}/Google_Chrome_History/Default".format(login_name)
            try:
                copytree(src_path,dest_path)
            except:
                pass

            file_path = f'{dest_path}/History'
            get_history_from_google_chrome(file_path)
    
    if find_platform == "Windows":
        pass