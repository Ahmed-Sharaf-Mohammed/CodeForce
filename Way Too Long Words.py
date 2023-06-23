n = int(input())

words = []
for i in range(n):
    word = input()
    words.append(word)

abbreviations = []
for word in words:
    if len(word) > 10:
        abbreviation = word[0] + str(len(word) - 2) + word[-1]
        abbreviations.append(abbreviation)
    else:
        abbreviations.append(word)

for abbreviation in abbreviations:
    print(abbreviation)
