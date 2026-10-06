#В компании хранятся данные о зарплатах сотрудников за разные годы. Некоторые сотрудники работают в компании дольше других, поэтому количество записей для каждого сотрудника может отличаться.
#Необходимо:
#Посчитать среднюю зарплату для каждого сотрудника.

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
#print(emp) 
for el in emp:
   salaries = emp[el]
   avg_salary = sum(salaries)/len(salaries)
   print(f"{el}:{avg_salary}")