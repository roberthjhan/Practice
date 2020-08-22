"""
Prompt:
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example,
truncate(8.345) = 8 and truncate(-2.7335) = -2.

https://leetcode.com/problems/divide-two-integers/

My solution uses a recursive function to subtract the second largest power of the divisor from the dividend.
The process is repeated on the new dividend until its absolute value is less than the absolute value of the divisor.
After each call to the recursive function a count is recorded.
At the end of the function logic is used to determine whether the result should be positive or negative.

Results: 90th percentile runtime, 80th percentile space.

Author: Rob Han
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def scale_div(dividend, divisor, count):
            """
            Recursively subtracts double the divisor until doubling the divisor
            is greater than the dividend - divisor. Starts with first step
            completed. Returns dividend - second largest power of the divisor.
            """
            if divisor + divisor > dividend - divisor:
                return dividend, count
            else:
                dividend -= divisor
                divisor += divisor # Double divisor
                count += count # Double count
                return scale_div(dividend, divisor, count)
        # Initialize return value and variables
        ret = 0
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        # Division step
        while abs_dividend >= abs_divisor:
            abs_dividend, count = scale_div(abs_dividend - abs_divisor, abs_divisor, 1)
            ret += count
        # Should the sign on return value be swapped?
        swap = dividend < 0 < divisor or divisor < 0 < dividend
        # The min and max is used for a unique case posed by the prompt and is not actually needed
        if swap:
            return max(-ret, -2147483648)
        else:
            return min(ret, 2147483647)