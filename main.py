# (1, 1, 3, 5, 8, 13, 21, 34, 55)
# abcdefghijklmnop
from django.db.models.expressions import result


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
