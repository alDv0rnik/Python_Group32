Task 5
d = {"question_1": "10", "question_2": "20", "question_3": "30"}
correct_answers = 0
score = 0
for k, v in d.items():
    if input(k) == v[0]:
        score = score + 1
        correct_answers = correct_answers + 1
print({"score": score, "correct_answers": correct_answers})
