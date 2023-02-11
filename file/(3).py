file = open('(3).txt', 'w')
for i in range(1, 101):
      if i % 2 == 1:
            str = file.write('{0}\n'.format(i))
file.close()
