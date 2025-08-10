import os
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.exceptions import ValidationError


def validate_audio_file(file):
    """
    Verify audio file formats for .mp3, .aac, and .ogg
    """
    extension = os.path.splitext(file.name)[1].lower()
    valid_extensions = ['.mp3', '.aac', '.ogg']
    if extension not in valid_extensions:
        raise ValidationError(f'Unsupported audio file format. Allowed formats: [.mp3 | .aac | .ogg]')

    max_size = 200 #MegaBytes
    if file.size > max_size * 1024 * 1024:
        raise ValidationError(f'File too large. Maximum size allowed is {max_size} MB.')


class Sermon(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    preacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='sermons')
    description = models.TextField()
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='sermons/images/', blank=True, null=True)
    date_preached = models.DateField()
    share_count = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_sermons', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Creates a slug field from sermon title
        """
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Sermon.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def like_count(self):
        return self.likes.count()