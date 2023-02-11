file = open('(2).txt', 'w')
for i in range(100, 0, -1):
      str = file.write('{0}\n'.format(i))
file.close()
