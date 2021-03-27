from django import forms
import googletrans
language_choices = googletrans.LANGUAGES

l = []
for key,value in language_choices.items():
    tup = (key,value)
    l.append(tup)

class InputForm(forms.Form):
    text =  forms.CharField(max_length=500)
    src_lang =  forms.ChoiceField(choices= l)
    tgt_lang = forms.ChoiceField(choices= l)