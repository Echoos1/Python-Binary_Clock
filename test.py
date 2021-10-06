hour = 2021

list = []
list.clear()
for i in range(12):
    list.append((hour // (2**i)) % 2)
list.reverse()

print(list)

