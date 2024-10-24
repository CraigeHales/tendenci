from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = ('Caches the photo for the size on the batch edit page and the photoset view page.')

    def add_arguments(self, parser):
        parser.add_argument('photo_id', type=int)

    def handle(self, photo_id, **options):
        # wch from tendenci.apps.photos.utils.caching import cache_photo_size
        from addons.forestHome.templatetags.foresthome_filters import cache_photo_size

        cache_kwargs_list = []
        cache_kwargs_list.append({"id": photo_id, "directory": "photos", "quality": 54, "size": "422x700", "constrain": True})
        cache_kwargs_list.append({"id": photo_id, "directory": "photos", "quality": 54, "size": "102x78", "crop": True})
        cache_kwargs_list.append({"id": photo_id, "directory": "photos", "quality": 54, "size": "640x640", "constrain": True})

        for cache_kwargs in cache_kwargs_list:
            # pic.pk, "photos", "200x200", crop=True, quality=40, download=False, constrain=False
            # id, directory, size, crop=False, quality=90, download=False, constrain=False
            cache_photo_size(**cache_kwargs)
