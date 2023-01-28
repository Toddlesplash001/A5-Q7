multiples_of_7 = []
multiples_of_11 = []
for i in range(1,501):
    if i%7 == 0:
        multiples_of_7.append(i)
    if i%11 == 0:
        multiples_of_11.append(i)
print("Multiples of 7 = ",multiples_of_7)
print("Multiples of 11 = ",multiples_of_11)
