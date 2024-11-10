values_list = [21.04, False, "Карбюратор"]
values_list_2 = ["Сдал на мотоцикл", 11.09]
values_dict = {"a": "Инжектор", "b": 2012, "c": True}

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print("ЗМЗ 406")
print("ЗМЗ 406", 8)
print("ЗМЗ 406", True, "V8")
print()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)