import re

def check_scout(msg):
    clean_str = msg.replace(' ', '')
    # []-один из символов
    # : обязательно
    # ? символ будет встречаться 0 или более раз
    # \d цифра
    #  + один и более раз
    # x:-76
    x_match = re.search(r'[XxХх]:(-?\d+)', clean_str)
    y_match = re.search(r'[YyУу]:(-?\d+)', clean_str)
    r_match = re.search(r'[RrРр]:(-?\d+)', clean_str)
    # X:12
    # Y:-4
    # R:20
    x = int(x_match.group(1))
    y = int(y_match.group(1))
    r = int(r_match.group(1))

    distance_squared = x**2 + y**2
    radius_squared = r**2
    werdict = distance_squared > radius_squared
    return werdict

print(check_scout('X: 12, Y:-4, R: 20'))#false
print(check_scout('X: 30, у: 30, Р: 10'))#true
