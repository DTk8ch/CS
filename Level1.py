def validat_bin(num):
    is_bin = None
    while is_bin == None:
        if num.isdigit() == True:
            is_bin = False
        elif num[:2] == '0b' and num[2:].isdigit() and num[2:].count('1') + num[2:].count("0") == len(num[2:]):
            is_bin = True
        else:
            num = input("This number can not be transformed. Please try another: ")
    return is_bin

def dec_to_bin(dec_number):
    x = ''
    dec_number = int(dec_number)
    while dec_number !=0:
        x = str(dec_number % 2) + x
        dec_number = dec_number // 2
    return "0b"+x

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
        number = input("Enter number in decimal or binary(use prefix 0b) form:")
        if validat_bin(number) == True:
            print(bin_to_dec(number))
        else:
            print(dec_to_bin(number))

        repeat_func = input('To repeat type "1". To stop program type anything else: ')

start_program()




