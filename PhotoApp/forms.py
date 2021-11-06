from .models import Photo
from django import forms


cat =(
    ("Food", "Food"),
    ("Love", "Love"),
    ("Nature", "Nature"),
    ("Music", "Music"),
)

vis=(
    ("Public", "Public"),
    ("Private", "Private"),

)

class Photoforms(forms.ModelForm):
    # cate = forms.ModelChoiceField(queryset=Category.objects.all())

    Title = forms.CharField(max_length=30, required=False, help_text='Optional.')
    Location = forms.CharField(max_length=30, required=False, help_text='Optional.')
    Image = forms.ImageField(required=False, help_text='Optional.')
    Description = forms.Textarea()
    Category = forms.ChoiceField(choices=cat)
    Visibility= forms.ChoiceField(choices = vis)

    class Meta:
        model = Photo
        fields = ['Title', 'Location','Image','Category', 'Visibility' , 'Description']
