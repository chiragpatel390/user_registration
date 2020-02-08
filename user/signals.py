from django.db.models.signals import pre_save
from django.dispatch import receiver
from user.models import File
from urllib.parse import urlencode
from urllib.request import urlopen
import contextlib


@receiver(pre_save, sender=File)
def add_compressed_url(sender, instance, **kwargs):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': instance.url}))
    with contextlib.closing(urlopen(request_url)) as response:
        instance.compressed_url = response.read().decode('utf-8 ')
