def get_input():
    array = []
    while array == []:
        temp = input(f"\nВведите любые числа через пробел:").split(' ')
        for a in temp:
            if a == '':
                continue
            try:
                x = int(a)
                array.append(x)
                idx = len(array)-1
                while idx > 0 and array[idx-1] > x:
                    array[idx] = array[idx-1]
                    idx -= 1
                array[idx] = x
            except ValueError:  # Сообщение об ошибке, если пользователь сделает неверный ввод
                print(f"\nНеверный ввод, введите целые числа")
                array = []
                break
    return array

def lin_search(array, element):
    idx = len(array)-1
    while element <= array[idx]:
        idx -= 1
    return idx

array = get_input()
print(f"\nОтсортированно: {array}")
while True:
    try:
        element = int(input(f"\nВведите целое число: "))
        break
    except ValueError:  # Здесь будет сообщение об ошибке, если пользователь сделает неверный ввод
        print(f"\nНеверный ввод, введите целые числа!")
idx = lin_search(array, element)
print(f"\nНомер позиции элемента, который меньше введенного вами числа равен {idx} ")
print(f"\nЕго значение: {array[idx]}")
print(f"\nСледующий за ним элемент, больший или равный вашему числу, имеет значение:")
print(f"{'Больший элемент' if idx == len(array)-1 else str(array[idx+1])}")
print(f"\nЕсли вы захотите вписать свое число в последовательность его место будет между этими двумя элементами")