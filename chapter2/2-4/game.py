stone = 30
min = 2
max = 4

print('交互に' + str(min) + '-' + str(max) + \
  '個の石を取っていき、最後の石を取った方が負けです')

def checkStone(player, stoneCount):
  if (stoneCount <= 0):
    if (player == 'you'):
      print('あなたの負けです')
    else:
      print('素晴らしい！あなたの勝ちです')
    return True
  else:
    return False

def getYou():
  global stone
  your = int(input('あなたは何個取りますか？'))

  if (your < min or your > max):
    print('それはダメ')
    return False
  stone -= your
  print('あなたは' + str(your) + '個取りました')
  return True

def getMe():
  global stone
  mine = (stone - min) % (min + max)
  if (mine < min):
    mine = min
  if (mine > max):
    mine = max
  
  print('私は' + str(mine) + '個取ります')
  stone -= mine

while(stone > 0):
  print(str(stone) + '個残っています')

  if (getYou() == False):
    continue

  if (checkStone('you', stone)):
    break

  print(str(stone) + '個残っています')

  getMe()

  if (checkStone('me', stone)):
    break

print('おしまい')