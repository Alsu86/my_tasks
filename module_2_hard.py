def generate_password(n):
    result = ""
    for i in range(1, 20 + 1):
        for j in range(i + 1, 20 + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += str(i) + str(j)
    return result


n = int(input())
password = generate_password(n)
print("Сгенерированный пароль:", password)