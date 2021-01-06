Lesson_5_new "Creating online_store"

Step 1. Creating diagram with https://app.quickdatabasediagrams.com
Very important to create right tables with right columns and connections between them. Primary key and Foreign Key.
Review "normalization".

Step 2. Going to terminal and creating new lesson.
     mkdir Lesson5_new

Step 3. Creating virtual folder
    python3 -m venv Lesson5_new # folder with the virtual environment

Step 4. Activate our virtual environment
    source env5_new/bin/activate

Step 5. Install Django in our lesson5
   pip install django

Step 6. Create folder with a new project called "online_store" in folder lesson5
     mkdir online_store_new

Step 7. Creating a new project with django
   django-admin startproject core .

Step 8. Creating a new application

   python3 manage.py startapp products # we are going to create new app for each big instance in our project(products, clients, etc)

Step 9. In pycharm open Lesson5_new\online_store_new
                        select right interpreter python3 in folder bin

Step 10.  Open workbench MySQL
Create a new_schema: Lesson5_online_store_new
For charset select utf8mb4
For collation select utf8mb4_general_ci
Press "Apply"

Create user for Database: press "Users and Privileges" --> "Add Account"
Login name: online_store_user
Password: ############
Authentication Type: Standard
Limit to Hosts Matching: localhost
Press "Apply"
In the "Schema Privileges" tab select "Add Entry" --> "Select All" --> "Apply"

Step 11. Open Pycharm
In pycharm open settings.py
In settings.py in DATABASE dictionary(or object) need to add:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/Users/pro/projects/lesson5/mysql.cnf', # file path for mysql.cnf
        },
    }
}

In mysql.cnf we wrote info about password and login in database:
[client]
database = les_5_online_store
user = online_store_user
password =############ I am not writing password here
default-char-set = utf8

Save this mysql.cnf file in lesson5 folder

Step 12. Connecting library mysqlclient

   pip install mysqlclient # for windows
   #for mac:
   first we need to install homebrew:
   brew install mysql-client # will be done once and forever. This command is updating homebrew
   then:
   sudo apt-get install python-dev python3-dev
   the OS will ask for user password: Apple

   brew install mysql-connector-c # for mac OS
   pip install mysqlclient # for mac

Step 13. Now we need to migrate tables from Django to mysql
  python3 manage.py migrate
Then check in Mysql if we have tables created by Django

Step 14. Open models.py
Creating new classes: # That's how we describe every table

class Product(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'

    title = models.CharField(blank=False, null=False, max_length=200, verbose_name='Title')
    price = models.FloatField(blank=False, null=False, verbose_name='Price')

    Add additional columns:

    product_brand = models.CharField(blank=False, null=False, max_length=200, verbose_name='Product_Brand', default='Not Specified')
    year_of_manufacture = models.IntegerField(blank=False, null=True, verbose_name='Year_Of_Manufacture')
    color = models.CharField(blank=False, null=False, max_length=50, verbose_name='Color', default='Not specified')
    quantity = models.IntegerField(blank=False, null=False, verbose_name='Quantity', default=1)
    product_image = models.ImageField(blank=False, null=False, verbose_name='Product_Image', default='No image available')
    size = models.CharField(blank=False, null=False, max_length=100, verbose_name='Size', default='Small')
    weight = models.DecimalField(blank=False, null=False, decimal_places=3, max_digits=12, verbose_name='Weight', default='180.00')
    description = models.CharField(blank=False, null=False, max_length=300, verbose_name='Description', default='Not Specified')

    Make migrations after you describe your table's columns

Connecting application products in settings.py:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products' #we added our application 'products'
]
After that we describe our table products, we migrate data to mysql:
    python3 manage.py makemigrations

    python3 manage.py migrate # after that we need to check our database in workbench to see if they appeared there
    #if we add new columns here, then we need to write same commands:
    python3 manage.py makemigrations

    python3 manage.py migrate

Step 15. Creating new Table Category
class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(blank=False, null=False, max_length=200, verbose_name='Title')
    description = models.CharField(blank=False, null=False, max_length=300, verbose_name='Description', default='Not Specified')
Step 16. Creating new Table ProductCategory
class ProductCategory(models.Model):
    class Meta:
        db_table = 'products_categories'
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Good', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name='Category', on_delete=models.CASCADE)

After we described new models(tables) and columns(as well as connected them using ForeignKey) we need to make migrations
 again!!!
    python3 manage.py makemigrations

   python3 manage.py migrate

 Then we go to workbench and refresh our database. There you will see new tables and columns.

Step 17. Creating new Application clients

   terminal command:
   python3 manage.py startapp clients

Repeat steps for Application products except new columns and changes in names of columns:


from django.db import models

class Client(models.Model):
    class Meta:
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    first_name = models.CharField(blank=False, null=False, max_length=30, verbose_name='First Name')
    last_name = models.CharField(blank=False, max_length=40, verbose_name='Last Name')
    login = models.CharField(blank=False, null=False, max_length=30, verbose_name='Login')
    email = models.EmailField(blank=False, null=False, max_length=80, verbose_name='Email Address')
    password = models.CharField(blank=False, null=False, max_length=30, verbose_name='Password')
    address_1 = models.CharField(blank=True, null=True, max_length=60, verbose_name='Corporate Address')
    address_2 = models.CharField(blank=False, null=False, max_length=60, verbose_name='Street Address')
    city = models.CharField(blank=False, null=False, max_length=20, verbose_name='City')
    state_or_province = models.CharField(blank=False, null=False, max_length=30, verbose_name='State / Province')
    county = models.CharField(blank=True, null=False, max_length=30, verbose_name='County')
    postal_code = models.CharField(blank=False, null=False, max_length=14, verbose_name='Postal / Zip Code')


    Do not forget to add application clients in setting.py in core application:

    'INSTALLED APPS' Section right after application 'products'

Then we make migrations:
    python3 manage.py makemigrations
    python3 manage.py migrate

Then we go to workbench and refresh our database. There you will see new tables and columns.

Step 18. Creating application orders

terminal command:
     python3 manage.py startapp orders

add new app in in setting.py in core application:

    'INSTALLED APPS' Section right after application 'products' and 'clients' # use comma(,)  and quotes('')

Then we create 2 models(tables) Order and Cart

from django.db import models
from clients.models import Client #That's how we import Client Model to connect with table in this Application
from products.models import Product # That's how we import Product Model to connect with table in this Application


class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    client = models.ForeignKey(Client, blank=False, null=True, verbose_name='Good', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False, null=False, verbose_name='Order Date and Time')
    payment_method = models.CharField(blank=False, null=False, max_length=20, verbose_name='Payment method')
    delivery_method = models.CharField(blank=False, null=False, max_length=20, verbose_name='Payment method')
    delivery_date = models.DateTimeField(blank=False,null=False, verbose_name='Delivery Date')
    total_price = models.FloatField(blank=False, null=False, verbose_name='Total Price')


class Cart(models.Model):
    class Meta:
        db_table = 'carts'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    order = models.ForeignKey(Order, blank=True, verbose_name='Order', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False, null=False, verbose_name='Date and Time Created')
    item_price = models.FloatField(blank=False, null=False, verbose_name='Item Price')
    quantity = models.IntegerField(blank=False, null=False, verbose_name='Products Quantity')
    sub_total = models.FloatField(blank=False, null=False, verbose_name='Sub total')
    product = models.ForeignKey(Product, blank=False, null=True, verbose_name='Good', on_delete=models.CASCADE)


    Pay attention how we connect two tables using ForeignKey!!!!!!!!!!!!

    then make migrations:

    python3 manage.py makemigrations
    python3 manage.py migrate

Then we go to workbench and refresh our database. There you will see new tables and columns.

Then we can add more Models!!!!!

Step 19. Now we need to add our Apps and Models to administrative panel in Django app
For each app we will use views.py file, admin.py and we need to create urls.py file for EACH app separately
 See those files to have an idea what I do. 
 
 After we are done --> save --> runserver --> use link to access admin panel(do not forget to use /admin in the end of localhost url)
 There you will see them all! 
 Check admin panel.
