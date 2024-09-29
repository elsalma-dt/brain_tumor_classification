from django.shortcuts import render
import os
import cv2
import numpy as np
import tensorflow
from keras.models import load_model
from django.http import JsonResponse


def home(request):
    return render(request, 'home.html')

def classify_image(request):
    try:
        if request.method == 'POST' and request.FILES['image']:
            # Check that the file extension is allowed
            image_file = request.FILES['image']
            ext = os.path.splitext(image_file.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png', '.dcm']:
                raise ValueError('Invalid file extension')

            # Load the image
            image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
            image = cv2.resize(image, (128, 128))
            image = np.expand_dims(image, axis=0)
            image = image.astype('float32') / 255

            # Load the trained CNN model
            model = load_model('project2\mymodels\model.h5')

            # Classify the image using the model
            predictions = model.predict(image)
            class_index = np.argmax(predictions[0])
            class_labels = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor'] 
            class_name = class_labels[class_index]
            response_data = {'class_name': class_name}
            return JsonResponse(response_data)

        else:
            return render(request, 'style.html')

    except KeyError:
        response_data = {'error': 'No image file found'}
        return JsonResponse(response_data, status=400)

    except ValueError as e:
        response_data = {'error': str(e)}
        return JsonResponse(response_data, status=400)

    except Exception as e:
        response_data = {'error': str(e)}
        return JsonResponse(response_data, status=500)
   





