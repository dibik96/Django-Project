# Django Blog Application  

Welcome to the **Django Blog Application**!  
This is a simple yet powerful blog application built with Django, allowing you to create, edit, and manage blog posts dynamically via the admin interface.  

## Features  
- **Dynamic Blog Management**: Easily create, update, and delete blog posts through the Django admin panel.  
- **Django Admin Interface**: Leverage Django's robust admin interface to efficiently manage your blog content.  

## Installation  

1. Clone this repository:  
   ```bash  
   git clone https://github.com/dibik96/Django-Project.git  
   ```  

2. Navigate to the project directory:  
   ```bash  
   cd django-blog-application  
   ```  

3. Create a virtual environment:  
   ```bash  
   python -m venv env  
   source env/bin/activate  # On Windows: env\Scripts\activate  
   ```  

4. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

5. Run migrations to set up the database:  
   ```bash  
   python manage.py migrate  
   ```  

6. Create a superuser to access the admin interface:  
   ```bash  
   python manage.py createsuperuser  
   ```  

7. Start the development server:  
   ```bash  
   python manage.py runserver  
   ```  

8. Access the application at:  
   - Blog: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  

## Usage  

1. Log in to the admin panel using the superuser account created earlier.  
2. Add, update, or delete blog posts directly from the admin interface.  
3. View your blog posts dynamically on the front end.  

## Technologies Used  
- **Backend**: Django  
- **Database**: SQLite (default)  
- **Frontend**: HTML, CSS (optional for customization)  
 
