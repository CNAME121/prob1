price = 0
ticket_quantity = int(input('Введите количество билетов: '))
for i in range(ticket_quantity):
    i += 1
    age_of_the_visitor = int(input(f'Введите возраст посетителя для {i} билета: '))
    if age_of_the_visitor < 18:
            print('Бесплатный билет если меньше 18 лет')
    elif 18 <= age_of_the_visitor < 25:
            price += 990
            print('Стоимость билета - 990 руб.')
    else:
            price += 1390
            print('Стоимость билета - 1390 руб.')

if ticket_quantity > 3:
    all_price = price - ((price / 100) * 10)
    print(f'Сумма к оплате - {price} руб. Вы получили 10 % скидки так-как купили больше 3 билетов!')
else:
    print(f'Сумма к оплате - {price} руб.')