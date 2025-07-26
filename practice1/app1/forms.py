from django import forms

# class Model1Form(forms.ModelForm):
#     class Meta:
#         model = Model1
#         fields = ['name', 'description']

# class Model2Form(forms.ModelForm):
#     class Meta:
#         model = Model2
#         fields = ['model1', 'title', 'content']

# class Model3Form(forms.ModelForm):
#     class Meta:
#         model = Model3
#         fields = ['model1', 'additional_info']

class VictimForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    contact_number = forms.CharField()

class IncidentForm(forms.Form):
    incident_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    location = forms.CharField()
    is_electronic = forms.BooleanField(required=False)
    electronic_medium = forms.CharField(required=False)

class PerpetratorForm(forms.Form):
    name = forms.CharField()
    relationship = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)