from django.db import models
from django.contrib.gis.db import models as gis_models
from accounts.models import User
class Points(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = 'NEW', 'New'
        OLD = 'OLD', 'Old'
    
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField();
    image_name = models.CharField(max_length=255 , unique=True)
    image = models.ImageField(
        upload_to='media/locations/image',
        default='media/locations/image/blank.jpg',
        blank=True,
        null=True
    )
    audio = models.FileField(upload_to='media/locations/audio',blank=True,null=True)
    video = models.FileField(upload_to='media/locations/video',blank=True,null=True)
    geom = gis_models.PointField()
    point_type = models.CharField(
        max_length=3,
        choices=StatusChoices.choices,
        default=StatusChoices.NEW
    )
    custom_fields = models.JSONField(default=dict, blank=True)
    
    #synce_status = models.BooleanField(default=False)
    #inside_polygon = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


