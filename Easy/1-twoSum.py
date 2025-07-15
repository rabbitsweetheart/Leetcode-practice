##20241126##


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i,j]

        return ans


###test###

n = Solution()  

nums = [3,2,4]
target = 6
print(n.twoSum(nums = nums, target = target))

nums = [3,3]
target = 6
print(n.twoSum(nums = nums, target = target))


'''
###Sample###

class Solution:

    def twoSum(self,nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in numSet:
                return [i,numSet[compliment]]
            else:
                numSet[nums[i]]=i
        return []  

'''