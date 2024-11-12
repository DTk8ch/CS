def validat_num(num):
    is_valid = False
    while is_valid == False:
        if num.isdigit() and num[:1]!="0":
            is_valid = True
            break
        elif 'X' in num and num[num.index('X')+1:].isdigit() and 2<=int(num[num.index('X')+1:])<=16:
            system_of_n = int(num[num.index('X')+1:])
            all_numbers = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            first_digit = sorted(list(num[:num.index('X')]), reverse=True)[0]
            if first_digit not in all_numbers:
                num = input("This number can not be transformed. Please try another: ").upper()
                break
            if all_numbers.index(first_digit)+1<system_of_n:
                is_valid = True
                break
            else:
                num = input("This number can not be transformed. Please try another: ").upper()

        else:
            num = input("This number can not be transformed. Please try another: ").upper()



    return is_valid

def convert_dec(dec_number, system_n):
    additional_nums = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    x = ''
    dec_number = int(dec_number)
    while dec_number !=0:
        if dec_number%system_n < 10:
            x = str(dec_number % system_n) + x
        else:
            x = additional_nums[dec_number%system_n]+x
        dec_number = dec_number // system_n
    return x+f"x{system_n}"

def system_n_to_dec(system_n_number):
    additional_nums = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    dec_form = 0
    N = int(system_n_number[system_n_number.index('X')+1:])
    system_n_number = list(system_n_number[:system_n_number.index('X')].upper())
    new_list = []
    for i in system_n_number:
        if i.isdigit() == True:
            new_list.append(i)
        else:
            new_list.append(additional_nums[i])
    l = len(new_list)
    for i in new_list:
        i = int(i)
        dec_form += i*N**(l-1)
        l -= 1

    return dec_form

def start_program():
    repeat_func = "1"
    while repeat_func == "1":
        number = input("Enter number in any system from binary to hexadecimal(use prefix xN or without it if num. is decimal):")
        number = number.upper()
        validat_num(number)
        system_n_rec = input('Enter system you want to convert to(in range from 2 to 16):')
        while True:
            if system_n_rec.isdigit() == True and 2<=int(system_n_rec)<=16:
                break
            else:
                system_n_rec = input("System is wrong, try another one:")
        if number.isdigit() == True:
            print(convert_dec(number, system_n=int(system_n_rec)))
        else:
            print(convert_dec(system_n_to_dec(number), system_n=int(system_n_rec)))


        repeat_func = input('To repeat type "1". To stop program type anything else: ')


start_program()
