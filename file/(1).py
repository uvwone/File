file = open('(1).txt', 'w')
for i in range(1, 101):
      str = file.write('{0}\n'.format(i))
file.close()
