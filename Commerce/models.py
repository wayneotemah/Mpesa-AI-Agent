from django.db import models
from twilio.rest import Client
from django.db.models import Q
from dotenv import load_dotenv
import os


load_dotenv()


client = Client(os.getenv("TWILIO_ACCOUNT_SID"),os.getenv("TWILIO_AUTH_TOKEN"))



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
    category = models.CharField(max_length=100,choices= choices)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_product_picture(product_id):
        product = Product.objects.get(id=product_id)
        print(product.image.url)
        return product.image.url
    
    @staticmethod
    def get_product(product_name):
        # This method now searches across multiple fields and orders by date_created
        products = Product.objects.filter(
            Q(id__icontains=product_name) |  
            Q(name__icontains=product_name) |
            Q(price__icontains=product_name) |
            Q(description__icontains=product_name) |
            Q(category__icontains=product_name)
        ).order_by('-date_created')
        
        return products.first() if products else None
    
    @staticmethod
    def send_product_picture_with_whatsAPP(product_name:str, phone_number:str):
        """Summary
           send a picture of a product to a user's whatsapp number

        Args:
            product_name (int): the product name
            phone_number (str): whatsApp number to sent to

        Returns:
            dict
        """
        try:
            product_id = Product.get_product(product_name).id
            print(product_id)
            image_url = Product.get_product_picture(product_id)
            print(image_url)
            media_url=os.environ.get("NGROK_URL")+image_url
            print(media_url)
            message = client.messages.create(body=f'Here is the image of {product_name}!\n{media_url}',
                        media_url=media_url,
                        from_=os.getenv("TWILIO_PHONE_NUMBER"),
                        to=f"whatsapp:{phone_number}")
            
            return "sent"
        
        except Exception as e:
            return str(e)
        
    
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