from django import forms
from .models import *

class BookForm(forms.ModelForm):
     class Meta:
        model = Book
        fields = [
         'title',
         'author',
         'phtoto_book',
         'phtoto_author',
         'pages',
         'prices',
         'retal_price_day',
         'retal_period',
         'total_rental',
         'status',
         'category',
         
         
        ]
        widgets = {
          'title': forms.TextInput(attrs={'class':'form-control'}),
          'author': forms.TextInput(attrs={'class':'form-control'}),
          'pages': forms.NumberInput(attrs={'class':'form-control'}),
          'prices': forms.NumberInput(attrs={'class':'form-control'}),
          'retal_price_day': forms.NumberInput(attrs={'class':'form-control','id':'rentalprice'}),
          'retal_period': forms.NumberInput(attrs={'class':'form-control','id':'rentaltime'}),
          'total_rental':forms.NumberInput(attrs={'class':'form-control','id':'rentaltotal'}),
          'status': forms.Select(attrs={'class':'form-control'}),
          'category': forms.Select(attrs={'class':'form-control'}),
          'phtoto_book': forms.FileInput(attrs={'class':'form-control'}),
          'phtoto_author': forms.FileInput(attrs={'class':'form-control'}) ,     
        }



class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
          'name': forms.TextInput(attrs={'class':'form-control', 'title': 'Search'})
        }

       
    
