def RhymeDef(text):
    count = 0
    for letter in text:
        if letter in vowels:
            count = count + 1
    return count


vowels = ['ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
rhyme = input("text = ").lower()
phrases = rhyme.split(' ')

vowelsCount = RhymeDef(phrases[0])
isrhymeOk = True
for phrase in phrases:
    isrhymeOk &= RhymeDef(phrase) == vowelsCount

if isrhymeOk:
    print("Парам пам-пам")
else:
    print("Пам парам")