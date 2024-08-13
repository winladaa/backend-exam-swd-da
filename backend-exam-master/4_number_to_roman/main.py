"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int):
        if number < 0:
            return 'number can not less than 0'

        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
            50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

        ans = ''
        for value, symbol in roman.items():
            while number >= value:
                ans += symbol
                number -= value
        return ans

solution = Solution()

input_1 = 101
output_1 = solution.number_to_roman(input_1)
print(f'Input: {input_1}\nOutput: {output_1}')

input_2 = -1
output_2 = solution.number_to_roman(input_2)
print(f'Input: {input_2}\nOutput: {output_2}')

input_3 = 599
output_3 = solution.number_to_roman(input_3)
print(f'Input: {input_3}\nOutput: {output_3}')

input_4 = 1530
output_4 = solution.number_to_roman(input_4)
print(f'Input: {input_4}\nOutput: {output_4}')

input_5 = 44
output_5 = solution.number_to_roman(input_5)
print(f'Input: {input_5}\nOutput: {output_5}')

input_6 = 654
output_6 = solution.number_to_roman(input_6)
print(f'Input: {input_6}\nOutput: {output_6}')

input_7 = 1000
output_7 = solution.number_to_roman(input_7)
print(f'Input: {input_7}\nOutput: {output_7}')

input_8 = 19
output_8 = solution.number_to_roman(input_8)
print(f'Input: {input_8}\nOutput: {output_8}')