import re


def standardize_expression(expr_str):
    """标准化表达式（处理+和×的交换律，确保去重）"""
    # 步骤1：按+/-拆分项（如"a + b - c"拆分为["a", "+b", "-c"]）
    terms = re.split(r"(?=[+-])" , expr_str)
    terms = [t for t in terms if t]  # 过滤空字符串

    # 步骤2：标准化每一项（处理×/÷的因子）
    standardized_terms = []
    for term in terms:
        sign = term[0] if term[0] in "+-" else "+"
        content = term[1:] if sign in "+-" else term

        # 按×/÷拆分因子（如"b×c"拆分为["b", "×c"]）
        factors = re.split(r"(?=[×÷])" , content)
        if not factors:
            continue

        # 提取因子值和运算符（如["b", "×c"] → [("×", "b"), ("×", "c")]）
        factor_list = []
        for f in factors:
            if f[0] in "×÷":
                op , val = f[0] , f[1:]
            else:
                op , val = "×" , f  # 第一项默认为×
            factor_list.append((op , val))

        # 对×的因子排序（处理交换律）
        product_groups = []
        current_group = [factor_list[0][1]]
        for op , val in factor_list[1:]:
            if op == "×":
                current_group.append(val)
            else:
                product_groups.append(("×" , sorted(current_group)))
                product_groups.append((op , [val]))
                current_group = []
        if current_group:
            product_groups.append(("×" , sorted(current_group)))

        # 重组因子字符串（如["b", "c"] → "b×c"）
        standardized_factor = ""
        for op , vals in product_groups:
            standardized_factor += op.join(vals)

        standardized_terms.append(f"{sign}{standardized_factor}" if sign == "-" else standardized_factor)

    # 步骤3：对+项排序（处理交换律）
    plus_terms = [t for t in standardized_terms if not t.startswith("-")]
    minus_terms = [t[1:] for t in standardized_terms if t.startswith("-")]
    plus_terms_sorted = sorted(plus_terms)
    minus_terms_sorted = sorted(minus_terms)

    # 重组标准化表达式
    expr_standardized = "+".join(plus_terms_sorted)
    if minus_terms_sorted:
        expr_standardized += "-" + "-".join(minus_terms_sorted)
    return expr_standardized if expr_standardized else "0"