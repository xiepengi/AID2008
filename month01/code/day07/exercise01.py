"""
    在终端中打印如下图形
"""
# for i in range(1, 5):
#     print("*" * i)
for r in range(4):
    for c in range(r + 1):
        print("*", end="")
    print()
