# Лабораторная работа № 4
## Задание №1
	Нужно было создать замыкание для накопления всех аргументов в коллекции, а при получении определённого значения - возврат и очистка коллекции.

Создал замыкание для накопления аргументов с списком внутри и сделал проверку на наличие стоп-слова.

![alt text](screen/image20250311103405.png)
## Задание №2
В нем нужно было создать декоратор для валидации аргументов функции с помощью условий:

```python
@validate(lambda x: x > 0, lambda y: isinstance(y, str))
def my_function(x, y):
    pass
```