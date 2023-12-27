employees = [
{
'id': 1,
'name': 'Alice',
'basic_salary': 50000,
'TA': 3000,
'DA': 4000,
'HRA': 2000,
'bonus': 3000,
'experience_years': 3,
},
{
'id': 2,
'name': 'Bob',
'basic_salary': 55000,
'TA': 3500,
'DA': 4500,
'HRA': 2500,
'bonus': 0,
'experience_years': 1,
},
{
'id': 3,
'name': 'Charlie',
'basic_salary': 60000,
'TA': 3800,
'DA': 4800,
'HRA': 2600,
'bonus': 0,
'experience_years': 4,
},
{
'id': 4,
'name': 'David',
'basic_salary': 52000,
'TA': 3200,
'DA': 4200,
'HRA': 2100,
'bonus': 0,
'experience_years': 2,
},
{
'id': 5,
'name': 'Eva',
'basic_salary': 58000,
'TA': 4000,
'DA': 5000,
'HRA': 2700,
'bonus': 3500,
'experience_years': 5,
},
]
# A) Display all employee names and their net salaries
def calculate_net_salary(employee):
    if employee['experience_years'] >= 2:
        bonus = employee['bonus']
    else:
        bonus = 0
    net_salary = employee['basic_salary'] + employee['TA'] + employee['DA'] +employee['HRA'] + bonus
    return net_salary
print("A) Employee names and their net salaries:")
for employee in employees:
    net_salary = calculate_net_salary(employee)
    print(f"{employee['name']}: {net_salary}")
# B) Display employee name with the highest & lowest salary
sorted_employees = sorted(employees, key=lambda x: calculate_net_salary(x))
highest_salary_employee = sorted_employees[-1]
lowest_salary_employee = sorted_employees[0]
print("\nB) Employee with the highest salary:")
print(f"Name: {highest_salary_employee['name']}")
print(f"Salary: {calculate_net_salary(highest_salary_employee)}")
print("\nEmployee with the lowest salary:")
print(f"Name: {lowest_salary_employee['name']}")
print(f"Salary: {calculate_net_salary(lowest_salary_employee)}")
# C) Display the average salary
total_salary = sum(calculate_net_salary(employee) for employee in employees)
average_salary = total_salary / len(employees)
print("\nC) Average salary:", average_salary)
