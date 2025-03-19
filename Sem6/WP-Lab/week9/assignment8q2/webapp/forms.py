from django import forms

class FeedbackForm(forms.Form):
    student_name = forms.CharField(label="Student Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    gender = forms.ChoiceField(label="Sex", choices=GENDER_CHOICES, widget=forms.RadioSelect)
    
    COURSE_CHOICES = [
        ('ASP-XML', 'ASP-XML'),
        ('DotNET', 'DotNET'),
        ('JavaPro', 'JavaPro'),
        ('Unix,C,C++', 'Unix,C,C++')
    ]
    course = forms.ChoiceField(label="Select Course", choices=COURSE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    
    TECHNICAL_COVERAGE_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Poor', 'Poor')
    ]
    technical_coverage = forms.ChoiceField(label="Technical Coverage", choices=TECHNICAL_COVERAGE_CHOICES, widget=forms.RadioSelect)
    
    suggestions = forms.CharField(label="Suggestions", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
