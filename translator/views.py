from django.shortcuts import render
import json
from watson_developer_cloud import LanguageTranslatorV3

API_KEY = ''

# Create your views here.
def translator(request):
    if request.method == 'POST':
        if request.POST['text']:
            language_translator = LanguageTranslatorV3(
                version='2018-05-01',
                ### url is optional, and defaults to the URL below. Use the correct URL for your region.
                # url='https://gateway.watsonplatform.net/language-translator/api',
                iam_apikey=API_KEY)

            texto = request.POST['text']
            opcao = request.POST['optradio']

            translation = language_translator.translate(
                text=texto,
                model_id=opcao).get_result()

            translate = translation['translations'][0]['translation']
            word_count = translation['word_count']

            return render(request, 'translate.html', {'texto':texto,'translate':translate, 'word_count':word_count})
    else:
        return render(request, 'translate.html')



