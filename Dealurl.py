import  requests
import threading
import queue
import sys
import progressbar
import difflib

results = []
headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
bar = progressbar.ProgressBar(max_value=100)


q = queue.Queue()

progress_count = 0

urlcontent = []



def Seturl(res,url):
    for lists in urlcontent:
        co = difflib.SequenceMatcher(None,res[250:300], lists).quick_ratio()
        if  co > 0.8:
            return       
    urlcontent.append(res[250:300])
    print(1)
    print(urlcontent)
    results.append(url)
    print(3)


def progress_write():
    bar.update(progress_count / max_size * 100)

def dealwith():
    global progress_count
    while True:
        if not q.empty():
            url = q.get()
            progress_count = progress_count + 1
            #progress_write()
            try:
                res = requests.get(url,timeout=20,headers=headers).content
                Seturl(res,url)
                
            except:
                continue

        else:
            #bar.update(100)
            break

with open(sys.argv[1],"r") as f:
    for i in f.readlines():
        i = i.strip(" ").strip("\n")
        if "http" not in i:
            httpurl = "http://" + i
            q.put(httpurl)
            httpsurl = "https://" + i
            q.put(httpsurl)
        else:
            q.put(i.strip(" ").strip("\n"))

max_size = q.qsize()

l = []

for i in range(1,50):
    t = threading.Thread(target=dealwith)
    t.start()
    l.append(t)
for i in l:
    i.join()

with open(sys.argv[2],"at") as fw:
        for w in results:
            fw.write(w+"\n")