from django.db import models

# Create your models here.

class Plant(models.Model):

    CATEGORY_CHOICES = [
        ('Tree', 'tree'),
        ('Fruit', 'fruit'),
        ('Vegetables', 'vegetables'),
        ('other', 'other'),
    ]
    name = models.CharField(max_length=20)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="other")
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
