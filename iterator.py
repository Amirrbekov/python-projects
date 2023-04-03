l = [3,4,5,2,3,632,3,1,3,4]

iterator = iter(l)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break