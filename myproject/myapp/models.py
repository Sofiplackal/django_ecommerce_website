from django.db import models


# Product model
class Products(models.Model):
    product_image = models.ImageField(upload_to='products')
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()


# Working model
class Working(models.Model):
    working_image = models.ImageField(upload_to='working_images')
    working_name = models.CharField(max_length=100)
    working_description = models.TextField()


# Hoodie model
class Hhoodie(models.Model):
    hoodie_name = models.CharField(max_length=100)
    hoodie_price = models.DecimalField(max_digits=6, decimal_places=2)
    hoodie_description = models.TextField()
    hoodie_image = models.ImageField(upload_to='hoodies')
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.hoodie_name


# Hoodie color options
class HoodieColorOption(models.Model):
    hoodie = models.ForeignKey(Hhoodie, related_name='color_options', on_delete=models.CASCADE)
    color_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=7)  # e.g., "#000000"
    color_image = models.ImageField(upload_to='hoodies/colors/', blank=True, null=True)

    def __str__(self):
        return f"{self.color_name} ({self.color_code})"











