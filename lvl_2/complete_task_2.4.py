# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строки.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"


def remove_exclamation_marks(s):
    stroka = s.split('!')
    return ''.join(stroka)
# .split - метод сканирования всей строки и разделения ее в случае нахождения символа- разделителя
# .join - метод преобразования (объединения) списка в строку

stroka="Hi! Hello!   Hello!!!        Oh, no!!"
print(remove_exclamation_marks(stroka))


# Пункт B.
# Удалите восклицательный знак из конца строки.
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    pass

def remove_last_em(s):
    if s[-1] == '!':
#        stroka = list(s)
#        del stroka[-1]
        stroka = s [0 : -2]
    return ''.join(stroka)

stroka="Hi! Hello!   Hello!!!        Oh, no!!"
print(remove_last_em(stroka))





# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    pass


stroka="Hi! Hello! Hello!!! Oh, no!!"
def remove_word_with_one_em(s):
    stroka_s = s.split(' ') # Разделяем строку на слова по одиночным пробелам (условие задачи)
#    print(stroka_s)
    stroka_new = []
#    print(stroka_new)
    for i in range(len(stroka_s)):
        schet = 0
        for j in stroka_s[i]: # Для каждого слова считаем количество восклицательных знаков
            if j == '!':
                schet += 1
        if schet > 1:   # Если их больше одного, добавляем слово к новой строке
            stroka_new.append(stroka_s[i])
        elif schet == 0: # Если не найдено ни одного, добавляем слово к новой строке
            stroka_new.append(stroka_s[i])
    return stroka_new

remove_word_with_one_em(stroka)
print(remove_word_with_one_em(stroka))