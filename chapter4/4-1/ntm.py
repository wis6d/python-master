import re

data = '''
太郎 090-(999)-999 taro@yamada.san
花子 080-(888)-888 hanako@flower.shop
一郎 070-777-777 ichiro@happy.man
'''

result = re.findall(r'(\S+)\s+([\()\d-]+)\s+([\w.-_]+@[\w.-_]+)', data)

print('※名前')
for item in result:
  print(item[0])

print('\n※電話番号')
for item in result:
  print(item[1])

print('\n※メールアドレス')
for item in result:
  print(item[2])