"""
汇率转换器
"""
# 1. 获取数据 - 美元
usd = float(input("请输入美元："))

# 2. 逻辑计算 - 美元 × 6.8538
cny = usd * 6.8538

# 3. 显示结果 - xx美元=xx人民币
print(str(usd) + "美元=" + str(cny) + "人民币")
