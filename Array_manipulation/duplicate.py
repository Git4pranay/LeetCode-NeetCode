Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
def containsDuplicate(nums):
    dup = ['p']*(max(nums)+1)
    # for i in range(nums):
    #     if i not in dup:
    #         dup +=[i]
    #     else:
    #         return 'false'
    # return 'true'
    for i in range(len(nums)):
        
        print(dup)
        if dup[nums[i]]!='p':
            return 'false'
        else:
            dup[nums[i]]=i    
        return 'true'
print(containsDuplicate([1,2,3,4]))