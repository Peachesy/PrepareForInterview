"""
十大经典排序算法：
冒泡排序，选择排序，快速排序，归并排序，堆排序，插入排序，希尔排序，计数排序，捅排序，基数排序
以下均实现从小到大排序
"""

class Sort:

    # 冒泡排序
    def bubble_sort(self,num_list):
        n=len(num_list)
        for i in range(n):
            for j in range(1,n-i):
                if num_list[j-1] > num_list[j]:
                    # 或者这样写：
                    # num_list[j-1],num_list[j] = num_list[j],num_list[j-1]
                    temp = num_list[j]
                    num_list[j] = num_list[j-1]
                    num_list[j-1] = temp
            print(num_list)
        print("最终结果：",num_list)

    # 选择排序
    def selection_sort(self,num_list):
        n = len(num_list)
        for i in range(n-1):
            min_index = i
            for j in range(i+1,n):
                if num_list[j] < num_list[min_index]:
                    min_index = j
            # 当i不是最小数时，将i和最小数交换
            if i != min_index:
                num_list[i],num_list[min_index] = num_list[min_index],num_list[i]
            print(num_list)
        print("最后结果：", num_list)






solution = Sort()
solution.selection_sort([7,84,14,23,-7,15,8])


