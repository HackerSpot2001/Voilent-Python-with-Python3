#! /usr/bin/python3
import pexpect

# PROMPT = ['\$','>>>','> ','#',"root@owaspbwa #"]
# # user = "msfadmin"
# password = "owaspbwa"
# child = pexpect.spawn('ssh root@192.168.0.112')
# child.expect("password:")
# child.sendline(password)
# child.expect(PROMPT)
# child.sendline('cat /etc/shadow | grep root')
# print(child.before)
# print("after")
# print(child.after)
# child.sendline('cat /etc/shadow | grep root')


from pexpect import pxssh
s = pxssh.pxssh()
if not s.login ('192.168.0.112', 'root', 'owaspbwa'):
    print ("SSH session failed on login.")
    print( str(s))
else:
    print ("SSH session login successful")
    s.sendline ('cat /etc/shadow | grep root')
    s.prompt()         # match the prompt
    print (str(s.before))   # print everything before the prompt.
    s.logout()