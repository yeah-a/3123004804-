import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="小学四则运算题目生成器")
    parser.add_argument("-n", type=int, help="生成题目的数量（正整数）")
    parser.add_argument("-r" , type = int , required = False , help = "数值范围（生成模式必须提供，正整数）")
    parser.add_argument("-e", type=str, help="题目文件路径（判题模式）")
    parser.add_argument("-a", type=str, help="答案文件路径（判题模式）")
    args = parser.parse_args()

    # 校验参数合法性
    if args.e or args.a:
        if not (args.e and args.a):
            parser.error("判题模式需同时指定 -e 和 -a 参数")
        if args.n is not None:
            parser.error("判题模式不需要 -n 参数")
    else:
        if args.n is None or args.n <= 0:
            parser.error("生成模式需提供正整数的 -n 参数")
        if args.r is None or args.r <= 0:  # 新增 args.r is None 检查
            parser.error("生成模式需提供正整数的 -r 参数")
    return args