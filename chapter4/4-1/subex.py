import re

s = '''
One Little, two little, three little Indians
Four little, five LITTLE, six LiTTle Indians
Seven LittlE, eight little, nine LittLe Indians
Ten Little Indians.
'''

result = re.sub('little', 'BIG', s, flags=re.IGNORECASE)
print(result)