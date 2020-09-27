# coding=utf-8
def get_even_before_237(input_array):
    # --------------------
    # Напишите программу,
    # которая выводит чётные числа из заданного списка и останавливается, если
    # встречает число 237
    # --------------------
    stop_number = 237
    output_array = []
    for number in input_array:
        if number == stop_number:
            print 'Программа остановилась, встретилось блокирующее число', 237
            break
        else:
            if number % 2 == 0:
                print(number)
                output_array.append(number)
    return output_array


get_even_before_237([4, 156, 65, 77, 90, 986, 537, 3423, 11, 237, 1234, 523, 3456])
