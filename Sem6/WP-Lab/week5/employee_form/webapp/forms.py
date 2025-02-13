from django import forms
EMPLOYEE_IDS = [
    ('101', 'Employee 101'),
    ('102', 'Employee 102'),
    ('103', 'Employee 103'),
    ('104', 'Employee 104'),
]

class EmployeeForm(forms.Form):
    employee_id = forms.ChoiceField(label="Employee ID", choices=EMPLOYEE_IDS)
    doj = forms.CharField(label="Date of Joining", max_length=100)

