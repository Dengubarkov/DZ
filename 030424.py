class Valid:
    def __set_name__(self, owner, point):
        self.point = "_" + point

    def __get__(self, instance, owner):
        if isinstance(instance, int):
            raise TypeError(f'координата  должна быть целым числом')
        return getattr(instance, self.point)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f'координата "{self.point}" должна быть целым числом')

        setattr(instance, self.point, value)


class Point3d:
    x = Valid()
    y = Valid()
    z = Valid()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point3d(1, 2, 3)

print(p1.__dict__)
