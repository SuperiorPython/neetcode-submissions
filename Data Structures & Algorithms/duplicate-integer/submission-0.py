class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        same_list = []
        dupe = False
        for num in nums:
            if num not in same_list:
                same_list.append(num)
            else:
                dupe = True
                break
        return dupe