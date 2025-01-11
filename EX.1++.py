import random
import string
objects = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choices(objects, k=7))
print(f"Generated Password: {password}")
