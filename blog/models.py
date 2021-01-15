from django.db import models

class BlogPostDB(models.Model):
	title 			=	models.CharField(max_length=100, null=False)
	date			=	models.DateField(auto_now=False, auto_now_add=False)
	author			=	models.CharField(max_length=100, null=False)

