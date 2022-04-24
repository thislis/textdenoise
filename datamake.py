import random

import sys
sys.setrecursionlimit(10**9)

def cambridge(str):

    text = []

    if len(str) < 4:
        return str

    first = str[0]
    last = str[-1]
    middles = list(str[1:-1])
    random.shuffle(middles)
    middles = "".join(middles)

    for i in [first, middles, last]:
        text.append(i)

    text = "".join(text)

    if text == str:
        return cambridge(text)
    else:
        return text

def pandan(word):

    middles = word[1:-1]

    for i in range(len(middles)-1):
        if middles[i] == middles[i+1]:
            return False
        else:
            continue

    return True

with open('C:/Users/ckwon/OneDrive/문서/파이썬+끝말잇기/dict.txt', 'rt', encoding='UTF8') as data:
    datalist = data.readlines()

usedata = []
small = []
big = []

for word in datalist:
    usedata.append(word.replace("\n", ""))

for i in range(len(usedata)):
    if len(usedata[i]) <= 3:
        small.append(usedata[i])

for word in small:
    usedata.remove(word)

for i in range(len(usedata)):
    if len(usedata[i]) >= 6:
        big.append(usedata[i])

del usedata[:5]

for word in big:
    usedata.remove(word)

for i in range(len(usedata)):
    tof = pandan(usedata[i])
    if tof == False:
        usedata[i] = 0
    else:
        continue

remove_set = {0}

usedata = [i for i in usedata if i not in remove_set]

import pandas

df = pandas.DataFrame(usedata)
print(df)
df.to_excel("C:/Users/ckwon/OneDrive/문서/data.xlsx", sheet_name="sample1")
