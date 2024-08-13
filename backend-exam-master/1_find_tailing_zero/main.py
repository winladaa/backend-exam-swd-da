"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int):
        if number < 0:
            return 'number can not be negative'

        count = 0
        i = 5 # because basically 5 can determine the number of tailing zeros for example 5*2 = 10, 5*20 = 100
        while number // i >= 1:
            count += number // i
            i *= 5

        return count

solution = Solution()

input_1 = 7 # 5040
output_1 = solution.find_tailing_zeroes(input_1) # 1
print(f'Input: {input_1}\nOutput: {output_1}')

input_2 = -10
output_2 = solution.find_tailing_zeroes(input_2)
print(f'Input: {input_2}\nOutput: {output_2}')

input_3 = 2 # 2
output_3 = solution.find_tailing_zeroes(input_3) # 0
print(f'Input: {input_3}\nOutput: {output_3}')

input_4 = 5 # 120
output_4 = solution.find_tailing_zeroes(input_4) # 1
print(f'Input: {input_4}\nOutput: {output_4}')

input_5 = 10 # 3628800
output_5 = solution.find_tailing_zeroes(input_5) # 2
print(f'Input: {input_5}\nOutput: {output_5}')