file = open('(3).txt', 'r')
data = file.read()
aa = data.split()
file.close()
#
file = open('(4).txt', 'w')
total = 0
for i in aa:
      total = total + int(i)

print(total)
file.write(str(total))
file.close()


#(3) 읽고 총합 구하고 저장
