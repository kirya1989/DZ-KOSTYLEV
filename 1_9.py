import random

storage = {}
question = None

while question != 'выход':
    question = input('Введите вопрос: ')
    ans = 'да' if random.random() < 0.5 else 'нет'

    q_comp = set(question.split())

    res = None

    for qkey in storage:
        q = set(qkey.split())
        similarity = len(q_comp.intersection(q)) / len(q_comp)
        if similarity >= 0.5:
            print('Вопрос уже был!')
            res = storage[qkey]
            break
    
    if res == None:
        res = ans
        storage[question] = ans

    print(res)
    