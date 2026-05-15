class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {number: index for index, number in enumerate(nums)}
        print(hashmap)
        for index, item in enumerate(nums):
            remaining = target - item
            if remaining in hashmap and index != hashmap[remaining]:
                return [index, hashmap[remaining]]