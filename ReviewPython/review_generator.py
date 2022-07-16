# import sys
#
#
# def fibonacci(n):
#     a,b,counter = 0,1,0
#     while True:
#         if (counter>n):
#             return
#         yield a
#         a,b = b, a + b
#         counter += 1
#
#
# f = fibonacci(5)  # f是个迭代器
#
# while True:
#     try:
#         print(next(f))
#     except StopIteration:
#         sys.exit()


def foo(num):
    print("starting...")
    while num < 10:
        num = num + 1
        yield num


for n in foo(0):
    print("打印：", n)
    # print(type(n))
