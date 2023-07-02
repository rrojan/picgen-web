from random import choice
from django.http import JsonResponse
from .models import GeneratedPhoto, Photo


def photos(request):
    photos = GeneratedPhoto.objects.all()
    data = [{'title': photo.title, 'image': photo.image.url}
            for photo in photos]
    return JsonResponse(data, safe=False)


def random_photo(request):
    photos = Photo.objects.all()
    if photos:
        random_photo = choice(photos)
        # Add this generated photo to list of generated photos
        GeneratedPhoto.build_from_photo(random_photo)
        data = {
            'title': random_photo.title,
            'image': random_photo.image.url,
        }
    else:
        data = {}
    return JsonResponse(data)
