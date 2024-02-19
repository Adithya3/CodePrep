def containsDuplicate(nums: list[int]) -> bool:
    returnBool = True;
    dictNums = {}
    for num in nums:
        if num in dictNums:
         dictNums[num] = dictNums[num] +1
        else:
            dictNums[num]=1
    for value in dictNums.values():
        if value>=2:
            returnBool = False
    return returnBool

def containsDuplicateOptimized(nums: list[int]) -> bool:
    dictNums = {}
    for num in nums:
         if num in dictNums:
             return True
         else:
            dictNums[num]=1
    return False

if __name__ == "__main__":
    print(containsDuplicateOptimized([1,2,3,4,5,1]))
