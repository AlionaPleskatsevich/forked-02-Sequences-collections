employees = [
{"name": "Anna Petrova", "year": 2022, "salary": 2200},
{"name": "Ivan Sidorov", "year": 2021, "salary": 1500},
{"name": "Petr Ivanov", "year": 2020, "salary": 1200},
{"name": "Ivan Sidorov", "year": 2022, "salary": 1700},
{"name": "Olga Smirnova", "year": 2023, "salary": 2800},
{"name": "Anna Petrova", "year": 2023, "salary": 2500},
{"name": "Petr Ivanov", "year": 2021, "salary": 1300},
{"name": "Ivan Sidorov", "year": 2023, "salary": 1900},
{"name": "Petr Ivanov", "year": 2022, "salary": 1350},
{"name": "Petr Ivanov", "year": 2023, "salary": 1400}
]

emp = {}
for person in employees:
    name = person["name"]
    salary = person["salary"]
    if name in emp:
     emp[name].append(person["salary"])
    else:
       emp[name] = [salary]
print(emp) #получился словарь, в котором для ключа есть список значений
#avg_salary = {} тут планируется словарь, где ключ:значение - это имя:средняя зп
#я понимаю, что нужно для каждого значения=списка найти среднее значение, но не понимаю, как к списку обратиться
#print(avg_salary) тут был бы вывод словаря