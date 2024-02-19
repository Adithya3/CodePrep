def twoSum(nums: list[int], target: int) -> list[int]:
    indexes=[]
    complimentValues ={}
    for num in nums:
        complimentValues[num] = target-num
    for num in nums:
        indexes=[]
        if complimentValues[num] in nums:
            indexes.append(nums.index(num))
            indexes.append(nums.index(complimentValues[num]))
        if indexes[0] != indexes[1]:
            return indexes
    return indexes

if __name__ == '__main__':
    print(twoSum([3,2,4],6))