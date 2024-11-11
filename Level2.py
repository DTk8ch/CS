def validat_num(num):
    # additional_nums = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    is_valid = None
    while is_valid == None:
        if num.isdigit() == True and num[:1] != '0':
            is_valid = True
        elif num[:2] == '0b' and num[2:].isdigit() and num[2:].count('1') + num[2:].count("0") == len(num[2:]):
            is_valid = True
        elif num[:2] == '0x':
            for i in num[2:]:
                if '9' <= i >= '0' and 'F' <= i >= 'A':
                    is_valid = True
        else:
            num = input("This number can not be transformed. Please try another: ")
    return is_valid

def dec_to_bin(dec_number):
    x = ''
    dec_number = int(dec_number)
    while dec_number !=0:
        x = str(dec_number % 2) + x
        dec_number = dec_number // 2
    return "0b"+x

def dec_to_hex(dec_number):
    additional_nums = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    x = ''
    dec_number = int(dec_number)
    while dec_number !=0:
        if dec_number%16 < 10:
            x = str(dec_number % 16) + x
        else:
            x = additional_nums[dec_number%16]+x
        dec_number = dec_number // 16
    return "0x"+x

def hex_to_dec(hex_number):
    additional_nums = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    dec_form = 0
    hex_number = list(hex_number[2:])
    new_list = []
    for i in hex_number:
        if i.isdigit() == True:
            new_list.append(i)
        else:
            new_list.append(additional_nums[i])
    l = len(new_list)
    for i in new_list:
        i = int(i)
        dec_form += i*16**(l-1)
        l -= 1

    return dec_form

def bin_to_dec(bin_number):
    dec_form = 0
    bin_number = bin_number[2:]
    l = len(bin_number)
    bin_list = list(bin_number)
    for i in bin_list:
        y = int(i)
        dec_form += y*2**(l-1)
        l -= 1
    return  dec_form

def start_program():
    repeat_func = "1"
    while repeat_func == "1":
        number = input("Enter number in decimal, binary(use prefix 0b) or hexadecimal(use prefix 0x) form:")
        validat_num(number)
        if number[:2] == "0b":
            answer = input('Chose system to transform to between decimal("10") or hexadecimal("16"):')
            while True:
                if answer == '10':
                    print(bin_to_dec(number))
                    break
                elif answer == '16':
                    print(dec_to_hex(bin_to_dec(number)))
                    break
                else:
                    answer = input("Input is wrong, try again: ")
        elif number[:2] == "0x":
            answer = input('Chose system to transform to between decimal("10") or binary("2"):')
            while True:
                if answer == '10':
                    print(hex_to_dec(number))
                    break
                elif answer == '2':
                    print(dec_to_bin(hex_to_dec(number)))
                    break
                else:
                    answer = input("Input is wrong, try again: ")
        else:
            answer = input('Chose system to transform to between hexadecimal("16") or binary("2"):')
            while True:
                if answer == '16':
                    print(dec_to_hex(number))
                    break
                elif answer == '2':
                    print(dec_to_bin(number))
                    break
                else:
                    answer = input("Input is wrong, try again: ")

        repeat_func = input('To repeat type "1". To stop program type anything else: ')

start_program()