from arg_parser import parse_args
from expression_generator import generate_expression
from duplicate_checker import standardize_expression
from file_handler import write_problems_and_answers , grade_exercises


def generate_problems(n , r):
    """生成n个不重复的题目及答案"""
    problems = []
    answers = []
    seen = set()  # 存储标准化后的表达式，用于去重

    while len(problems) < n:
        expr_str , result = generate_expression(r)
        if not expr_str or not result:
            continue  # 跳过无效表达式

        # 标准化表达式并去重
        standardized = standardize_expression(expr_str)
        if standardized in seen:
            continue
        seen.add(standardized)

        # 格式化结果（真分数/带分数）
        if result.denominator == 1:
            ans_str = str(result.numerator)
        else:
            integer_part = result.numerator // result.denominator
            numerator = result.numerator % result.denominator
            if integer_part == 0:
                ans_str = f"{numerator}/{result.denominator}"
            else:
                ans_str = f"{integer_part}'{numerator}/{result.denominator}"

        problems.append(f"{expr_str} =")
        answers.append(ans_str)

    return problems , answers


def main():
    args = parse_args()
    if args.e and args.a:
        # 判题模式
        grade_exercises(args.e , args.a)
    else:
        # 生成模式
        problems , answers = generate_problems(args.n , args.r)
        write_problems_and_answers(problems , answers)


if __name__ == "__main__":
    main()