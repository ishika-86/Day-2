s = input()

dig = let = 0

for c in s:
    if c.isdigit():
        dig = dig + 1
    elif c.isalpha():
        let = let + 1
    else:
        pass

print('Letters ', let)
print('Digits: ', dig)

