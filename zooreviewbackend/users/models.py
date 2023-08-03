from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model): 
    first_name = models.CharField(max_length=20)
    last_name =  models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8, 'the field must contain at least 8 characters')
        ]
    )
    bio = models.CharField(max_length=200)
    avatar = models.CharField(max_length=1000)
    random_string = models.CharField(max_length=1000) # browser cookie
    verified = models.BooleanField()
    # liked_blogs = models.JSONField() # ArrayField would work w/ PostgreSQL database
    # disliked_blogs = models.JSONField() 
