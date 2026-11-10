class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        #setting up 2 pointers left and right
        l, r = 0, len(numbers) - 1
        

        #[1,3,4,5,7,11]
        #will move to right if total of sum of l + r is smaller
        #will move to left if total of sum of l + r is bigger than the target
        while l < r:
            CurrentSum = numbers[l] + numbers[r]

            if CurrentSum > target:
                r -= 1
            elif CurrentSum < target:
                l += 1
            else:
                #we do l + 1 and r + 1 since index's are not starting from 0 they are starting from 1
                return [l + 1, r + 1]
         
        