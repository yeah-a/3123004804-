import random
from number_generator import generate_number
from expression_evaluator import evaluate_expression


def generate_operators(count):
    """生成count个运算符（+、-、×、÷）"""
    return [random.choice(["+" , "-" , "×" , "÷"]) for _ in range(count)]


def check_expression_validity(nums , ops):
    """校验表达式是否合法：无负数、除法结果为真分数"""
    current = nums[0]
    for i in range(len(ops)):
        op = ops[i]
        next_num = nums[i + 1]

        if op == "-" and current < next_num:
            return False  # 减法结果为负数
        if op == "÷":
            if next_num == 0:
                return False  # 除数为0
            if current % next_num == 0:
                return False  # 除法结果为整数（非真分数）

        # 更新当前值（用于后续校验）
        if op == "+":
            current += next_num
        elif op == "-":
            current -= next_num
        elif op == "×":
            current *= next_num
        elif op == "÷":
            current /= next_num
    return True


def generate_expression(r):
    """生成单个合法表达式（1~3个运算符），返回表达式字符串和结果（无重试）"""
    from random import randint , choice
    from fractions import Fraction

    # 内联数字生成函数（减少调用开销）
    def _generate_number(r , min_num = 0 , max_num = None):
        max_num = max_num or r
        num = randint(min_num , max_num) if max_num >= min_num else min_num
        return str(num) , Fraction(num)

    op_count = randint(1 , 3)  # 运算符数量：1~3个
    nums = []  # 存储Fraction对象（用于计算）
    num_strs = []  # 存储数字字符串（用于构建表达式）
    ops = []  # 存储运算符

    # 生成第一个数字
    num_str , num = _generate_number(r)
    nums.append(num)
    num_strs.append(num_str)

    # 生成后续运算符和数字（生成时确保合法性）
    for _ in range(op_count):
        op = choice(['+' , '-' , '*' , '/'])  # 可根据需求调整运算符权重

        if op == '-':
            # 减法：确保被减数 >= 减数（避免负数）
            prev_num = nums[-1]
            num_str , num = _generate_number(r , max_num = prev_num)  # 减数 <= 被减数
        elif op == '/':
            # 除法：确保除数不为0且结果为真分数（a = b * k，k为正整数）
            b = randint(1 , r)  # 除数b ∈ [1, r]
            max_k = r // b  # 确保a = b*k ≤ r
            k = randint(1 , max_k) if max_k > 0 else 1
            a = b * k
            num_str , num = str(a) , Fraction(a)
        else:
            # 加法/乘法：直接生成范围内数字
            num_str , num = _generate_number(r)

        ops.append(op)
        nums.append(num)
        num_strs.append(num_str)

    # 构建表达式字符串（列表拼接高效版）
    parts = [num_strs[0]]
    for op , num_str in zip(ops , num_strs[1:]):
        parts.append(f" {op} {num_str}")
    expr_str = ''.join(parts)

    # 直接计算结果（避免字符串解析）
    result = nums[0]
    for i in range(op_count):
        op = ops[i]
        next_num = nums[i + 1]
        if op == '+':
            result += next_num
        elif op == '-':
            result -= next_num
        elif op == '*':
            result *= next_num
        elif op == '/':
            result /= next_num

    return expr_str , result