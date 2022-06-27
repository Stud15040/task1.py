text = input('Введите строку \n')
text = text.split(" ")
i = 0
for word in text:
    if word[0].lower() == "е":
        i = i+1;
print ('Количество слов, начинающихся с буквы "е": ',i)
