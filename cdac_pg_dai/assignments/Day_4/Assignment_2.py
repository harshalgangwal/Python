Scores = {'Alice': 85, 'Bob': 92, "Charlie": 78, 'David': 65}

Siya = {x: Scores[x] + 5 for x in Scores if Scores[x] > 80}
print(Siya)
