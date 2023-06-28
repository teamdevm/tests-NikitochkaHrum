from django.db import models
from django.db import models
import hashlib

def calculate_file_hash(file_path):
    with open(file_path, 'rb') as f:
        hash_algorithm = hashlib.sha256()
        for chunk in iter(lambda: f.read(4096), b''):
            hash_algorithm.update(chunk)
    return hash_algorithm.hexdigest()

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=255)
    image = models.CharField(max_length=255, default='placeholder.png')
    image_hash = models.CharField(max_length=64, blank=True)

    def save(self, *args, **kwargs):
        if not self.image_hash:
            self.image_hash = calculate_file_hash(self.image)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'products'