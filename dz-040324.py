ar = [-2,3,8,-11,-4,6]
print(ar)

def nullup(data):
    if not data:
        return False
    if data[0] > 0:
        return nullup(data[1:]) + 1
    else:
        return nullup(data[1:])


print("n =",nullup(ar))