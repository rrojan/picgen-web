from random import choice
from django.http import JsonResponse
from django.utils import timezone
from .models import GeneratedPhoto, Photo


def photos(request):
    photos = GeneratedPhoto.objects.all().order_by('-created_at')
    data = [
        {
            'title': photo.title,
            'image': photo.image.url,
            'created_at': timezone.localtime(photo.created_at).strftime('%Y-%m-%d %H:%M:%S')
        }
        for photo in photos
    ]
    return JsonResponse(data, safe=False)


def random_photo(request):
    photos = Photo.objects.all()
    if photos:
        random_photo = choice(photos)
        # Add this generated photo to the list of generated photos
        GeneratedPhoto.build_from_photo(random_photo)
        created_at_gmt = timezone.localtime(random_photo.created_at).replace(
            tzinfo=timezone.timezone.utc
        ).astimezone(timezone.get_fixed_timezone(345))  # GMT+5:45
        data = {
            'title': random_photo.title,
            'image': random_photo.image.url,
            'created_at': created_at_gmt.strftime('%Y-%m-%d %H:%M:%S')
        }
    else:
        data = {}
    return JsonResponse(data)
