from django.db import models

class Product(models.Model):
    choices = [('Electronics','Electronics'),
               ('Fashion','Fashion'),
               ('Home','Home'),
               ('Beauty','Beauty'),
               ('Toys','Toys')]
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    catrgory = models.CharField(max_length=100,choices= choices)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    phone_number = models.CharField(max_length=13)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    
    @staticmethod
    def get_all_orders():
        return Order.objects.all()
    
    @staticmethod
    def get_order_by_id(order_id):
        return Order.objects.get(id=order_id)
    
    @staticmethod
    def get_order_by_phone_number(phone_number):
        return Order.objects.filter(phone_number=phone_number)
    
    @staticmethod
    def get_order_by_date(date):
        return Order.objects.filter(date=date)
    
    @staticmethod
    def get_order_by_product(product):
        return Order.objects.filter(product=product)
    
    @staticmethod
    def get_order_by_total_price(total_price):
        return Order.objects.filter(total_price=total_price)
    
    @staticmethod
    def get_order_by_quantity(quantity):
        return Order.objects.filter(quantity=quantity)
    
    @staticmethod
    def get_order_by_product_name(product_name):
        return Order.objects.filter(product__name=product_name)
    
    @staticmethod
    def get_order_by_product_price(product_price):
        return Order.objects.filter(product__price=product_price)
    
    @staticmethod
    def get_order_by_product_description(product_description):
        return Order.objects.filter(product__description=product_description)
    
    @staticmethod
    def get_order_by_product_image(product_image):
        return Order.objects.filter(product__image=product_image)
    
    @staticmethod
    def get_order_by_product_id(product_id):
        return Order.objects.filter(product__id=product_id)
    
    @staticmethod
    def get_order_by_product_name_and_price(product_name, product_price):
        return Order.objects.filter(product__name=product_name, product__price=product_price)
    
    @staticmethod
    def get_order_by_product_name_and_description(product_name, product_description):
        return Order.objects.filter(product__name=product_name, product__description=product_description)
    
    @staticmethod
    def get_order_by_product_name_and_image(product_name, product_image):
        return Order.objects.filter(product__name=product_name, product__image=product_image)
    
    @staticmethod
    def get_order_by_product_name_and_id(product_name, product_id):
        return Order.objects.filter(product__name=product_name)