import re
from fractions import Fraction
from number_generator import parse_number_str

def evaluate_expression(expr_str):
    """计算表达式结果（支持分数运算）"""
    # 替换运算符并转换为Fraction计算
    expr = expr_str.replace("×", "*").replace("÷", "/")
    # 正则匹配数字并替换为Fraction对象
    def replace_num(match):
        return f"Fraction({parse_number_str(match.group(0))})"
    expr = re.sub(r"\d+’\d+/\d+|\d+/\d+|\d+", replace_num, expr)
    try:
        return eval(expr)  # 安全计算（仅处理生成的表达式）
    except:
        return None