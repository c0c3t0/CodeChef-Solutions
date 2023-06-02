def oddish_or_evenish(num):
    to_list = [int(el) for el in str(num)]
    total = sum(to_list)

    if total % 2 == 0:
        return 'Evenish'
    return 'Oddish'


print(oddish_or_evenish(43))
print(oddish_or_evenish(373))
print(oddish_or_evenish(4433))
