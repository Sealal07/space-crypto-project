
# (1, 1, 3, 5, 8, 13, 21, 34, 55)
# abcdefghijklmnop


def encrypt_hourglass(text, marker='*'):
    parts = []
    current_index = 0 #для текущей позиции в тексте
    fib_prev = 0 #фиктивное на старте
    fib_curr = 1 # текущее число (первый кусок размером с 1)

    while current_index < len(text):
        end_index = current_index + fib_curr
        chunk = text[current_index:end_index] # [start:end:step]
        if len(parts) % 2 != 0:
            chunk = chunk[::-1]
        parts.append(chunk)
        current_index = end_index
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr

    encrypt_text = marker.join(parts)
    return encrypt_text

message = 'abcdefghijklmnop'
result = encrypt_hourglass(message)
print(f'зашифрованный текст: {result}')

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

