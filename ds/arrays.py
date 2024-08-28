import array as arr

a = arr.array('i', [1, 2, 3, 5, 5, 3, 3, 2])
print(a)
while True:
    try:
        a.remove(3)
    except ValueError:
        break
print(a)