# #要求一:使用迴圈計算最小值到最大值之間，所有整數的總和
def calculate(min, max):
    sum=0
    for i in range(min, max+1):
        sum+=i
    print(sum)
calculate(1, 3)
calculate(4, 8)

# #要求二:計算出員工的平均薪資，請考慮員工數量會變動的情況
def avg(data):
    sum=0
    for i in range(data["count"]):
        sum+=data["employees"][i]["salary"]
    result=sum/data["count"]
    print(result)
avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000},
        {
            "name": "Bob",
            "salary": 60000},
        {
            "name": "Jenny",
            "salary": 50000}
    ]
    })
#要求三:找出至少包含兩筆整數陣列中，兩兩數字相乘後的最大值
def maxProduct(nums):
    max=nums[0]*nums[1]
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if(nums[i]*nums[j]>=max):
                max=nums[i]*nums[j]
            else:max
    print(max)
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
#要求四：印出陣列哪兩個索引內的整數相加會等於目標數字
def twoSum(nums, target):
    arr=[0,1]
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                arr=[i,j]
                break
            else:continue
    return arr
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
