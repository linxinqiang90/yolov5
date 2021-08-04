# coding=gbk
f=open("test.txt","w+",encoding="gbk")

with open('no.txt', 'r',encoding="gbk") as file_to_read:
  while True:
    lines = file_to_read.readline()
    if not lines:
      break
    f.writelines(lines+"\n")
f.close()

