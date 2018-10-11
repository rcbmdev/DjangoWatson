from django.shortcuts import render
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

# Create your views here.
def understanding(request):
    if request.method == 'POST':
        if request.POST['text'] != '':
            service = NaturalLanguageUnderstandingV1(
                version='2018-03-16',
                ## url is optional, and defaults to the URL below. Use the correct URL for your region.
                # url='https://gateway.watsonplatform.net/natural-language-understanding/api',
                username='2e37f4ae-1ee1-4fd4-a02a-796be1eb7f5a',
                password='4l00fMqeeoMz')
            text = request.POST['text']

            dados = service.analyze(
                text=text,
                features=Features(entities=EntitiesOptions(emotion=True, sentiment=True),
                                  keywords=KeywordsOptions(emotion=True,
                                                           sentiment=True))).get_result()

            keywords = dados['keywords']

            entities = dados['entities']

            sentiments = dados['keywords'][0]['sentiment']

            print(sentiments)

            emotions = dados['keywords'][0]['emotion']

            print(emotions)


            return render(request, 'understanding.html',{'text':text,'keywords':keywords, 'entities':entities,'sentiments':sentiments,'emotions':emotions})

    else:
        print('caiu no else')
        return render(request, 'understanding.html')





