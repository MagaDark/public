price_all = 0
while True:
    try:
        tick = input('Сколько человек хотите зарегистрировать на конференцию? ')
        tick = int(tick)
        if type(tick) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(tick):
    i += 1
    while True:
        try:
            age_for_ticket = input(f'Какой возраст участника №{i}? ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('Билет бесплатный')
            elif 25 > age_for_ticket >= 18:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if tick > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'Сумма к оплате {price_all} руб. (с учетом 10%-ой скидки за регистрацию больше 3х человек)')
else:
    print(f'Сумма к оплате {price_all} руб.')