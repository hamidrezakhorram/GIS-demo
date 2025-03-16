from django.db import models

class Layer(models.Model):
    class FileTypeChoices(models.TextChoices):
        Polyline = 'Polyline'
        Polygon = 'Polygon'
    name = models.CharField(max_length=255)
    layer_type = models.CharField(max_length=255, choices=FileTypeChoices.choices)
    file = models.FileField(upload_to='media/layers/file', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    label_enabled = models.BooleanField(default=False)
    #user

    def __str__(self):
        return self.name


