"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return 'number can not less than 0'

        units = {0: '', 1: 'หนึ่ง', 2: 'สอง', 3: 'สาม', 4: 'สี่',
            5: 'ห้า', 6: 'หก', 7: 'เจ็ด', 8: 'แปด', 9: 'เก้า'
        }
        tens = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

        if number == 0:
            return 'ศูนย์'

        text = ''
        place = 0

        while number > 0:
            digit = number % 10
            if digit == 1 and place == 0:
                text = 'เอ็ด'
            elif digit != 0 or place == 0:
                text = units[digit] + tens[place] + text
            number //= 10
            place += 1

        text = text.replace('หนึ่งสิบ', 'สิบ')

        return text

solution = Solution()

input_1 = 101
output_1 = solution.number_to_thai(input_1)
print(f'Input: {input_1}\nOutput: {output_1}')

input_2 = -1
output_2 = solution.number_to_thai(input_2)
print(f'Input: {input_2}\nOutput: {output_2}')

input_3 = 0
output_3 = solution.number_to_thai(input_3)
print(f'Input: {input_3}\nOutput: {output_3}')

input_4 = 1530
output_4 = solution.number_to_thai(input_4)
print(f'Input: {input_4}\nOutput: {output_4}')

input_5 = 35
output_5 = solution.number_to_thai(input_5)
print(f'Input: {input_5}\nOutput: {output_5}')

input_6 = 35496
output_6 = solution.number_to_thai(input_6)
print(f'Input: {input_6}\nOutput: {output_6}')

input_7 = 1000000
output_7 = solution.number_to_thai(input_7)
print(f'Input: {input_7}\nOutput: {output_7}')

input_8 = 18
output_8 = solution.number_to_thai(input_8)
print(f'Input: {input_8}\nOutput: {output_8}')