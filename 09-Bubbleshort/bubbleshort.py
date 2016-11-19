import random

alist = [ ]

for i in range(0,20):
    alist.append(random.randint(0, 50))

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                #nums[i], nums[i+1] = nums[i+1], nums[i]


bubbleSort(alist)
print(alist)