f = open('data.txt', mode='r')
count = 0
for p in f:
  count += 1
  print( str(count) + ':' + p)
f.close()