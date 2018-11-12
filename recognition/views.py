from django.shortcuts import render
from watson_developer_cloud import VisualRecognitionV3
import json
from django.core.files.storage import FileSystemStorage

#API KEY Visual Recognition
API_KEY=''

# Create your views here.
def detecta_faces(request):
    if request.method == 'POST':
        if request.FILES['image']:
            visual_recognition = VisualRecognitionV3(
                '2018-03-19',
                iam_apikey=API_KEY)
            image = request.FILES['image']
            faces = visual_recognition.detect_faces(image).get_result()
            json_data = json.dumps(faces, indent=2)
            novas_faces = json.loads(json_data)
            facesEncontradas = len(novas_faces['images'][0]['faces'])

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
                iam_apikey=API_KEY)
            image = request.FILES['image']
            car_results = visual_recognition.classify(
                images_file=image,
                threshold='0.1',
                classifier_ids=['default']).get_result()
            json_data = json.dumps(car_results, indent=2)
            news_objects = json.loads(json_data)

            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
            return render(request, 'detecta_objetos.html',
                          {'uploaded_file_url': uploaded_file_url,
                           'objetos': news_objects['images'][0]['classifiers'][0]['classes'],
                           })
    else:
        return render(request, 'detecta_objetos.html')


