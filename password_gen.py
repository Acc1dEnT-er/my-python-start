import random
import string

length = int(input("Введите длину пароля: "))
count = int(input("Сколько паролей сгенерировать: "))

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(count):
    password = "".join(random.choice(characters) for _ in range(length))
    print(f"Пароль {i+1}: {password}")
