class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v
            results.append(current_max)
            if current_max == window.popleft():
                current_max = float('-inf')
        return results
        

'''
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
  if not nums:
    return nums
  
  result = []
  for i in range(len(nums) - k + 1):
    result.append(max(nums[i:i + k]))
  
  return result


import collections


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
  result = []
  window = collections.deque()
  current_max = float('-inf')
  for i, v in enumerate(nums):
    window.append(v)
    if i < k - 1:
      continue
    
    # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
    if current_max == float('-inf'):
      current_max = max(window)
    elif v > current_max:
      current_max = v
    result.append(current_max)
    
    # 최댓값이 윈도우에서 빠지면 최댓값을 초기화
    if current_max == window.popleft():
      current_max = float('-inf')
return result
'''
