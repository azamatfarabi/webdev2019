
def first_last6(nums):
  
def same_first_last(nums):
  for i in range(len(nums)):
    if len(nums) >= 1 and nums[0] == nums[-1]:
      return True
      
  return False

def make_pi():
  n = math.pi
  nums = []
  nums.append(n)
  for i in range(len(nums)):
    return nums[0:2]

def common_end(a, b):
  for i in range(len(a)):
    for j in range(len(b)):
      if a[0] == b[0] or a[-1] == b[-1]:
        return True
        
  return False

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  for i in range(len(nums)):
    nums[0],nums[1] = nums[1],nums[2]
  
  return nums

def reverse3(nums):
  nums.reverse()
  return nums

  def max_end3(nums):
  for i in range(len(nums)):
    big = max(nums[0], nums[2])
    nums[0] = big
    nums[1] = big
    nums[2] = big
    return nums


    def sum2(nums):
  for i in range(len(nums)):
      return nums[i] + nums[i+1]
    

def middle_way(a, b):
  

def has23(nums):
  for i in range(len(nums)):
    if nums[i] == 2 or nums[i] == 3:
      return True
  
  return False
