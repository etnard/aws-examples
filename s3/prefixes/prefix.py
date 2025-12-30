import random

words = [
    "alpha","beta","gamma","delta","epsilon","zeta","eta","theta",
    "lambda","omega","kappa","sigma","vector","matrix","entropy",
    "cipher","hash","binary","packet","kernel","sandbox","runtime"
]

prefix = ""
while len(prefix) < 1024:
    prefix += random.choice(words) + "/"

print(prefix[:1024])
print("Length:", len(prefix[:1024]))
