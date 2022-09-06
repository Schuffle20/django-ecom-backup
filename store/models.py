from django.db import models
from django.contrib.auth.models import User
import datetime  
from django.utils.timezone import now  

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	joined_on = models.DateTimeField(default = now  ,blank=True)

	def __str__(self):
		return self.name

class Admin(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.user.username

class Category(models.Model):
	name = models.CharField(max_length=150, null=True, blank=True)
	status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
	image = models.ImageField(null=True, blank=True)
	slug = models.CharField(max_length=150, null=True, blank=True)


	# def __str__(self):
	# 	return self.name


class Product(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
	detail=models.TextField(default="true")
	# specs=models.TextField()
	price = models.DecimalField(max_digits=7, decimal_places=2)
	discount_price = models.DecimalField(max_digits=7, decimal_places=2, default=65)
	discount = models.BooleanField(default=False, help_text="0=No Discount, 1=Discount")
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	# def __str__(self):
	# 	return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

ORDER_STATUS = (
	("Order Received", "Order Received"),
	("Order Processing", "Order Processing"),
	("On the Way", "On the Way"),
	("Order Completed", "Order Completed"),
	("Order Canceled", "Order Canceled"),
)

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)
	order_status = models.CharField(max_length=100, choices=ORDER_STATUS, default="")

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		if(self.product.discount):
			total = self.product.discount_price * self.quantity
		else:
			total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address