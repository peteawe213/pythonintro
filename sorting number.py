variable = [5, 1, 2, 5, 5, 3, 6, 9]
uniques = []
for number in variable:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()
print(uniques)
