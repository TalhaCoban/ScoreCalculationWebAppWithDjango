
def yuvarla(x):
    fark = x - int(x)
    if fark < 0.5:
        return int(x)
    else:
        return int(x) + 1

def ham2018(x,index,path):
    x = yuvarla(x)
    ham2018 = open(path + "\\YKSsiralama\\ham2018.txt")
    for i in ham2018.readlines():
        i = i.split(",")
        i[-1] = i[-1].split("/")[0]
        if int(x) == int(i[0]):
            sonuc = i[index]
            ham2018.close()
            return sonuc


def yer2018(x,index,path):
    x = yuvarla(x)
    yer2018 = open(path + "\\YKSsiralama\\yer2018.txt")
    for i in yer2018.readlines():
        i = i.split(",")
        i[-1] = i[-1].split("/")[0]
        if int(x) == int(i[0]):
            sonuc = i[index]
            yer2018.close()
            return sonuc

    

def ham2019(x,index,path):
    x = yuvarla(x)
    ham2019 = open(path + "\\YKSsiralama\\ham2019.txt")
    for i in ham2019.readlines():
        i = i.split(",")
        i[-1] = i[-1].split("/")[0]
        if int(x) == int(i[0]):
            sonuc = i[index]
            ham2019.close()
            return sonuc

    

def yer2019(x,index,path):
    x = yuvarla(x)
    yer2019 = open(path + "\\YKSsiralama\\yer2019.txt")
    for i in yer2019.readlines():
        i = i.split(",")
        i[-1] = i[-1].split("/")[0]
        if int(x) == int(i[0]):
            sonuc = i[index]
            yer2019.close()
            return sonuc
