import random 
passwords = []
objects = 'AaBaCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890@!%&-_'
for i in range(7):
    new = random.choices(objects)
    passwords.append(new)
print(passwords)

#رمز تصادفی
