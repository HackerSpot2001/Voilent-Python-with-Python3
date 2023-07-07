from requests import get
from threading import Thread , ThreadError
from time import sleep


def make_req(url):
    """Helps to make Get Request."""
    try:
        res = get(url)
        if (res.status_code != 404):
            print("[+]sending url: {}  code: {} ".format(url,res.status_code))


    except KeyboardInterrupt:
        print("Going to die...")
        exit(0)


    except Exception as e:
        print("[!] Failed to make request with url: {}\n Error: {}".format(url,e))



url = "http://dvwa/"
dir_path = "WordLists-20111129/Filenames_or_Directories_All.wordlist"
fh = open(dir_path,"rb")
for line in fh.readlines():
    try:
        full_url = url + str(line.decode()).strip()
        th = Thread(target=make_req, args=(full_url,) )
        th.start() 

    except ThreadError:
        sleep(1)

    except Exception as e:
        print("Error: {}".format(e))


fh.close()