questions = (
    "How many stars in solar system?\n",
    "How many genders exists?\n"
    "How many hands have normal man?\n"
    "How many colors on the traffic light?\n"
    "How many fingers have normal mans palm?\n"
)
correct_answers = ("1", "2", "3", "4", "5")
answers = [input() for _ in range(len(correct_answers))]
score = 0
for i in range(len(answers)):
    if answers[i] == correct_answers[i]:
        score += 1
res = {
    "score": score,
    "correct answers": correct_answers
}
print(res)

