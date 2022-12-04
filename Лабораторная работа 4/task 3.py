def delete(list_, index=None):
    if index is None or index == -1:
        return list_[:-1]
    list2 = list_[:index]
    return list2 + list_[index + 1:]

print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
