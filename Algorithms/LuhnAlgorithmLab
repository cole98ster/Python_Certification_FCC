def verify_card_number(digits: str):
    digits = digits.replace(" ","")
    digits = digits.replace("-","")
    sum_of_digits = 0
    for index,x in enumerate(reversed(digits)):
        temp = int(x)
        if index % 2 == 1:
            temp *= 2
            if temp > 9:
                temp -= 9
        sum_of_digits += temp
    if sum_of_digits % 10 != 0:
        return "INVALID!"
    else:
        return "VALID!"

        
    
