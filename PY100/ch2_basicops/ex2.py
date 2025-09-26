input = 4936

ones = input % 10
tens = input % 100 // 10
hundreds = input % 1000 // 100
thousands = input % 10000 // 1000

print(ones, tens, hundreds, thousands)
