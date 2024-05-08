# additional functions to process strings of numbers separated by numbers all at once, i.e. convertBase('2154 53656 63 7434 2456', 32) -> convertDecimal('23a 1kco 1v 78a 2co', 32) -> '2154 53656 63 7434 2456'

def convertBase(input_str, base):
    numbers_str_list = input_str.split()
    binary_numbers = [toBase(int(number), base) for number in numbers_str_list]
    return ' '.join(binary_numbers)

def convertDecimal(input_str, base):
    numbers_str_list = input_str.split()
    binary_numbers = [fromBase(number, base) for number in numbers_str_list]
    return ' '.join(map(str, binary_numbers))
