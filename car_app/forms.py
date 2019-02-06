from django import forms
from car_app.models import TruckModel, TruckNumber, Post


class TruckModelForm(forms.ModelForm):
    class Meta:
        model =  TruckModel
        fields = ('model_name', 'max_capacity', 'model_description', )


class TruckNumberForm(forms.ModelForm):
    class Meta:
        model =  TruckNumber
        fields = ('bort_number', 'model_name', 'current_weight', 'truck_number_description', )
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        
        
        
        