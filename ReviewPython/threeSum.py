"""给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
"""
class Solution:

    def threeSum(self,nums):

        # 排序，使列表从小到大排列
        for i in nums:
            min_num = 0
            if i < min_num:
                pass
        j = 1
        temp = []
        if nums == [] or nums == [0]:
            print('[]')
        else:
            for i in nums:
                for j in range(len(nums)-1):
                    # print(j)
                    if i+nums[j]+nums[j+1] == 0 & j<len(nums):
                        temp.append([i,nums[j],nums[j+1]])
            print("结果：",temp)


s = Solution()
s.threeSum([0,0,0,0,0,0])
# s.threeSum([])
