import re

data = '''
40インチTV 98000円
ノートPC 113000円
スマホ 58700円
タブレット 49500円
'''

res = re.findall(r'(\d+)円', data)

total = 0

for item in res:
  print(item)
  total += int(item)

print('total ' + str(total) + '円')