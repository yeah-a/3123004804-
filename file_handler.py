from expression_evaluator import evaluate_expression
from number_generator import parse_number_str


def write_problems_and_answers(problems , answers):
    """将题目和答案写入文件"""
    with open("Exercises.txt" , "w" , encoding = "utf-8") as f:
        f.write("\n".join(problems))
    with open("Answers.txt" , "w" , encoding = "utf-8") as f:
        f.write("\n".join(answers))


def grade_exercises(exercise_path , answer_path):
    """对比题目和答案，生成Grade.txt"""
    with open(exercise_path , "r" , encoding = "utf-8") as f:
        exercises = [line.strip().replace(" =" , "") for line in f if line.strip()]
    with open(answer_path , "r" , encoding = "utf-8") as f:
        answers = [line.strip() for line in f if line.strip()]

    if len(exercises) != len(answers):
        raise ValueError("题目和答案数量不匹配")

    correct = []
    wrong = []
    for i in range(len(exercises)):
        expr = exercises[i]
        expected_ans = answers[i]
        try:
            actual_ans = evaluate_expression(expr)
            expected_ans_frac = parse_number_str(expected_ans)
            if actual_ans == expected_ans_frac:
                correct.append(i + 1)  # 题目编号从1开始
            else:
                wrong.append(i + 1)
        except:
            wrong.append(i + 1)

    with open("Grade.txt" , "w" , encoding = "utf-8") as f:
        f.write(f"Correct: {len(correct)} ({', '.join(map(str , correct))})\n")
        f.write(f"Wrong: {len(wrong)} ({', '.join(map(str , wrong))})\n")