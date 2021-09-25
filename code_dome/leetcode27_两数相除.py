"""
leetcode27 两数相除
题目以及翻译：
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

链接：https://leetcode-cn.com/problems/divide-two-integers

"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
        # 取运算符
        sign = -1 if dividend * divisor < 0 else 1
        a = abs(dividend)
        b = abs(divisor)
        tot = 0
        while a >= b:
            cnt = 0
            while a >= (b << cnt):
                cnt += 1
            cnt -= 1
            tot += 1 << cnt
            a -= b << cnt
        return sign * tot if INT_MIN <= sign * tot <= INT_MAX else INT_MAX
