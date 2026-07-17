#TwoSumSolution in Python w/ comments

#Give below solve for solution
#class Solution:
   # def twoSum(self, nums: List[int], target: int) -> List[int]:
        


#Inital Brutforce Solution
class Solution: #given
    def twoSum(self, nums: List[int], target: int) -> List[int]: #given
        for i in range(len(nums)): #checks the indicies i is in the array nums 
        #example of the i could be indicie 0 in the array [7,94,204,23]
        #where i = 0 and the 
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []