 # В FFD еще должна происходить сортировка, но здесь значения уже передаются в нужном виде
def FFD(values, bins=[]):
    for el in values:
        placed = False
        for bin in bins:
            if sum(bin) + el <= 1:
                bin.append(el)
                placed = True
                break
        if not placed:
            bins.append([el])
    return bins

def bin_packing(values, eps):
    # 1. Сортировка в невозрастающем порядке
    items_sorted = sorted(values, reverse=True)

    # 2. Разделение на большие и маленькие предметы
    k = 0
    while k < len(items_sorted) and items_sorted[k] > eps / 2:
        k += 1
    large_items = items_sorted[:k]
    small_items = items_sorted[k:]

    # 3. Упаковка больших предметов
    bins_large = FFD(large_items)

    # 4. Доупаковка маленьких предметов
    bins_small = FFD(small_items, bins_large)

    return bins_small
