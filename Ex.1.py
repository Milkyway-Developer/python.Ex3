import random
passwords = []
objects = "AaBaCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890@!%&-_"
for i in range(7):
    new = random.choices(objects, k=7)
    passwords.append(new)
rammz = "".join(new)
print(rammz)

# رمز تصادفی
