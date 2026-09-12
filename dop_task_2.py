def get_digits(num):       
    digits = []
    for digit in str(num):
        digits.append(int(digit))
    return digits 

def digit_root(num):
    if num > 10000000:
        return None
    else:
        result = num
        while result >= 10:
            result = sum(get_digits(result))
    return result
