def search(self, nums: List[int], target: int) -> int:
  def binary_search(left, right):
    if left <= right:
      mid = left + (right - left) // 2
      
      if nums[mid] < target:
        return binary_search(mid + 1, right)
      elif nums[mid] > target:
        return binary_search(left, mid - 1)
      else:
        return mid
    else:
      return -1
    
  return binary_search(0, len(nums) - 1)

def search(self, nums: List[int], target: int) -> int:
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] < target:
      left = mid + 1
    elif nums[mid] > taregt:
      right = mid - 1
    else:
      return mid
  return -1

import bisect

def search(self, nums: List[int], target: int) -> int:
  index = bisect.bisect_left(nums, target)
  
  if index < len(nums) and nums[index] == target:
    return index
  else:
    return -1

def search(self, nums: List[int], target: int) -> int:
  try:
    return nums.index(target)
  except ValueError:
    return -1
