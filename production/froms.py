from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title       = forms.CharField(label="Title", widget= forms.TextInput(attrs={"placeholder":"Your Title"})) 
    #, widget= forms.TextInput(attrs= {"placeholder":"Your Title"})
    description = forms.CharField(required= False, 
    widget=forms.Textarea(
        attrs={
            "placeholder":"Your Description",
            "class":"new class two",
            "id":"my-id",
            "rows":"20",
            "cols":"20"
        })) #default reqired is true
    price       = forms.IntegerField(initial=99)
    class Meta:
        model= Product
        fields={
            "title",
            "description",
            "price"
        }
    
    def clean_title(self,*args,**kwargs):
        title= self.cleaned_data.get("title")
        if "Ali" in title:
            raise forms.ValidationError("this is not a valid title")
        else:
            return title



class RawProductForm(forms.Form):
   
    title       = forms.CharField(label="Title", widget= forms.TextInput(attrs={"placeholder":"Your Title"})) 
    #, widget= forms.TextInput(attrs= {"placeholder":"Your Title"})
    description = forms.CharField(required= False, 
    widget=forms.Textarea(
        attrs={
            "placeholder":"Your Description",
            "class":"new class two",
            "id":"my-id",
            "rows":"20",
            "cols":"20"
        })) #default reqired is true
    price       = forms.IntegerField(initial=99)
