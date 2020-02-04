import random

me = 0
you = 0
end_point = 20

while(True):
  input('--push enter or return--')
  rnd = random.randint(1, 7)
  you += rnd
  print('you:' + str(rnd) + ' total:' + str(you))
  if (you >= end_point):
    print('*** you win! ***')
    break
  rnd = random.randint(1, 7)
  me += rnd
  print('me:' + str(rnd) + ' total:' + str(me))
  if (me >= end_point):
    print('*** I win! ***')
    break
print('---end---')