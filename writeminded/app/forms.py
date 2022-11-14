from django import forms
from app.models import uploadfilemodel

# for upload file
class uploadfileform(forms.ModelForm):
    class Meta:
        model = uploadfilemodel
        fields = "__all__"