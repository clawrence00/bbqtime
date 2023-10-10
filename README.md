# Milestone Project 4: BBQ Time

![Mockup on different screen sizes of home page](https://github.com/clawrence00/bbqtime/blob/main/docs/images/mockup.png)
Welcome to my fourth milestone project with the Code Institute. The purpose of this project is to build a full-stack site based around business logic to control a centrally-owned dataset. Authentication will be required to perform certain actions and gain further value from the site. Stripe has been used to provide online payment processing giving the project e-commerce functionality.

**Please find my deployed site [here](https://bbq-time-7d47ca93266d.herokuapp.com/).**

---

## Technologies used

- HTML5
- CSS3
- JavaScript
- Python3, using the following packages;
  - asgiref==3.7.2
  - boto3==1.28.62
  - botocore==1.31.62
  - dj-database-url==0.5.0
  - Django==3.2.22
  - django-allauth==0.41.0
  - django-countries==7.2.1
  - django-crispy-forms==1.14.0
  - django-storages==1.14.1
  - gunicorn==21.2.0
  - jmespath==1.0.1
  - oauthlib==3.2.2
  - Pillow==10.0.1
  - psycopg2==2.9.9
  - python3-openid==3.2.0
  - pytz==2023.3.post1
  - requests-oauthlib==1.3.1
  - s3transfer==0.7.0
  - sqlparse==0.4.4
  - stripe==6.6.0
  - urllib3==1.26.17
- Balsamiq
- Font Awesome
- Google Fonts
- Bootstrap v4.6
- GitHub
- codeanywhere
- Heroku
- ElephantSQL
- PostgreSQL
- S3 - Amazon Web Services (AWS)

---

## UX & UI

### Project Goals

The goal of the project is to build a full-stack site that provides e-commerce functionality so that a user can purchase a product they want and the site owner can make a profit selling products.

### Customer Goals

Users can browse the online shop, add products to the basket and checkout securely. Users can checkout as guests or as registered account holders.

### Features

- Users can browse products by category.
- Users can use a search input to browse for products.
- Users can checkout securely as guests.
- Users can register, which saves their details and allows them to view their order history.
- Users can add products to a wishlist that only they can see.
- Users can add reviews for products that other users can read.
- Shop owners can display their products.
- Shop owners can add, edit and delete products from the shop.

### User Stories

| User story # | As a...          | I want to be able to...                           | so that I can...        |
|--------------|------------------|---------------------------------------------------|-------------------------|
|1	           |shopper           |	view all products	                              | choose something to buy |
|2	           |shopper	          |view products by category                          |filter the things I want to buy
|3	           |shopper	          |search the shop	                                  |find the product I want to buy without extensive browsing
|4	           |shopper	          |add items to a basket	                          |purchase all items in the basket
|5	           |guest shopper     |checkout without signing up                        |purchase items without an account
|6	           |registered shopper|save delivery info	                              |not need to enter it each time I purchase something
|7	           |registered shopper|create a wishlist of items                         |find the products easily to puchase them in the future
|8	           |shopper	          |read reviews for individual products               |make an informed decision on whether to purchase the product or not
|9	           |shopper	          |leave reviews for individual products I have bought|publish my experience to inform other shoppers
|10	           |shop owner	      |display products for sale	                      |sell products
|11	           |shop owner	      |provide a secure checkout	                      |give customers confidence to purchase from my shop



### Wireframes

Before any code was written wireframes were created using [Balsamiq](https://balsamiq.com/) for each page on three different screen sizes; mobile, tablet and desktop.

[See all wireframes here](https://github.com/clawrence00/bbqtime/blob/main/docs/wireframes.pdf)

### Data Schema

The following database schema has been created to show the relationship between the data models and the entities within those models.

![Data schema](https://github.com/clawrence00/bbqtime/blob/main/docs/images/data_schema.png)

There are eight database models. 'Users' is the data model that is created by Django allauth and holds individual user logon and session data. The 'user_id' from this data model has been used as a foreign key in three other data models; 'UserProfile', 'Wishlist' and 'Review'. This allows users to save their delivery details and, with the 'product_id' as a second foreign key, add products to the wishlist and add reviews to individual products. The 'Product' data model is also used as a foreign key in the 'OrderLineItem' model along with 'order_id'. This links to the 'Order' data model which collects data for orders placed. Guest order data is still logged as the 'userprofile' key is allowed to be null. The 'Product' data model itself contains the information for individual products and is linked to the 'Category' model by the 'category_id' foreign key. This allows products to be sorted by category.

### Design Choices

#### Font

The font used throughout the website is Heebo. This is a sans-serif font that gives the website a clean, contemporary look.

#### Colours

As an image has been used as the main background a black navbar and a dark footer image have been used to frame the webpage. All products and information are placed in cards that use Bootstrap's default styling. This is mainly a white background with some light grey sections to differentiate between parts of the card.

For the font a very dark grey was used to contrast against the light backgrounds.

A theme of orange was used throughout for webpage headings and icons such as the bullet points, the basket and the fire icon bullet points.

Most buttons took on Bootstrap's styling using mostly. the btn-warning and btn-danger classes

#### Styling

The bootstrap framework was used for this project. The responsive navbar was used from Bootstraps components. Inspiration was taken from the [album example](https://getbootstrap.com/docs/4.6/examples/album/) for the shop. Cards were used on many pages due to the fixed, consistent layout that they achieved. 

#### Images

The navbar logo was created on [logo.com](https://logo.com/).

Several images have been used in this project. A main image is has been set as the background of a person grilling on a kettle BBQ. This fits in with the theme of the website and made for a nice background to have with the product cards on top of it. This image was sourced from Vincent Keiman on [Unsplash](https://unsplash.com/photos/ul_m5dHThaM).

The footer uses another image of some burning coals, again fitting in with the BBQ theme. This clearly defines the footer and makes the site look more interesting, particularly when a large amount of the foreground is taken up with a product detail card or basket/checkout.  This image was sourced from Almos Bechtold on [Unsplash](https://unsplash.com/photos/GFgWx3o8bTI).

The product images were taken from [Angus & Oink's](https://angusandoink.com/) product range.

The majority of images were resized on [imageresizer.com](https://imageresizer.com/) to either reduce the file size hence improve website performance or to keep the product images at a similar scale.

![Home page](https://github.com/clawrence00/bbqtime/blob/main/docs/images/home_page.png)

![Shop](https://github.com/clawrence00/bbqtime/blob/main/docs/images/shop.png)

![Product detail page](https://github.com/clawrence00/bbqtime/blob/main/docs/images/product_detail.png)

![Basket](https://github.com/clawrence00/bbqtime/blob/main/docs/images/basket.png)

---

## Credits

### Code

- The main bulk of the project was built using the [Boutique Ado walkthrough](https://github.com/Code-Institute-Solutions/boutique_ado_v1) from the Code Institute.

- The following sources helped with styling the cards;
  - As mentioned in the Design Choices section Bootstraps album example
  -  [sepuckett86's answer](https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width) to making images in cards the same.
  - [ObjectiveTC's answer](https://stackoverflow.com/questions/39031224/how-to-center-cards-in-bootstrap-4) for centering cards

- The following sources were used to create the Wishlist and Review models and also help with the functionality;
  - For the Review model this [youtube video](https://www.youtube.com/watch?v=8iCqlFyFu2s&ab_channel=CodeWithStein) from Code With Stein
  - For the Wishlist model this [youtube video](https://www.youtube.com/watch?v=A8rarkE0TKQ&ab_channel=codepiep) from codepiep
  - Adding to the Wishlist [Ajmal Aamir's answer](https://stackoverflow.com/questions/56580696/how-to-implement-add-to-wishlist-for-a-product-in-django)
  - Deleting objects [Wolph's answer](https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models)

### Media

- Product images and descriptions were used from [Angus & Oink's](https://angusandoink.com/) product range. The content and media has been used for educational purposes only.

---

## Testing

### Testing for this project

Manual testing was performed to check the functionality of the site using an authenticated user, non-authenticated user and the admin. To record this testing a test script was created to follow a sequence of steps with the expected output. The actual output was reported and screenshots were appended to provide evidence of this testing.

The responsiveness was tested during development using Chrome Developer Tools by changing the screen resolution.

Stripe was tested using the following card numbers;
  - 4000000000009995 for a failed payment. Ensure the expiry date is a date in the future.
  - 4242424242424242 for a successful payment. Again, ensure the expiry date is a date in the future.

### Bugs & Fixes

- Using the Stripe documentation the Stripe CLI was used to test the webhooks. A failure constantly occurred on the payment_intent.succeeded. Searching through Slack the [answer](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1631980362410300) was simple - the test webhook does not contain the required data therefore I was receiving an internal server error. When performing the check within the application all webhooks are received successfully.
- Using the 'prettier-vscode' extension in the Codeanywhere IDE caused Django template errors when it reformatted the code automatically after manually saving. Instead of manually saving changes I allowed the IDE to auto save which prevented the extension from applying itself.


### Validation

The HTML for all pages was checked using the [W3C markup validation service](https://validator.w3.org/). There were some warnings and errors with all the web pages. Trailing slashes and potential misuse of aria-label were common with most pages. These were addressed appropriately.

The CSS was checked using the [W3C CSS validation service](https://jigsaw.w3.org/css-validator/). There were no issues to report.

The JS was checked using [JSHint](https://jshint.com/). Any errors or warnings were corrected with the exception of the variable 'stripe' in checkout as this was required for Stripe to work.

Flake8 was used to check for pep8 compliance. All files created were corrected to comply, migrations and django generated code (bbqtime\settings.py) were not corrected. Two lines in checkout\webhook_handler.py are too long and cannot be changed without affecting the functionality of the code. In checkout\apps.py there is an error that signals is imported but not used. Signals is required for the app to work correctly therefore was not removed.

All evidence of the testing and validation can be found in the [validation](https://github.com/clawrence00/bbqtime/tree/main/docs/validation) folder.

---

## Future implementations

I would have liked to implement an optional subscription for registered users which would give free delivery on all orders and a monthly 'mystery box' product. Subscriptions are possible with Stripe and was attempted using the Stripe documentation however I was unable to implement this.

---

## Deployment

The website was deployed using Heroku. The PostgreSQL database was hosted by ElephantSQL. Here are the following steps required to **deploy the site**;

Set up ElephantSQL to host your database instance

1. Go to ElephantSQL.com and click "Get a managed database today"
2. Select "Try now for FREE" in the TINY TURTLE database plan
3. Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account
4. In the Create new team form:

- Add a team name (your own name is fine)
- Read and agree to the Terms of Service
- Select Yes for GDPR
- Provide your email address
- Click “Create Team

5. Your account is successfully created! Click “Create New Instance”
6. Set up your plan

- Give your plan a Name (this is commonly the name of the project)
- Select the Tiny Turtle (Free) plan
- You can leave the Tags field blank

7. Select “Select Region”
6. Then click “Review”
7. Check your details are correct and then click “Create instance”
8. Select a data center near you
9. Return to the ElephantSQL dashboard and click on the database instance name for this project. Leave this tab open.

Create a new Heroku app

1. Log into Heroku.com and click “New” and then “Create a new app”
2. Choose a unique name for your app, select the region closest to you and click “Create app”
3. Go to the Settings tab of your new app
4. Click Reveal Config Vars
5. Return to your ElephantSQL tab and copy your database URL
6. Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”

Project preparation in your IDE

1. In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to your external database.
   - pip3 install dj_database_url==0.5.0 psycopg2
2. Update your requirements.txt file with the newly installed packages
   - pip3 freeze > requirements.txt
3. In your settings.py file, import dj_database_url underneath the import for os
4. Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated. DO NOT COMMIT THIS FILE. This is temporary so that the new database can be connected and migrations made.
```
    DATABASES = {
        'default': dj_database_url.parse('your-database-url-here')
    }
```

5. In the terminal, run the showmigrations command to confirm you are connected to the external database
   - python3 manage.py showmigrations
6. If you are, you should see a list of all migrations, but none of them are checked off
7. Migrate your database models to your new database
   - python3 manage.py migrate
8. Create a superuser for your new database. The email address can be left blank.
   - python3 manage.py createsuperuser
9. To prevent exposing the database when pushing to GitHub the code in step 4 will be deleted from settings.py. The database in settings.py should look like the following;
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
 ```
 10. In settings.py use the following setting to prevent 500 errors during login on the deployed site.
- ACCOUNT_EMAIL_VERIFICATION = 'none'

Confirm your database

1. On the ElephantSQL page for your database, in the left side navigation, select “BROWSER”
2. Click the Table queries button, select auth_user
3. When you click “Execute”, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database.

Deploy the site

1. In your IDE install gunicorn.
   - pip3 install gunicorn
2. Update your requirements.txt file with the newly installed package
   - pip3 freeze > requirements.txt
2. Heroku requires a Procfile containing a command to run your program. Inside the root directory of your project create the new file. It must be called Procfile with a capital P, otherwise Heroku won’t recognise it.
3. Inside the file, add the following command
  - web: gunicorn bbq_time.wsgi:application
4. In you IDEs terminal log in to Heroku and disable collect static files
   - heroku config:set DISABLE_COLLECTSTATIC=1 --app [github username]-[github repository name]
5. In settings.py add Heroku to ALLOWED_HOSTS
6. Commit and push these changes to GitHub
7. Navigate to the “Deploy” tab of your app
8. In the Deployment method section, select “Connect to GitHub”
9. Search for your repo and click Connect
10. Optional: You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository
11. Use the Manual deploy section and click Deploy Branch. This will start the build process.
12. The project is now in place.

Set up an Amazon Web Services Account (AWS)

1. Set up an AWS Account
2. Create a new bucket to store your static files using the S3 service.

Deploy Static files to Heroku

1. In settings.py add the following;
```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'YOUR BUCKET NAME'
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
2. The following setting/keys need to be added to the Heroku config Variables;
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - SECRET_KEY
   - STRIPE_PUBLIC_KEY
   - STRIPE_SECRET_KEY
   - STRIPE_WH_SECRET
   - USE_AWS : TRUE
3. DISABLE_COLLECTSTATIC should be removed.
4. Commit and push these changes to GitHub. If automatic deploys are enabled the Heroku will begin the build. If not, on the Heroku dashboard, in the manual deploy section, click 'deploy branch'.

To **clone this repository**;

1. On GitHub.com select the main page of the repository.
2. Click the green 'Code' button.
3. Select HTTPS. Click the clipboard icon to copy the repository URL.
4. Create a location on your machine where you want the repository to be cloned.
5. Using Git Bash change the working directory to the location where you want the repository to be cloned.
6. Type *git clone* and paste the URL of the repository, copied in step 3.
7. Press enter. A local clone has now been created on your machine.  
