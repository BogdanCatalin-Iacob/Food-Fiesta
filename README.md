## Table of Contents
* [Purpose](#Purpose)
* [User Experience Design (UX)](#User-Experience-Design)
  * [User stories](#User-Stories)
    * [First Time Visitor Goals](#First-Time-Visitor-Goals)
    * [Returning Visitor Goals](#Returning-Visitor-Goals)
    * [Frequent User Goals](#Frequent-User-Goals)
  * [Structure](#Structure)
  * [Design](#Design)
    * [Colour Scheme](#Colour-Scheme)
    * [Typography](#Typography)
    * [Imagery](#Imagery)
    * [Wireframes](#Wireframes)
    * [Limitations](#Limitations)
* [Features](#Features)
    * [Existing Features](#Existing-Features)
    * [Future Features](#Features-Left-to-Implement)
* [Technologies](#Technologies)
* [Testing](#Testing)
    * [Test Strategy](#Test-Strategy)
      * [Summary](#Summary)
    * [Test Results](#Test-Results)
    * [Testing Issues](#Issues-and-Resolutions-to-issues-found-during-testing)
* [Deployment](#Deployment)
    * [Project Creation](#Project-Creation)
    * [GitHub Pages](#Using-Github-Pages)
    * [Locally](Run-Locally)
* [Credits](#Credits)
    * [Code](#Code)
    * [Content](#Content)
    * [Media](#Media)
    * [Acknowledgements](#Acknowledgements)
    * [Comments](#Comments)

## Purpose
This Website was created for the sole purpose of completing the third Milestone Project for the Code Institute's Full Stack Developer course. 
It was built using the knowledge gained from the HTML, CSS, JavaScript, Python, Flask, MongoBb and SQL modules. A full list of technologies used can be found in the technologies section of this document.

The live website can be found [here](https://food-fiesta-ms3.herokuapp.com/).
![Website Mock Up]()

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals
        1. As a First Time Visitor, I want to see different recipes so I can select one that looksgood to cook
        1. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content
        1. As a First Time user, I want to view the website and content clearly on my mobile device
        1. As a First Time user, I want to be able to register an account

    -   #### Returning Visitor Goals
        1. As a Returning Visitor, I want to be able to create recipes
        1. As a Returning Visitor, I want to find community links
        1. As a Returning Visitor, I want to keep my login informations hidden

    -   #### Frequent User Goals
        1. As a Frequent User, I want to be able to see and edit my recipes

    -   #### Admin User Goals
        1. As admin, I want to be able to create new categories
        1. As admin, I want to be able to edit categories
        1. As admin, I want to be able to delete categories
        1. As admin, I want to be able to create new recipes or edit recipes
        1. As admin, I want to be able to delete recipes
        1. As admin, I want to be able to delete users accounts

-   ### Structure

    - All Pages will contain a Navigation menu at the top of the Webpage that directs them to a new Page to allow users to Navigate the site easily. The Nav Menu will be collapsable on a Mobile device to make use of space on smaller devices.<br>
        The purpose of this is to fulfill user story:
        > As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
    
    - Materialize framework will be used to make the website resposive on different devices and display organised content.
    All pages will be responsive and the layouts will change dependant on screen size. This is to ensure content flow is appealing, images are displayed properly and that the content is not shrunk side by side, so small that it is unreadable.<br>
        The purpose of this is to fulfill user story:
        > As a First Time user, I want to view the website and content clearly on my mobile device.

    - All pages will contain a Footer Element Social Media Icons. The icons used will be from font-awesome. These are referenced below in the Technologies section of this document.<br>
        The purpose of this is to fulfill user story:
        > As a Returning Visitor, I want to find community links.

    - A Registration page will be provided so the users can register an account
	    - this gives to user the opportunity to register an account and create/edit own recipes
	    - a link to login page is provided at the bottom of the page in case user already has an account<br>
        The purpose of this is to fulfill user story:
        > As a First Time user, I want to be able to register an account

    - A login page will be provided so any registered user can login 
	    - this gives to registered user the possibility to create/edit recipes at any time after registration
	    - a link to register page is provided at the bottom of the page in case the user doesn't have an account already<br>
        The purpose of this is to fulfill user story:
        > As a Returning Visitor, I want to be able to create recipes<br>
        > As admin, I want to be able to create new recipes or edit recipes

    - A logout link will be displayed in the navbar for any logged in user
	    - this is to ensure the user's data are not accessible for other users<br>
        The purpose of this is to fulfill user story:
        > As a Returning Visitor, I want to keep my login informations hidden

    - A dedicated page to create recipes will be provided for registered users
        - this gives the possibility to share recipes with other users of the website<br>
        The purpose of this is to fulfill user story:
        > As a Returning Visitor, I want to be able to create recipes<br>
        > As admin, I want to be able to create new recipes or edit recipes

    - An edit recipe page will be provided for logged in users if the user is the creator of the recipe<br>
        The purpose of this is to fulfill user story:
        > As a Frequent User, I want to be able to see and edit my recipes<br>
        > As admin, I want to be able to create new recipes or edit recipes

    - A recipe page with recipes from db will be provided for any type of user
	    - all recies will be available on this page
	    - only the recipes created by the current logged in user will have edit/delete buttons available
	    - each recipe has a dropdown list to display recipes details<br>
        The purpose of this is to fulfill user story:
        > As a First Time Visitor, I want to see different recipes so I can select one that looksgood to cook<br>
        > As a Frequent User, I want to be able to see and edit my recipes<br>
        > As admin, I want to be able to create new recipes or edit recipes

    - A profile page will be provided for any logged in user
	    - the page will display only the recipes created by the logged in user
	    and they will have dedicated edit/delete buttons<br>
        The purpose of this is to fulfill user story:
        > As a Frequent User, I want to be able to see and edit my recipes<br>
        > As admin, I want to be able to create new recipes or edit recipes

    - A category page will be provided to the admin user
	    - Add category button available to create new categories -> a new page will be displayed and gives possibility of adding a new category
	    - all existent categories will be displayed on this page
	    - each category will have edit/delete buttons available
	    - edit button opens a new page where category name edit is possible
	    - delete button removes the category from db<br>
        The purpose of this is to fulfill user story:
        > As admin, I want to be able to create new categories<br>
        > As admin, I want to be able to edit categories<br>
        > As admin, I want to be able to delete categories<br>

-   ### Design
    -   #### Colour Scheme
        -   The main colours used are: . 

    -   #### Typography
        
        
    -   #### Imagery
        -   

    -   #### Wireframes
Home Page<br>
![Home Page Wireframe]()<br>


-   ### Limitations

***
## Features
 
-   ### Existing Features

    - Each page of the website features a consistent responsive navigational system:

    - The header contains the logo of the website in the center of the navigation bar. This will also redirect users back to the home page once clicking on it. On       smaller screens, everything but the logo is condensed down into a dropdown menu which provides users with the same navigation. I chose a dropdown because I think it works better and is more presentable on smaller devices. On the far right of the navigation bar, the user is presented with either 'login' or 'logout' depending on if they have an account they are logged into.

    - Each page can be accessed from a mobile device

    - Standard user features
        - Registration page
        - Login page
        - Logout page
        - Create recipe page
        - View recipes
        - Edit recipe page
        - Delete Recipe
    - Admin user features on top of the standard features
        - Create categories
        - View categories
        - Edit categories
        - Delete categories

    - The footer is intentionally simple to keep up with the simplicity of the rest of the site. It contains social network links .


- Error page (404) to redirect the user back to home page<br>
    ![error-page]()<br>

- Icon in the browser tab<br>
    ![browser-tab-icon]()<br>

-   ### Features Left to Implement

    - Admin user to be able to create users and give the admin privileges
   

***

## Technologies

* HTML
	* This project uses HTML as the main language used to complete the structure of the Website.
* CSS
	* This project uses custom written CSS to style the Website.
* Flask
    * This is used as the main connection between frontend and backend
* Python
    * This is used as the backend of the project
* Postgresql
    * This is used as database for Users and Categories 
* [MongoDB](https://www.mongodb.com/)
    * This is used as database for Recipes details (name, ingrediets, cooking steps, cooking time, preparation time, owner of the recipe)
* [Materialize](https://materializecss.com/)
    * This is used as frontend framework to display the content in an organized way
* [Font Awesome](https://fontawesome.com/)
	* Font awesome Icons are used for the Social media links contained in the Footer section of the website
* [Google Fonts](https://fonts.google.com/)
	* Google fonts are used throughout the project to import the *Spectral* and *Lora* fonts.
* [Gitpod](https://gitpod.io/)
	* Gitpod is the tool used to develop the Website.
* [GitHub](https://github.com/)
	* GithHub is the hosting site used to store the source code for the Website
* [Git](https://git-scm.com/)
	* Git is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [Heroku](https://dashboard.heroku.com/)
    * Heroku is used to deploy the web app
* [Pixlr](https://pixlr.com/)
	* Pixlr is used to reduce the file sizes of images before being deployed to reduce storage and bandwith.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
	* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
* [Coolors](https://coolors.co/)
    * This was used to select color palette. 
* [Techsini](http://techsini.com/multi-mockup/index.php)
    * tecnisih.com Multi Device Website Mockup Generator was used to create the Mock up image in this README.
* [Favicon](https://favicon.io/)
    * This was used to generate the icon on browser's tab.
***

## Testing

-   ### Test Strategy 

    -   #### Summary 

        Manual testing will be done on three different browsers (Chrome, Firefox, Opera)
	    Testing will be done for:
		- Website name in the navbar redirects to home page
		- Home page links redirect to create recipe or recipes pages
		- Registration page to register unique users
			- all fields are filled in
			- password confirmation to match the password
			- link to redirect to login page
		- Login page to log in only existing users
			- display a flas message if no username or wrong username or password
			- link to redirect to register page
		- Profile page to display name of the logged in user
			- display the user's created recipes
			- buttons to edit/delete recipe
		- Recipes page to display a full list of recipes
			- show edit/delete buttons only on recipes created by logged in user
		- Create recipe page display a form to be filled in with all required fields
		- Edit recipe page will display the recipes details with possibility to change and save the changes
		- Log out link in the navbar to remove current user from session
		- Admin category page to be displayed in the navbar
			- a list of categories dispalyed on the category page
			- a button to create new categories must be at the top of the page 
			and redirect to create category page
			- edit / delete buttons for each category
		- Footer links open the urls in new browser tabs

        - The live Project can be found [here](https://food-fiesta-ms3.herokuapp.com/).</br>

    -   ### Test Results

    - All Pages were run through the [W3C HTML Validator](https://validator.w3.org/) and showed no errors.<br>
    ![html-validation]()<br>


    - CSS Stylesheet was run through the [W3C CSS Validator]() and showed no errors.<br>
    ![css-validation]()<br>

    - Website was tested by running locally and tested on the deployed version on three different browsers:
        - Google Chrome: no differences found
        - Opera: no differences found
        - Mozilla Firefox: <br>
    - Test header's logo to redirect to home.html (on all pages) - worked as expected on all tested browsers

    - Navbar displays: 
        - "Home, Log in, Register" for general users => work as expected
	    - "Home, Recipes, Create Recipe, Profile, Log out" for standard logged in user => work as expected
		- "Home, Recipes, Categories, Create Recipe, Profile, Log out" for admin logged in user => work as expected

    - Navbar on mobile: 
        - becomes dropdown list under a "burger" icon  => work as expected
		- has the same elements like the navbar on large screens  => work as expected

    - Home page has two images with links:
        - first link redirect logged in user to -> Create Recipe  => work as expected
        - if user not logged in -> flash message "You must be logged in to create a recipe
            and redirects user to recipes page  => work as expected
        - second link redirect user to recipes page  => work as expected

    - Register form:
	    - fields must be filled in to submit the form
		- if successfully registered redirect user to profile page  
            => work as expected
		- try try submit with no values -> each field if has no value displays required message 
            => work as expected
		- try submit with password and confirm password not matching 
            -> flash message dispalyed at the top of the page "Password does not match" 
                => work as expected
		- try submit with wrong email format -> format matching error  
            => work as expected
		- try submit username already registered -> flash message "Username already exists" 
            => work as expected
		- reload the page after failed submission 
            => work as expected
	- click on the "Log in" link at the bottom -> redirect user to login page 
        => work as expected

    - Login form:
	    - fields must be filled in to submit the form
		- if successfully logged in redirect user to profile page  
            => work as expected
		- try submit with no values -> username field require message popup 
            => work as expected
		- try submit with username but no password -> password field require message popup 
            => work as expected
		- try submit username not registered in db 
            -> flash message displayed at the top of the page 
				"Wrong username or/and password" 
                  => work as expected
		- try submit wrong password 
            -> flash message displayed at the top of the page
				"Wrong username or/and password" 
                    => work as expected

	- click on the "Click here" should redirect user to register page
         => work as expected

    - Profile page
        - display a list of recipes created by logged in user  
            => work as expected
	    - options to edit or create each recipe  
            => work as expected

    - Recipes page
        - display a list of all recipes found in db 
            => work as expected
        - edit and delete options only for the recipes created by logged in user  
            => work as expected

    - Create recipe page
        - display a form to be filled in with : 
            - Category (limited to existing categories - dropdown list)
			- Recipe name (required)
			- Servings (required)
			- Preparation time (required)
			- Cooking time (required)
			- Total time (autofill - requred - can be modified)
			- Ingredients field (must contain a value)
			- Preparation steps (must contain a value)
			- Button Add Ingredient (add ingredient to recipe ingredients list)
			- Button Add Step ( add preparation step to recipe steps list)
	    => all work as expected

    - Log out
        - removes logged in user from session and redirect to Login page
            with flash message : "You have been logged out"  
                => work as expected

    - Admin only - Categories page
	    - Add category button opens a new form with one input
	    - display categories if exist in db 
	    - each category has Edit and Delete buttons
	    - Edit category - category name can be edited and saved to db
	    - Delete category - delete category from the db
        => all work as expected

    -Footer: 
        - is the same on all website pages
	    - links to social media open new tab 
	    => all work as expected

### Issues and Resolutions to issues found during testing
 - Total time on the create_recipe form was not live updated:
    - I created a new js function (totalTime()) to get cook_time and prep_time values from the form 
    and set the addition of them to the form's total_time value

- On the Create Recipe form, when user added new ingredient or new preparation step, they were displayed as duplicated values
    - I made the ingredients[] and stepsList{} global variables and cleared the displayed text before iterate through them

- The navbar links were displayed all the time for all users
    - I put condition in base.html to be displayed depending on logged in user
        - if not log in Home, LogIn and Register links are displayed
        - if logged in as standard user Create recipe will be displayed as well
        - if logged in as admin Categories is displayd as well

- Categories could be modified by any user if accessed via direct link
    - add conditional statement to be admin in order to modify the Categories in any way

- Edit Recipe page was not displaying the name of the recipe category
    - in the category selector in if statement I had to cast the value returned from mongo db into 'int'
    to match the type returned from postgreSQL

- When a category was deleted all the recipes created with that respective category changed their category name to next available in the list
    - in delete_category() I added a statement to delete from db all the recipes related to the deleted category


***
## Deployment

This project was developed using a [GitPod](https://gitpod.io/ "Link to GitPod") workspace. The code was committed to [Git](https://git-scm.com/ "Link to Git") and pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the env and __init__.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the __init__.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths..
    - In env.py add the following (with values):
        - "IP"
        - "PORT"
        - "DEBUG"
        - "DEVELOPMENT"
        - "SECRET_KEY"
        - "MONGO_URI"
        - "MONGO_DBNAME"
        - "DB_URL"
    - in Heroku config var add the same variable with values

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, storage, and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.WSGI
    - Log in to Heroku using the terminal Heroku login -i.
    - Then run the following command: **heroku git:remote -a your_app_name_here** and replace your_app_name_here with the name of your Heroku app. This will link the app to your Gitpod terminal.
    - After linking your app to your workspace, you can then deploy new versions of the app by running the command **git push heroku main** and your app will be deployed to Heroku.


-   ### Project Creation
The project was started by navigating to the [template](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking 'Use this template'. Under Repository name I input "Food-Fiesta" and checked the Include all branches checkbox. I then navigated to the new [repository](https://github.com/BogdanCatalin-Iacob/Food-Fiesta). I then clicked the Gitpod button to open the project in Gitpod.

 The following commands were used throughout the project:

* git add filename - This command was used to add fils to the staging area before commiting.
* git commit -m *commit message explaining the updates* - This command was used to to commit changes to the local repository.
* git push - This command is used to push all commited changes to the GitHub repository. 

-   ### Using Heroku


-   ### Run Locally
1. Navigate to the GitHub [Repository:](https://github.com/BogdanCatalin-Iacob/mFood-Fiesta)
1. Click the Code drop down menu.
1. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
1. Open your developement editor of choice and open a terminal window in a directory of your choice.
1. Use the 'git clone' command in terminal followed by the copied git URL.
1. A clone of the project will be created locally on your machine.

***
## Credits
-   ### Code
   - The code for validate materialize select was taken from [codeinstitute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/6449dcd23ca14016aa83dc7313d91a02/?child=first)
   - The code for sticky footer was taken from Materializecss (https://materializecss.com/footer.html) 

-   ### Content
    

-   ### Media
    - Image for recipes link was taken from[unsplash](https://unsplash.com/photos/uB7q7aipU2o)
    - Image for recipes link was taken from[unsplash](https://unsplash.com/photos/KJOUnsGXq58)

-   ### Acknowledgements
    - I'd like to thank my mentor Daisy McGirr for her guidance throughout my project.<br>