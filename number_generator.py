from fractions import Fraction
import random


def generate_natural(r):
    """生成0~r-1的自然数"""
    return random.randint(0 , r - 1)


def generate_proper_fraction(r):
    """生成真分数（分子 < 分母）"""
    denominator = random.randint(2 , r - 1)  # 分母范围：2~r-1
    numerator = random.randint(1 , denominator - 1)  # 分子范围：1~分母-1
    return numerator , denominator


def generate_mixed_fraction(r):
    """生成带分数（整数部分+真分数）"""
    integer_part = random.randint(1 , r - 2)  # 避免整数部分过大导致分母溢出
    denominator = random.randint(2 , r - 1)
    numerator = random.randint(1 , denominator - 1)
    return integer_part , numerator , denominator


def generate_number(r):
    """随机生成自然数/真分数/带分数，返回字符串和Fraction对象"""
    num_type = random.choice(["natural" , "proper" , "mixed"])  # 等概率选择类型

    if num_type == "natural":
        n = generate_natural(r)
        return str(n) , Fraction(n)

    elif num_type == "proper":
        numerator , denominator = generate_proper_fraction(r)
        return f"{numerator}/{denominator}" , Fraction(numerator , denominator)

    else:  # mixed
        integer , numerator , denominator = generate_mixed_fraction(r)
        return f"{integer}'{numerator}/{denominator}" , Fraction(integer * denominator + numerator , denominator)


def parse_number_str(s):
    """将数字字符串（自然数/真分数/带分数）转换为Fraction对象"""
    if "'" in s:  # 带分数（如2'3/8）
        integer_part , frac_part = s.split("'")
        numerator , denominator = map(int , frac_part.split("/"))
        return Fraction(int(integer_part) * denominator + numerator , denominator)
    elif "/" in s:  # 真分数（如3/5）
        numerator , denominator = map(int , s.split("/"))
        return Fraction(numerator , denominator)
    else:  # 自然数（如5）
        return Fraction(int(s))