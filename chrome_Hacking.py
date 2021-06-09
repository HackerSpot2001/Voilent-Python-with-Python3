try:
    import os
    import sqlite3
    import shutil

except Exception as e:
    print("Import Error, Some modules not found",e)

"""
SQL Commands:- 
cursor.execute("pragma table_info('urls')")
cursor.execute("select name from sqlite_master where type='table'")
cursor.execute("pragma table_info('downloads')")
cursor.execute("pragma table_info('visits')")
cursor.execute("pragma table_info('keyword_search_terms')")
"""


def getChromeHistory():
    history_path = os.path.join(os.environ['USERPROFILE'],"AppData","Local","Google","Chrome","User Data","Default","History")
    dstPath = os.path.join(os.getcwd(),"chromeHistory")
    shutil.copyfile(history_path,dstPath)
    conn = sqlite3.connect(dstPath)
    cursor = conn.cursor()
    cursor.execute("select id,url,title,visit_count,typed_count,last_visit_time,hidden from urls order by id")
    for i in cursor.fetchall():
        print("="*100)
        print("Id:- ",i[0])
        print("URL:- ",i[1])
        print("Title:- ",i[2])
        print("Visit Count:- ",i[3])
        print("Typed Count:- ",i[4])
        print("Last Visit TImd:- ",i[5])
        print("Hidden:- ",i[6])

    cursor.close()
    conn.close()
    os.remove(dstPath)

def getDownloadsInfo():
    history_path = os.path.join(os.environ['USERPROFILE'],"AppData","Local","Google","Chrome","User Data","Default","History")
    dstPath = os.path.join(os.getcwd(),"chromeHistoryofDownloads")
    shutil.copyfile(history_path,dstPath)
    conn = sqlite3.connect(dstPath)
    cursor = conn.cursor()
    cursor.execute("pragma table_info('downloads')")
    cursor.execute("select id,guid,current_path,target_path,start_time,end_time,total_bytes,received_bytes,site_url,tab_url,by_ext_id,by_ext_name from downloads order by id")
    for i in cursor.fetchall():
        print("="*100)
        print("id:- ",i[0])
        print("guid:- ",i[1])
        print("current path:- ",i[2])
        print("target path:- ",i[3])
        print("start time:- ",i[4])
        print("end time:- ",i[5])
        print("total bytes:- ",i[6])
        print("recieved bytes:- ",i[7])
        print("site url:- ",i[8])
        print("tab url:- ",i[9])
        print("Ext id:- ",i[10])
        print("Ext name:- ",i[11])

    cursor.close()
    conn.close()
    os.remove(dstPath)

def getChromeMediaHistory():
    pass

def getChromeLoginData():
    pass

def getChromeCookies():
    pass

if __name__ == '__main__':
    pass