employees = {
    101: {"name": "Rahul", "department": "IT", "salary": 45000, "attendance": 20},
    102: {"name": "Priya", "department": "HR", "salary": 55000, "attendance": 22},
    103: {"name": "Amit", "department": "IT", "salary": 30000, "attendance": 18},
    104: {"name": "Smeeta", "department": "Finance", "salary": 60000, "attendance": 21},
    105: {"name": "Niraj", "department": "HR", "salary": 25000, "attendance": 22}
}
# ==================================================
# 1. Calculate Net Salary and Salary Bands
# ==================================================

payslips = {}

for emp_id, details in employees.items():

    gross_salary = details["salary"]
    attendance = details["attendance"]

    deductions = 0

    if attendance < 22:
        absent_days = 22 - attendance
        deductions = absent_days * 500

    net_salary = gross_salary - deductions

    # Salary Band
    if gross_salary < 20000:
        band = "Junior"

    elif gross_salary <= 50000:
        band = "Mid"

    else:
        band = "Senior"

    payslips[emp_id] = {
        "name": details["name"],
        "gross": gross_salary,
        "deductions": deductions,
        "net": net_salary,
        "band": band
    }

# ==================================================
# 2. Find Highest Paying Department
# ==================================================

department_salary = {}

for emp_id, details in employees.items():

    dept = details["department"]
    salary = details["salary"]

    if dept not in department_salary:
        department_salary[dept] = []

    department_salary[dept].append(salary)

highest_department = ""
highest_avg = 0

for dept, salaries in department_salary.items():

    avg_salary = sum(salaries) / len(salaries)

    print(f"{dept} Average Salary = {avg_salary}")

    if avg_salary > highest_avg:
        highest_avg = avg_salary
        highest_department = dept

print("\nHighest Paying Department:", highest_department)
print("Average Salary:", highest_avg)

# ==================================================
# 3. Transfer Employee 103
#    IT -> Finance
# ==================================================

employees[103].update({
    "department": "Finance"
})

print("\nEmployee 103 transferred to Finance")

# ==================================================
# 4. Fire Employee 105 using del
# ==================================================

del employees[105]

print("Employee 105 removed")

# ==================================================
# 5. Promote Employee 101
#    Salary +10000
# ==================================================

employees[101].update({
    "salary": employees[101]["salary"] + 10000
})

print("Employee 101 promoted")

# ==================================================
# 6. Example of pop()
#    Remove and show attendance
# ==================================================

removed_attendance = employees[104].pop("attendance")

print("Attendance popped from Smeeta:", removed_attendance)

# Restoring it back
employees[104]["attendance"] = removed_attendance

# ==================================================
# 7. Generate Final Payslips
# ==================================================

print("\nFINAL PAYSLIPS\n")

for emp_id, details in employees.items():

    gross_salary = details["salary"]
    attendance = details["attendance"]

    deductions = 0

    if attendance < 22:
        deductions = (22 - attendance) * 500

    net_salary = gross_salary - deductions

    if gross_salary < 20000:
        band = "Junior"

    elif gross_salary <= 50000:
        band = "Mid"

    else:
        band = "Senior"

    final_payslip = {
        "name": details["name"],
        "gross": gross_salary,
        "deductions": deductions,
        "net": net_salary,
        "band": band
    }

    print(f"Employee ID: {emp_id}")
    print(final_payslip)
    print("-" * 40)

