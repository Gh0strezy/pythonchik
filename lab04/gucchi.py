def validate(condition1, condition2):
    def decorator(func):
        def wrapper(args1, args2):
            if condition1(args1) or condition2(args2):
                print("Условие выполнено, запуск функции")
                return func(args1, args2)
            else:
                print("Условие не выполнено, функция не выполнится")
                return args1 * args2
        return wrapper
    return decorator

def set_collector(reset_value):
    storage = []
    def collector(*args):
        nonlocal storage
        if args and args[0] is reset_value:
            result = storage.copy()
            storage.clear()
            return result
        storage.extend(args)
        return None
    return collector


collector = set_collector("Стоп")
collector(1, 2,)
collector(3, 4)
print(collector("Стоп"))
print(collector("Стоп"))
collector(5, 6, 7)
print(collector("Стоп"))
print(collector("Стоп"))



# @validate(lambda x: x > 0, lambda y: isinstance(y, str))
# def my_func(x, y):
#     pass

# print(my_func(-5, 3))
# print(my_func(-3, "ZXC"))
# print(my_func(5, "ZXC"))
# print(my_func(5, 5))


<<<<<<< HEAD
def my_dec(x=lambda x: x <= 1024):
=======
@validate(lambda x: x > 0, lambda y: isinstance(y, str))
def my_func(x, y):
    pass
print(my_func(-5, 3))
print(my_func(-3, "ZXC"))
print(my_func(5, "ZXC"))
print(my_func(5, 5))


def my_dec(x):
>>>>>>> 7f9b7807a071d6406bf82a98b70493164f98abb5
    cnt = 0
    def decorator1(func):
        def wrapper(args):
            result = func(args)
            nonlocal cnt
            if x(result):
                print(f"Результат вычисления 2 в {args} степени равен или больше 1024, а точнее {result}")
            else:
                print(f"Результат вычисления 2 в {args} степени не равен 1024, а равен {result}")
            return result
        return wrapper
    return decorator1


@my_dec(x= lambda x: x <= 2048)
def my_func2(x):
    if x == 0:
        return 1
    else:
        return 2 * my_func2(x - 1)
print(my_func2(12))
