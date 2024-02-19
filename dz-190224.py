def decor_f(fn):
    def wrap(*x):
        fn(x)
        print("сумма чисел",*x,"равна",fn(x))
        print("Среднее арифметическое чисел",*x,"равно",fn(x)/len(x))
    return wrap


@decor_f
def func(lst):
    return sum(lst)

func(2,3,3,4)

