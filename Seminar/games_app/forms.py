from django import forms


class Games(forms.Form):
    name = forms.ChoiceField(choices=[('E', 'Eagle'),
                                      ('C', 'Cub'),
                                      ('N', 'Number')
                                      ])
    count = forms.IntegerField(min_value=1, max_value=64)
