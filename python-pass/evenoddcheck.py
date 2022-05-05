def EvenOddCheck():
    x = int(input('Enter X value: '))
    Num = []

    if x > 0 and x <= 10:
        for i in range(0, x):
            Num.append( int(input()))

    
    else:
        print('Enter value from 1 to ten only.')
    
    for i in Num:
        if i % 2 == 0:
            print(f'{i} is even')
        else:
            print(f'{i} is odd')


EvenOddCheck()
