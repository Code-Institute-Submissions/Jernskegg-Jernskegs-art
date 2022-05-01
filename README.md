![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Casper Hille

Full-Stack Development course (5p) | Portfolio project 5 (E-Commerce focused project)
---

# Purpose of the Project

The project aims to make an e-commerce webpage with an authorization system and payment methods

The page built to sell my art and make me available for people to make requests or commissions in the art community.
# Design, planning and Wireframes

## User Stories

  Using a Kanban board, I will use Agile development to work on one user story at a time.

  - As an Admin, I can go to inquiries so that I can fulfil a users request
  - As an Admin, I can disable a user so that I can prevent users from accessing the page after they have broken the terms of service
  - As an admin, I can create  a product post, set a price, upload image (epic) so that I can sell my products
  - As a User, I Can look at the gallery so that I can browse for designs
  - As a User, I Can add an item to my shopping cart so that I can buy can see the price combined and buy them all in one go
  - As a User, I Can add a request so that I can buy the graphic design that fits my purpose
  - As a User, I Can subscribe to the gallery so that I will be notified when new art is being posted in a form of a newsletter
  - As a User, I Can go to purchase history so that I can watch the status of my inquiry
  - As a User, I Can change my profile To keep my contact details updated
  - As a User, I Can order(filter) the products so that I can more easily find what I need
  - As a User, I Can make an account so that I can have the benefits
  - As a User, I Can change my password to keep my account secured
  - As a User, I Can go to purchase history to download the art I have bought (This has changed to receiving it in email)
  - As a User, I can go to Order Status to watch updates so that I can give input

## Admin panel userstories

  - As an admin/site owner, I can view requests so that so that I can fulfil a users order
  - As an Admin, I can add a product so that I can add a new product easily to be able to sell it
  - As an Admin, I can Delete an image so that I can remove an Image I don't want to be sold anymore
  - As an Owner/admin, I can adjust prices so that so that I can increase/decrease prices to increase sales

## Rough sketch

![wireframe](docs/wireframes/home.png)
![wireframe](docs/wireframes/gallery.png)
![wireframe](docs/wireframes/request.png)

## Database relations

![Databaserelation](docs/images/db_diagram.png)

## Data model

# Features

  ## Gallery

  the webpage uses a database and accesses it, displays the database entries as a repeatable template and Bootstrap popup

  ## Shop

  From the gallery, you can purchase items using stripe as a secure payment method

  ## Request

  the webpage has a request feature where the user is allowed to request more personalized images/artwork

  ##  E-commerce Admin panel

 In the Admin panel  you can adjust the price, name, and Change the visibility of a product or delete an image.

  ## python

  Python is an easy and basic programming language, but it is powerful with libraries to bring out capabilities to use for mulitple purposes

  ## Django Framework

  Django is a framework that is made to speed up the process of building web applications, Here you can make apps and then use the apps for different projects. it has extensive documentation.

  It is like all on in framework or "Batteries included philosophy framework"

# Future features

  ## Request

  I have planned to add user feedback and a chat system per order so that the Admin and user can have a feedback loop going, To ensure the Customer is fully satisfied with the result

  ## E-commerce Admin panel

  add the Cloudinary file to allow changing the existing picture instead of having to add a new product


# Bussiness model

  My idea is to sell art to private customers and people who want art they could print out and hang at home, have as a desktop wallpaper.

  Businesses can also make a request but this service is aimed at private customers, so mainly B2C 

  The target audience is pretty big but niched, Mostly people who play games there is a lot of requests for artwork on communities on facebook "World of Warcraft" group or forums, so using Googles/facebook ads on those pages would increase webpage traffic, Facebook groups are commonly used for art commission so announcing the existence in communities would also increase webpage traffic.

  one market strategy would be to build a customer base. So have left requests for free which if they are satisfied they would willing to come back and tell their friends or recommend the business services.

 ## Facebook page
 I have created a Facebook page if for any reason the link is dead I've attached a [screenshot](docs/images/facebook.png). 

# testing

  ## code validation

  - W3C HTML validated, No errors
  - JShint Validated. 1 warning "Stripe variable undefined", Disregarding this because this - variable is being used by Stripes main JS
  - Jigsaw CSS validated, No errors
  - Pep8 validated, No errors except for Generated files,

  ## Responsive tests

  I am going to check all pages and test them through Google developer tools using the Device toolbar and set it to different models of tablets and phones.

  - ## Nexus 5
    
  - ## Galaxy Note II

  - ## Ipad Pro
  
  - ## Iphone 6/7/8 plus

  ## Automated testing

  - ## File checker
     in the admin panel made a custom function to test for file format, And to ensure my function worked I've made tests accordingly and designed it after the tests

  ## User Story testing

  In this testing phase, I will go manually test all user stories to ensure they work as intended.

  User Story: Add an inquiry: Sign up link not working when not logged in.

  User Story: Ap view requests. Shows on the overview but not designated tab

  The rest of the user stories work as intended

# Deployment

## via Heroku

- Before you deploy, ensure your requirements.txt is updated and accounted for and get your API keys ready. I have Attached a Example.Env.py with intructions in it '

- to deploy an application through Heroku, you need to make an account. Once you have created an account, you can have up to 5 projects on the free plan.

- To create a new app. Log in, and you'll see a "Create app" button.
  Once pressed, you'll be able to name your project and choose which region your application will host. The name needs to be unique.

- You'll need to set up all your setting before you can deploy your project. You can find the “setting” in the tabs in the dashboard.

  If you have API keys, you can insert them in the Config Vars section, and there is a button to reveal the keys.
  once clicked, the const you used in the project should be in "KEY" and creds.json in the "VALUE"

  Next, we'll set up build packs. Press the build pack and add the build packs you need. If you need more than one, make sure you put them in the correct order, You can drag and drop their list items.

- now, we can start the deployment by heading over to the deploy tab. in this project, I chose to deploy through GitHub.

  After I clicked through GitHub, I had to connect Heroku to my GitHub account. Thereafter I had to search for my project. Once selected.
  I could choose which branch.

  Now I can select an automatic deployment, which updates the app once GitHub updates or a manual deployment that will only update Heroku when I press that button again.

  Now we'll wait for Heroku to download all plugins and install all the requirements. Once done, there will be a message telling it is completed or failed. Once successful, it will show a button to view your deployed application.

- Now you have your deployed page. Now you can test if everything works as it should or send the links to your friends to show off those accomplishments you have made.



# Credits

  Some parts of the checkout have been taken from Stripes docs.
  checkout and cart app was coded along with Boutique-ado from Code Institute, Some similarities may occur and those credits go to Code institute
