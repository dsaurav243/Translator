from django.shortcuts import render
from .forms import InputForm
# Create your views here.
from google_trans_new import google_translator
context = {}
def home(request):

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            src_lang = form.cleaned_data['src_lang']
            tgt_lang = form.cleaned_data['tgt_lang']
            translator = google_translator()
            result = translator.translate(text= text, lang_src= src_lang, lang_tgt= tgt_lang)
            form = InputForm()
            context['form'] = form
            context['text'] = text
            context['result'] = result
            return render(request, 'testapp/home.html', context)


    form = InputForm()
    return render(request,'testapp/home.html',{'form':form})
