
def sort_by_salary(data):
    return sorted(data, key=lambda x: x[2])

Data = [[101,"Seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,"Suresh",35000]]

sorted_data = sort_by_salary(Data)

for emp in sorted_data:
    print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}")
