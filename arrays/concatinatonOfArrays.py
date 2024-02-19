def getConcatenation(nums: list[int],noOfConcatination:int) -> list[int]:
    result=[]
    for x in range(noOfConcatination):
        for num in nums:
            result.append(num)
    return result
    
if __name__ == '__main__':
    print(getConcatenation(nums=[1,2,3]))