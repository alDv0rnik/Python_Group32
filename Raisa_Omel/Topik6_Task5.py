dct={'qustion1':['answer1',2],'qustion2':['answer2',5], 'qustion3':['answer3',1]}
score = 0
correct_answers = 0
for key,val in dct.items():
    if input(key) ==val[0]:
        score+=val[1]
        correct_answers+=1

print({'score': score, 'correct_answers': correct_answers})
