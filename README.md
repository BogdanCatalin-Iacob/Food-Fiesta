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

The live website can be found [here]().
![Website Mock Up]()

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals
        1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the organisation.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        3. As a First Time user, I want to view the website and content clearly on my mobile device.

    -   #### Returning Visitor Goals
        1. As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.
        2. As a Returning Visitor, I want to find community links.

    -   #### Frequent User Goals
        1. As a Frequent User, I want to be able to see and edit my recipes.

-   ### Structure


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
* MongoDB
    * This is used as database for Recipes details (name, ingrediets, cooking steps, cooking time, preparation time, owner of the recipe)
* Materialize
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

      
        - The live Project can be found [here]().</br>

    -   ### Test Results

    - All Pages were run through the [W3C HTML Validator](https://validator.w3.org/) and showed no errors.<br>
    ![html-validation]()<br>
    ![html-validation]()<br>

    - CSS Stylesheet was run through the [W3C CSS Validator]() and showed no errors.<br>
    ![css-validation]()<br>

    - Website was tested by running locally and tested on the deployed version on three different browsers:
        - Google Chrome: no differences found
        - Opera: no differences found
        - Mozilla Firefox: <br>
    - Test header's logo to redirect to index.html (on all pages) - worked as expected on all tested browsers

    
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

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - Cloudinary to the INSTALLED_APPS list
        - STATICFILE_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

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
    - Image for recipes link was taken from[unsplash](https://unsplash.com/photos/-bLkT8wGV0I)

-   ### Acknowledgements
    - I'd like to thank my mentor Daisy McGirr for her guidance throughout my project.<br>