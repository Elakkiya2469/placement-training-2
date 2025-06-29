class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        i = 0  
        j = len(nums) - 1  

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] == target:
                return True

            if nums[i] <= nums[mid]:  
                if nums[i] <= target <= nums[mid]:
                    j = mid
                else:
                    i += 1
            else:  
                if nums[mid] <= target <= nums[j]:
                    i = mid
                else:
                    j -= 1

        return False

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r] or nums[mid] < nums[l]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[l] or nums[mid] > nums[r]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return False
