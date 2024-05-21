from django.db import models

# Create your models here.



class Esrog(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='esrogim_images/')
    created_date = models.DateTimeField(auto_now_add=True)  
    size = models.IntegerField()
    price = models.IntegerField()
    


    def __str__(self):
        return f"{self.id = } - {self.description = } - {self.price = } - {self.size = } - {self.created_date = }"