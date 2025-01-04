# -*- coding: utf-8 -*-
def newDic(name, phone, birth, sex, score):
    return {"name":name, "phone":phone, "birth":birth, "sex":sex, "score":score}

def getStr(name, phone, birth, sex, score):
    return name + "\t" + phone + "\t" + birth + "\t" + sex + "\t" + score

rows=[]
rows.append(newDic("reakwon", "010-1234-1234", "1981-01-01", "M", "100"))
rows.append(newDic("sim", "010-4321-4321", "1999-09-09", "F", "88"))
rows.append(newDic("nara", "010-1010-2020", "1993-12-12", "M", "20"))
rows.append(newDic("yut", "010-2323-2323", "1988-10-10", "F", "59"))
rows.append(newDic("kim", "010-1234-4321", "1977-07-17", "M", "69"))
rows.append(newDic("nam", "010-4321-7890", "1996-06-20", "M", "75"))

filePath = "note.txt"
file = open(filePath, 'w')

file.write(getStr('name', 'phone', 'birth', 'sex', 'score') + '\r\n')

for i, dic in enumerate(rows, 1):
    file.write(getStr(dic['name'], dic['phone'], dic['birth'], dic['sex'], dic['score']) + '\r\n')

file.close()
