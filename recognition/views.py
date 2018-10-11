from django.shortcuts import render
from watson_developer_cloud import VisualRecognitionV3
import json
from django.core.files.storage import FileSystemStorage

# Create your views here.
def detecta_faces(request):
    if request.method == 'POST':
        if request.FILES['image']:
            visual_recognition = VisualRecognitionV3(
                '2018-03-19',
                iam_apikey='IwxurU5UCEPJS1UO13iQNAlyZl0s4sNBfYj6zIsWIV2k')
            image = request.FILES['image']
            faces = visual_recognition.detect_faces(image).get_result()
            json_data = json.dumps(faces, indent=2)
            novas_faces = json.loads(json_data)
            #print(json_data)
            facesEncontradas = len(novas_faces['images'][0]['faces'])


            '''
            for face in (faces['images'][0]['faces']):
                #print(face['face_location'])
                #new_image = dr.rectangle(((face['face_location']['height'], face['face_location']['width']), (face['face_location']['left'], face['face_location']['top'])), fill="black", outline="blue")
                idade["idadeMin"] = face['age']['min']
                idade["idadeMax"] = face['age']['max']
                #print(face['gender']['gender'])
                print(idade)
                #media_idade = mean([int(x) for x in idade.values()])
                #print(media_idade)
                # Tentar pegar a media das idades
                sexo["sexo"] = face['gender']['gender']
                if sexo["sexo"] == 'MALE':
                    sexo["sexo"] = 'Masculino'
                else:
                    sexo["sexo"] = 'Feminino'
                #print(sexo)
                #print(len(idade))

            '''
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
            return render(request, 'detecta_faces.html',
                          {'uploaded_file_url': uploaded_file_url,
                           'facesEncontradas':facesEncontradas,
                           'faces':novas_faces['images'][0]['faces']
                           })
    else:
        return render(request, 'detecta_faces.html')

def detecta_objetos(request):
    if request.method == 'POST':
        if request.FILES['image']:
            visual_recognition = VisualRecognitionV3(
                '2018-03-19',
                iam_apikey='IwxurU5UCEPJS1UO13iQNAlyZl0s4sNBfYj6zIsWIV2k')
            image = request.FILES['image']
            car_results = visual_recognition.classify(
                images_file=image,
                threshold='0.1',
                classifier_ids=['default']).get_result()
            json_data = json.dumps(car_results, indent=2)
            news_objects = json.loads(json_data)

            #print(news_objects['images'][0]['classifiers'])


            #objetos = (object['classes'] for object in (news_objects['images'][0]['classifiers']) )
            #print(objetos)
            #for objeto in car_results['images'][0]['classifiers'][0]['classes']:
            #    print(objeto)





            #print(getattr(news_objects, "classes"))

            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
            return render(request, 'detecta_objetos.html',
                          {'uploaded_file_url': uploaded_file_url,
                           'objetos': news_objects['images'][0]['classifiers'][0]['classes'],
                           #'faces': novas_faces['images'][0]['faces']
                           })
    else:
        return render(request, 'detecta_objetos.html')


