"""
1~9999数列中数字3出现的次数，用递推方法解出
"""

"""
思路
关键点：
1~9999范围，是不是涉及到大数问题；
递推方法
"""


class NumTimes:

    # 非递归的方式
    def times_of_num(self,num: list):
        count = 0
        for i in num:
            for j in str(i):
                # print(type(str(i)))
                if '3' in j:
                    count = count+1
        print(count)

    # 递归的方式
    def recursion_times_of_num(self,num:list):
        count = 0
        for i in num:
            self.recursion_times_of_num(i)
        print(count)


num_list = [100,103,1034,3333,4563,2345,3333,1,2,3,4,5,6,7,2,3,23,42,56,78,90,31,55,63,83,73,99]
# num_list = [4,7,3,53,73,33]
solution = NumTimes()
solution.recursion_times_of_num(num_list)


