def is_empty(string):
    if len(string) == 0:
        return True
    else:
        return False

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True