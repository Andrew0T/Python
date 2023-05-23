# reverse sort with range of 3 top scores within test scores

test_scores = [45, 23, 89, 78, 98, 55, 74, 87, 95, 75]

test_scores.sort(reversed= True)

for i in range(0, 3):
  print(test_scores[i])