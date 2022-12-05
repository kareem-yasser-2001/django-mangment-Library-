from django.db import models
class Category (models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Book (models.Model):
    status_books =[
        ('avalible','avalible'),
        ('rental','rental'),
        ('sold','sold'),
    ]

    title = models.CharField( max_length=50)
    author = models.CharField( max_length=250)
    phtoto_book = models.ImageField(upload_to='photo',null=True , blank = True)
    phtoto_author = models.ImageField(upload_to='photo',null=True , blank = True)
    pages = models.IntegerField(null = True , blank = True)
    prices = models.DecimalField(max_digits=5, decimal_places=2,null = True , blank = True)
    retal_price_day = models.DecimalField(max_digits=5, decimal_places=2,null = True , blank = True)
    retal_period = models.IntegerField(null = True , blank = True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2,null = True , blank = True)  
    active = models.BooleanField(default = True)
    status = models.CharField(max_length=50,choices=status_books,null = True , blank = True )
    category = models.ForeignKey(Category, on_delete=models.PROTECT,null = True , blank = True)
    def __str__(self):
         return self.title

 