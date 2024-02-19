# This can also be done using sorting. which might have a complexity less than o(n)
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

if __name__ == "__main__":
    print(containsDuplicate([1,2,3,4,5,1]))
