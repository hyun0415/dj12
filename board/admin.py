from django.contrib import admin

# Register your models here.
from .models import Board, Reply
admin.site.register(Board)
admin.site.register(Reply)

