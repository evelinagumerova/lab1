def proc1():
    words = []
    while (new_word := str(input())) !='stop':
        words.append(new_word)

    print(' '.join(words))



def proc2():
    word=input()
    if 'ф' in word or 'Ф' in word:
        print(word,'-Ого! Это очень редкое слово!')
    else:
        print(word,'Эх, это не очень редкое слово...')



def proc3():
    import random
    k=0
    while k<3:
        a=random.randint(0,9)
        b=random.randint(0,9)
        print(a,'+',b,'=')
        res=int(input())
        if res == a+b:
            print('Правильно!')
        else:
            print('Неправильно!')
            k+=1
    else:
        print('Game over')


proc1()
proc2()
proc3()