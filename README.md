# Milestone Project 4: BBQ Time

![Mockup on different screen sizes of home page](https://github.com/clawrence00/bbqtime/blob/main/docs/images/mockup.png)
Welcome to my fourth milestone project with the Code Institute. The purpose of this project is to 

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



### Customer Goals



### Features

- 
- 
- 
- 

### User Stories



### Wireframes

Before any code was written wireframes were created using [Balsamiq](https://balsamiq.com/) for each page on three different screen sizes; mobile, tablet and desktop.

[See all wireframes here](https://github.com/clawrence00/bbqtime/blob/main/docs/wireframes.pdf)

### Data Schema

The following database schema has been created to show the relationship between the data models and the entities within those models.

![Data schema](https://github.com/clawrence00/bbqtime/blob/main/docs/images/data_schema.png)

There are eight database models. 'Users' is the data model that is created by Django allauth and holds individual user logon and session data. The 'user_id' from this data model has been used as a foreign key in three other data models; 'UserProfile', 'Wishlist' and 'Review'. This allows users to save their delivery details and, with the 'product_id' as a second foreign key, add products to the wishlist and add reviews to individual products. The 'Product' data model is also used as a foreign key in the 'OrderLineItem' model along with 'order_id'. This links to the 'Order' data model which collects data for orders placed. Guest order data is still logged as the 'userprofile' key is allowed to be null. The 'Product' data model itself contains the information for individual products and is linked to the 'Category' model by the 'category_id' foreign key. This allows products to be sorted by category.

### Design Choices



#### Font

Heebo

#### Colours



#### Styling



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


 ---

## Testing

### Testing for this project



### Bugs & Fixes

- 


### Validation

The HTML for the welcome message and a question with answers was checked using the [W3C markup validation service](https://validator.w3.org/). There were some warnings relating to the browse table inside the browse modal. This starts with seven columns for the letters, then 5 columns for the numbers. This was deliberately done to evenly spread the links out and does not affect the rendering of the table. Multiple info messages were found where trailing back slashes are present in the code. These are present due to using the 'prettier-vscode' extension in the Codeanywhere IDE.

The CSS was checked using the [W3C CSS validation service](https://jigsaw.w3.org/css-validator/). There were no issues to report.

Google Lighthouse was used on the mobile version of the home page. The initial findings for accessibility were not 100% due to an aria-label not being present on the mobile sidenav trigger button. This was added, along with a meta tag to described the web application for better search engine optimisation.

Flake8

All evidence of the validation can be found in the [validation](https://github.com/clawrence00/bbqtime/tree/main/docs/validation) folder.

---

## Future implementations



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

In your IDE create files that Heroku will need

1. Generate the requirements.txt file with the following command in the terminal. After you run this command a new file called requirements.txt should appear in your root directory

- pip freeze --local > requirements.txt

2. Heroku requires a Procfile containing a command to run your program. Inside the root directory of your project create the new file. It must be called Procfile with a capital P, otherwise Heroku won’t recognise it.
3. Inside the file, add the following command

- web: python app.py

4. Open your init.py file
5. Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, DATABASE_URL.
6. To ensure that SQLAlchemy can also read our external database, its URL needs to start with “postgresql://”, but we should not change this in the environment variable. Instead, we’ll make an addition to our else statement from the previous step to adjust our DATABASE_URL in case it starts with postgres://:
7. Save all your files and then add, commit and push your changes to GitHub

Conneting the database to Heroku

1. Log into Heroku.com and click “New” and then “Create a new app”
2. Choose a unique name for your app, select the region closest to you and click “Create app”
3. Go to the Settings tab of your new app
4. Click Reveal Config Vars
5. Return to your ElephantSQL tab and copy your database URL
6. Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”
7. Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var.

Deploy the site

1. Navigate to the “Deploy” tab of your app
2. In the Deployment method section, select “Connect to GitHub”
3. Search for your repo and click Connect
4. Optional: You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository
5. Use the Manual deploy section and click Deploy Branch. This will start the build process.
6. The project is now in place and there is an empty database. The tables from the models.py file need to be added. Click the “More” button and select “Run console”.
7. Type python3 into the console and click Run
8. This opens the Python terminal. To create the tables use the following commands;

- from mototorque import db
- db.create_all()

9. Exit the Python terminal, by typing exit() and hitting enter, and close the console.
10. Click the “Open app” button to view the deployed site.

To **clone this repository**;

1. On GitHub.com select the main page of the repository.
2. Click the green 'Code' button.
3. Select HTTPS. Click the clipboard icon to copy the repository URL.
4. Create a location on your machine where you want the repository to be cloned.
5. Using Git Bash change the working directory to the location where you want the repository to be cloned.
6. Type *git clone* and paste the URL of the repository, copied in step 3.
7. Press enter. A local clone has now been created on your machine.  
