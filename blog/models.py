from django.db import models


class PostBlog(models.Model):
    caption = models.CharField(unique=True,max_length=300,) 
    img  = models.ImageField(upload_to='static/media/blog')
    des = models.CharField(max_length=600)
    
    def __str__(self):
        return self.caption
    
class TechnologyPost(models.Model):
    caption = models.CharField(unique=True,max_length=300,) 
    img  = models.ImageField(upload_to='static/media/tech')
    des = models.CharField(max_length=600)
    
    def __str__(self):
        return self.caption
class DesignPost(models.Model):
    caption = models.CharField(unique=True,max_length=300,) 
    img  = models.ImageField(upload_to='static/media/')
    des = models.CharField(max_length=600)
    
    def __str__(self):
        return self.caption
class ProgrammingPost(models.Model):
    caption = models.CharField(unique=True,max_length=300,) 
    img  = models.ImageField(upload_to='static/media/blog')
    des = models.CharField(max_length=600)
    
    def __str__(self):
        return self.caption
class LifestylePost(models.Model):
    caption = models.CharField(unique=True,max_length=300,) 
    img  = models.ImageField(upload_to='static/media/blog')
    des = models.CharField(max_length=600)
    
    def __str__(self):
        return self.caption