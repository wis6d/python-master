f = open('data.txt', mode='w')
while(True):
  s = input('message:')
  if (s == ''):
    break;
  f.write(s + '\r\n')
f.close()
print('finished!')