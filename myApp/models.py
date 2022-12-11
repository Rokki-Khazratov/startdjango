from django.db import models
from django.urls import reverse
from django.core import serializers
import json





# sting ↓
def __str__(self):
   return self.title
   
# auto slug ↓
def get_absolute_url(self):
   return reverse('component:login', kwargs = {'slug' : self.slug})