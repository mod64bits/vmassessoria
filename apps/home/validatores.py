from django.core.exceptions import ValidationError

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageValidator(object):
    messages = {
        "dimensions": (
            'Allowed dimensions are: %(width)s x %(height)s.'
        ),
        "size": (
            "File is larger than > %(size)skB."
        )
    }

    def __init__(self, size=None, width=None, height=None, messages=None):
        self.size = size
        self.width = width
        self.height = height
        if messages is not None and isinstance(messages, Mapping):
            self.messages = messages

    def __call__(self, value):
        # _get_image_dimensions is a method of ImageFile
        # https://docs.djangoproject.com/en/1.11/_modules/django/core/files/images/
        if self.size is not None and value.size > self.size:
            raise ValidationError(
                self.messages['size'],
                code='invalid_size',
                params={
                    'size': float(self.size)/1024,
                    'value': value,
                }
            )
        if (self.width is not None and self.height is not None and
                (value.width != self.width or value.height != self.height)):
            raise ValidationError(
                self.messages['dimensions'],
                code='invalid_dimensions',
                params={
                    'width': self.width,
                    'height': self.height,
                    'value': value,
                }
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.size == other.size and
            self.width == other.width and
            self.height == other.height
        )