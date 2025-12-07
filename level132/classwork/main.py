def len_plant(a):
    if len(a) % 2 == 0:
        return a[len(a) // 2:]
    else:
        return a[len(a) // 2 + 1:]
print(len_plant("Helro"))