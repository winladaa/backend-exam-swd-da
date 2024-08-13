"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list):
        if not numbers:
            return 'list can not blank'
        
        maximum_i = 0
        maximum_v = numbers[0]

        for i in range(1, len(numbers)): # start with index 1
            if numbers[i] > maximum_v:
                maximum_i = i
                maximum_v = numbers[i]

        return maximum_i

solution = Solution()

input_1 = [1, 2, 1, 3, 5, 6, 4]
output_1 = solution.find_max_index(input_1)
print(f'Input: {input_1}\nOutput: {output_1}')

input_2 = []
output_2 = solution.find_max_index(input_2)
print(f'Input: {input_2}\nOutput: {output_2}')

input_3 = [4, 7, 2, 3]
output_3 = solution.find_max_index(input_3)
print(f'Input: {input_3}\nOutput: {output_3}')

input_4 = [9, 5, 1, 8, 12, 8]
output_4 = solution.find_max_index(input_4)
print(f'Input: {input_4}\nOutput: {output_4}')