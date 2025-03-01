from django.db import models

from django.db import models

class Vendor(models.Model):
    CATEGORY_CHOICES = [
        ('Photography', 'Photography'),
        ('Venue Coordinator', 'Venue Coordinator'),
        ('Decor Coordinator', 'Decor Coordinator'),
        ('Beautician', 'Beautician'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=15) 
    mobile_no = models.CharField(max_length=15, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.category})"

class Service(models.Model):
    service_name = models.CharField(max_length=200)
    details = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="services")  # Added vendor_id

    def __str__(self):
        return self.service_name

class VendoraddShop(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)  # Establish relationship
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    image = models.ImageField(upload_to='vendor_images/')  # Store images
    year_in_business = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.year_in_business} years"
