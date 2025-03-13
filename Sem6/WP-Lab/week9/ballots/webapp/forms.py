from django import forms

class VoteForm(forms.Form):
    CHOICE_OPTIONS = [
        ('Good', 'Good'),
        ('Satisfactory', 'Satisfactory'),
        ('Bad', 'Bad'),
    ]
    choice = forms.ChoiceField(choices=CHOICE_OPTIONS, widget=forms.RadioSelect)
