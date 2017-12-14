
# coding: utf-8

# In[1]:

article = []
content = []


# In[2]:

def makeline(txt) :
    txt1 = txt.split("\n")
    while '' in txt1 :
        txt1.remove('')
    return txt1


# In[3]:

def ACchecker(line) :
    article.append(line[1])
    content.append(line[2:])


# In[5]:

def contentTokenizer(content) :
    contenttoken = []
    sym = "~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?"
    for x in range(len(content[0])) :
        new = content[0][x].lower()
        for s in sym :
            new = new.replace(s, " ")
        contenttoken.extend(new.split())
    return contenttoken


# In[6]:

def articleTokenizer(article) :
    articletoken = []
    sym = "~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?"
    for x in range(len(article)) :
        new = article[x].lower()
        for s in sym :
            new = new.replace(s, " ")
        articletoken.extend(new.split())
    return articletoken


# In[9]:

def getFrequpdown(li):
    "Takes a list as input, returns a dictionary of frequency count."
    di = {}
    for x in li:
        if x not in di: di[x] = 1
        else: di[x] += 1
    for x in sorted(di, key=di.get, reverse=True):
        print(x, di[x])


# In[10]:

def getFrequpdownwrite(li, name):
    di = {}
    for x in li:
        if x not in di: di[x] = 1
        else: di[x] += 1
    filename = name+".txt"
    f = open(filename, "w")
    for x in sorted(di, key=di.get, reverse=True):
        f.write(x + " " + str(di[x]) + ("\n"))
    f.close()


# In[8]:

def textanalyze(txt) :
    article = []
    content = []
    txt = makeline(txt)
    txt1 = ACchecker(txt)
    contenttoken = contentTokenizer(content)
    articletoken = articleTokenizer(article)
    


# In[ ]:

def textanalyze1(txt) :
    txt = makeline(txt)
    txt1 = ACchecker(txt)
    contenttoken = contentTokenizer(content)
    articletoken = articleTokenizer(article)
    


# In[ ]:

def makeline2(txt) :
    txt2 = []
    for x in range(len(txt)) :
        txt1 = txt[x].replace("\"", '').split("\n")
        while '' in txt1 :
            txt1.remove('')
        txt2.extend(txt1)
    return txt2


def fileopener() :
    file = input("How many files do you have?(only DIGITS work)")
    name = input("How file name made?")
    txtli = []
    for x in range(1, int(file)+1) :
        f = open(name+str(x)+".txt", "r")
        txt = f.read()
        f.close()
        txtli.append(txt)
    return txtli
