


def scene_1():
    import time
    print('---------------------------------------------------------------------------------------------------------------------------------------------')
    print("ГГ просывается. Закованный в цепи он вытается выбраться.Вдруг кирпич,который бы присоединен к цепи,падает,и грохот доносится до нижних этажей")
    print('---------------------------------------------------------------------------------------------------------------------------------------------')
    time.sleep(2)
    print("ГГ видит окно и решает залесть в него. ГГ взберается и думает куда ему идти ")
    print('---------------------------------------------------------------------------------------------------------------------------------------------')
    time.sleep(2)
    print('Выбор: 1.Залесть наверх    '
                 '2.Прыгнуть вниз')
    print('---------------------------------------------------------------------------------------------------------------------------------------------')
    time.sleep(2)

    c1=input()
    ans='incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=='1'):
            print('ГГ взобрался и нашел веревку ведущюю вниз')
            ans='correct'
            choise_1='True'
        elif(c1.upper()=='2'):
            print('ГГ прыгнул в стог сена')
            ans='correct'
            choise_1='False'
        else:
             print('Введите корректный ответ')   
             c1=input()
    time.sleep(2)
    #scene_2(choise_1)
scene_1()

