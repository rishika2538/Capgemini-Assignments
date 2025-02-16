salary=float(input("Enter Salary:"))
allowances=float(input("Enter allowances:"))

gross_salary=salary+allowances
if gross_salary<500000:
    tax_r=0.10
else:
    tax_r=0.20
tax=gross_salary+tax_r
net=gross_salary-tax
print(f'Gross salary:{gross_salary}')
print(f'Tax:{tax}')
print(f'Net Salary:{net}')
print(f'Allowances:{allowances}')