"""
re 功能扩展
"""
import re

s = """Hello
北京
"""
# s = "JKkghKHLLHlHL, : !@#$%^&*((就算了键盘啦, \n为副书记哦你发个"

result = re.findall("\w+", s)
print(result)

# 只能匹配ascii字符
result = re.findall(r"\w+", s, flags=re.A)
print(result)

# 不区分大小写
result = re.findall(r"[a-z]+", s, flags=re.I)
print(result)

# 让 . 匹配换行
result = re.findall(r".+", s)
print(result)

result = re.findall(r".+", s, flags=re.S)
print(result)

# 让 ^ 和 $ 匹配每行的开头结尾位置
result = re.findall(r"^\w+", s)
print(result)

result = re.findall(r"^\w+", s, flags=re.M)
print(result)