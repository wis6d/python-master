import re

data = '''
40インチTV 98000円
ノートPC 113000円
スマホ 58700円
タブレット 49500円
'''

result = re.sub(r'(\d+)円', r'¥\1-', data)
print(result)