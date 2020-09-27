# coding=utf-8
def swap_two_words(input_string):
    # -------------------------------
    # Реализовать программу, которая получает на вход строку, содержащую 2 слова через пробел.
    # На выходе программа должна выводить эти же слова в обратном порядке.
    # При решении не стоит пользоваться условными операторами if и циклами (for, while).
    # -------------------------------
    array = input_string.split(' ', 1)
    output_string = array[1] + ' ' + array[0]
    print(output_string)
    return output_string


swap_two_words('One Two')
