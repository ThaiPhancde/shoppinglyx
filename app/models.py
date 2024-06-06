from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
  ('An Giang', 'An Giang'),
  ('Bà Rịa - Vũng Tàu', 'Ba Ria - Vung Tau'),
  ('Bắc Giang', 'Bac Giang'),
  ('Bắc Kạn', 'Bac Kan'),
  ('Bạc Liêu', 'Bac Lieu'),
  ('Bắc Ninh', 'Bac Ninh'),
  ('Bến Tre', 'Ben Tre'),
  ('Bình Định', 'Binh Dinh'),
  ('Bình Dương', 'Binh Duong'),
  ('Bình Phước', 'Binh Phuoc'),
  ('Bình Thuận', 'Binh Thuan'),
  ('Cà Mau', 'Ca Mau'),
  ('Cao Bằng', 'Cao Bang'),
  ('Đắk Lắk', 'Dak Lak'),
  ('Đắk Nông', 'Dak Nong'),
  ('Điện Biên', 'Dien Bien'),
  ('Đồng Nai', 'Dong Nai'),
  ('Đồng Tháp', 'Dong Thap'),
  ('Gia Lai', 'Gia Lai'),
  ('Hà Giang', 'Ha Giang'),
  ('Hà Nam', 'Ha Nam'),
  ('Hà Tĩnh', 'Ha Tinh'),
  ('Hải Dương', 'Hai Duong'),
  ('Hậu Giang', 'Hau Giang'),
  ('Hòa Bình', 'Hoa Binh'),
  ('Hưng Yên', 'Hung Yen'),
  ('Khánh Hòa', 'Khanh Hoa'),
  ('Kiên Giang', 'Kien Giang'),
  ('Kon Tum', 'Kon Tum'),
  ('Lai Châu', 'Lai Chau'),
  ('Lâm Đồng', 'Lam Dong'),
  ('Lạng Sơn', 'Lang Son'),
  ('Lào Cai', 'Lao Cai'),
  ('Long An', 'Long An'),
  ('Nam Định', 'Nam Dinh'),
  ('Nghệ An', 'Nghe An'),
  ('Ninh Bình', 'Ninh Binh'),
  ('Ninh Thuận', 'Ninh Thuan'),
  ('Phú Thọ', 'Phu Tho'),
  ('Quảng Bình', 'Quang Binh'),
  ('Quảng Nam', 'Quang Nam'),
  ('Quảng Ngãi', 'Quang Ngai'),
  ('Quảng Ninh', 'Quang Ninh'),
  ('Quảng Trị', 'Quang Tri'),
  ('Sóc Trăng', 'Soc Trang'),
  ('Sơn La', 'Son La'),
  ('Tây Ninh', 'Tay Ninh'),
  ('Thái Bình', 'Thai Binh'),
  ('Thái Nguyên', 'Thai Nguyen'),
  ('Thanh Hóa', 'Thanh Hoa'),
  ('Thừa Thiên Huế', 'Thua Thien Hue'),
  ('Tiền Giang', 'Tien Giang'),
  ('Trà Vinh', 'Tra Vinh'),
  ('Tuyên Quang', 'Tuyen Quang'),
  ('Vĩnh Long', 'Vinh Long'),
  ('Vĩnh Phúc', 'Vinh Phuc'),
  ('Yên Bái', 'Yen Bai')
)

class Customer(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 locality = models.CharField(max_length=200)
 city = models.CharField(max_length=50)
 zipcode = models.IntegerField()
 state = models.CharField(choices=STATE_CHOICES, max_length=50)

 def __str__(self):
  # return self.user.username
  return str(self.id)


CATEGORY_CHOICES = (
 ('M', 'Mobile'),
 ('L', 'Laptop')
)
class Product(models.Model):
 title = models.CharField(max_length=100)
 selling_price = models.FloatField()
 discounted_price = models.FloatField()
 description = models.TextField()
 brand = models.CharField(max_length=100)
 category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
 product_image = models.ImageField(upload_to='productimg')

 def __str__(self):
  return str(self.id)


class Cart(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)

 def __str__(self):
  return str(self.id)
  
  # Below Property will be used by checkout.html page to show total cost in order summary
 @property
 def total_cost(self):
   return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
  ('Accepted','Accepted'),
  ('Packed','Packed'),
  ('On The Way','On The Way'),
  ('Delivered','Delivered'),
  ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)
 ordered_date = models.DateTimeField(auto_now_add=True)
 status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

  # Below Property will be used by orders.html page to show total cost
 @property
 def total_cost(self):
   return self.quantity * self.product.discounted_price
class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.title}'