# 1) Write a function that converts kilograms into grams.
# 2) Write a function that converts grams into kilograms.
# *Bonus: Do both in the same function. Using a parameter "kgtog" - kilo to
# Gram or "gtokg" - gram to kilo.
#
c=float(input('Hello, Enter kilograms to convert in grams'))

def convert_k_to_g(c):
    return c * 1000

grams=convert_k_to_g(c)

print("in Grams it is: ", grams)


gr=float(input('Enter Grams '))

def convert_g_to_k(c):
    return gr / 1000

kilograms=convert_g_to_k(gr)

print("in kilograms it is: ", kilograms)

print("thanks")