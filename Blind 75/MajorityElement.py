 #Majority Element - Leetcode question 169 - https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
    
        # Optimized Approach:
        # This solution uses the Boyer-Moore Voting Algorithm.
        # First, we initialize an element and a count. We iterate through the list,
        # updating the candidate element when the count reaches zero.
        # If the current number matches the candidate, we increase the count.
        # If it doesn't match, we decrease the count.
        # After the first pass, we verify if the candidate is indeed the majority element
        # by counting its occurrences in the array.

        element = None
        count = 0

        # First pass to find the candidate
        for num in nums:
            if count == 0:
                element = num
                count = 1
            elif num == element:
                count += 1
            else:
                count -= 1

        # Second pass to confirm the candidate/element
        count = 0
        for num in nums:
            if num == element:
                count += 1
            if count > len(nums) // 2:
                return element

        # If no majority element found, return -1
        return -1

# Time Complexity:
# The time complexity is O(n) since we traverse the list twice, resulting in linear time complexity.

# Space Complexity:
# The space complexity is O(1) as we only use a constant amount of extra space for the variables.
