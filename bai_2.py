import os

os.chdir('C:/word')
chdir = os.getcwd()
print(chdir)

#1
f = open('C:/word/abs2004.txt','r', encoding='utf-8')
f.read(4)

#2
l = open('C:/word/abs2004.txt','w', encoding='utf-8')
l.write('hello world')

#3
with open ('hung1.png','rb') as byte_reader:
    print(byte_reader.read(1))

#4
h = open('abs2004.txt', mode= 'r', encoding= utf-8)

#5
h.close()

#6
try:
    h = open('abs2004.txt', mode='r', encoding=utf - 8)
finally:
    h.close()

#7
with open('C:/word/abs2004.txt', mode='r',encoding='utf-8') as b:
    b.read(10)

#8,9
n = open('C:/word/hung1.docx',mode='r',encoding='utf-8')
v = n.read(10)
print(v)

#9
m = open('C:/word',mode='rw',encoding='utf-8')
print(m.write(hi))
print(m.read(4))
