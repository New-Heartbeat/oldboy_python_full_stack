
# 算法：高效解决问题的办法
# 算法之二分法

# 需求：有一个按照从小到大顺序排列的数字列表
#       需要从该数字列表中找到我们想要的那一个数字
#       如何更高效？？


nums = [-3, 4, 7, 10, 13, 21, 43, 77, 89]
find_num = 13

# 方案一：整体遍历效率太低
# for num in nums:
#     if num == find_num:
#         print('find it')
#         break

# 方案二：二分法
def binary_search(find_num, l):
    print(l)
    if len(l) == 0:
        print('找到的值不存在')
        return
    mid_index = len(l) // 2
    mid_num = l[mid_index]
    if find_num > mid_num:
        new_l = l[mid_index+1:]
        binary_search(find_num, new_l)
    elif find_num < mid_num:
        new_l = l[:mid_index]
        binary_search(find_num, new_l)
    else:
        print('find it')
binary_search(258, nums)
