# Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
# It should follow the API demonstrated in the examples below.
# # Multiple roman numeral values will be tested for each helper method.
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit
# and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting
# in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
# Input range : 1 <= n < 4000
# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
class RomanNumerals:
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def to_roman(self):
        result = ''
        count = 0
        while self:
            div = self // RomanNumerals.arab[count]
            self %= RomanNumerals.arab[count]
            while div:
                result += RomanNumerals.roman[count]
                div -= 1
            count += 1
        return result

    def from_roman(self):
        result = 0
        for idx, val in enumerate(self):
            first = RomanNumerals.arab[RomanNumerals.roman.index(val)]
            second = RomanNumerals.arab[RomanNumerals.roman.index(self[idx + 1])] if idx + 1 != len(self) else -1
            if first >= second:
                result += first
            else:
                result -= first
        return result


print(RomanNumerals.to_roman(1990))
print(RomanNumerals.from_roman("XM"))
