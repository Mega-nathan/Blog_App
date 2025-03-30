from django.db import models


class blog(models.Model):
    category_choices=[
        ('Tech','Tech'),
        ('Lifestyle','Lifestyle'),
        ('business','business'),
        ('Foods','Foods'),
    ]
    thumbnail=models.ImageField(upload_to='thumbnails/',blank=True)
    userName=models.CharField(max_length=30)
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.CharField(max_length=20,choices=category_choices,default=category_choices[0])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="all_blogs"


