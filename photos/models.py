from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'pics/', null = True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null='True', blank=True)
    location = models.ForeignKey('Location', on_delete=models.PROTECT, null='True', blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()   

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)       