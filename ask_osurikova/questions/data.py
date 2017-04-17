authors =['author_' + str(i) for i in range(1,10)]

tags =['tag_' + str(j) for j in range(1,20)]

answers = ['text of answer ' + str(j) for j in range(1,5)]

questions = []
for i in range(1, 30):
    questions.append({
        'title': 'title ' + str(i),
        'id': i,
        'text': 'text ' + str(i),
        'answers': i,
    })