def majorityElements(arr):
    count1 = 0
    count2 = 0
    ele1 = None
    ele2 = None
    for i in range(len(arr)):
        if (ele1 == None or count1 == 0) and arr[i] != ele2:
            ele1 = arr[i]
            count1 = 1
        elif (ele2 == None or count2 == 0) and arr[i] != ele1:
            ele2 = arr[i]
            count2 = 1
        elif arr[i] == ele1:
            count1 += 1
        elif arr[i] == ele2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    count1 = 0
    count2 = 0
    res = []
    for i in range(len(arr)):
        if arr[i] == ele1:
            count1 += 1
        elif arr[i] == ele2:
            count2 += 1
    mini = (len(arr) // 3) + 1
    print(ele1, ele2)
    if count1 >= mini:
        res.append(ele1)
    if count2 >= mini:
        res.append(ele2)
    return res
    

print(majorityElements([11, 33, 33, 11, 33, 11]))