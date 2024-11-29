import re

def format_name(name): #Fungsional [1]
    # (string manipulation) [2]
    return " ".join(word.capitalize() for word in name.split())

# RegEx [3]
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def calculate_salary_with_bonus(salary):
    # Conditional statement [4]
    if salary < 5000000:
        bonus = 0.10 * salary
    elif 5000000 <= salary <= 10000000:
        bonus = 0.05 * salary
    else:
        bonus = 0
    return salary + bonus

# looping [5]
def process_employees(employee_data):
    employees = []
    for data in employee_data:
        name, email, salary = data['nama'], data['email'], data['gaji']
        
        if not validate_email(email):
            print(f"Format email tidak valid untuk: {name}")
            continue
        
        formatted_name = format_name(name)
        
        final_salary = calculate_salary_with_bonus(salary)
        
        employees.append({
            'Nama': formatted_name,
            'Email': email,
            'Gaji Akhir': f'Rp{final_salary:,.0f}'
        })
    
    return employees

# Data Type Collections [6]
data_pegawai = [
    {"nama": "Mirna", "email": "mirna@gmail.com", "gaji": 4000000},
    {"nama": "talita", "email": "talita@gmail.", "gaji": 8000000},
    {"nama": "aisyah", "email": "aisyah@gmail.com", "gaji": 12000000},
]

processed_employees = process_employees(data_pegawai)
for employee in processed_employees:
    print(f"Nama: {employee['Nama']}, Email: {employee['Email']}, Gaji Akhir: {employee['Gaji Akhir']}")
