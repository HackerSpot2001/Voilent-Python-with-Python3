import os
"""
If You Want to use other options of os.system function 
This Function Accept cmd command (or Powershell Commands)
if you want to show other option of shutdown use:-
shutdown
/s = shutdown
/r = restart
/t = timer in seconds (60second = 1minutes)
"""
shutdown = os.system("shutdown /s /t 60")