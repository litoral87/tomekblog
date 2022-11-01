from django.contrib import admin

# Register your models here.
#importujemy modele z klasy POST - którą sobie utworzyliśmy
from .models import Post

#rejestrujemy model z klasy post - uwaga te zmianysda
admin.site.register(Post)

