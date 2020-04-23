# Tsundere Inc - Tickets System

[![Build Status](https://travis-ci.org/Robtych121/TsundereInc-MS4.svg?branch=master)](https://travis-ci.org/Robtych121/TsundereInc-MS4)

This project is for the Full Stack Frameworks With Django Milestone Project By Code Institute.

This website was created to allow users to view and create bug tickets, view feature requests and possibly pay some mone towards getting those features done quicker. There is also a simple forum allowing people to discuss bugs/features.

You can view this website via Heroku by clicking this [link](https://tsundereinc.herokuapp.com/).

![Tsundere](/Wireframes/mockup.PNG)

## UX
The website was designed with a simple style to keep things easy for the users when they visit the website. The theme for this is using the Bootswatch Lux Theme.

### User Stories
As a User, I would like to be able to:
- View existing bugs that have been posted as a guest
- View existing feature requests that have been posted as a guest
- Register for an account
- Reset my own password incase I forget it
- See my own profile with personlised stats
- Upvote bugs for free
- Upvote features using my available points balance
- Purchase more points when i want to upvote more features
- Provide feedback to bugs and features via comments
- Post forum posts to share with users
- Search for tickets using the name 

I have created a series of wireframes of the different types of pages that are going to be used. These can be found under the Wireframes folder. 

## Features
The website was designed from the ground up to be specialised in dealing with tickets. To Achieve this i have used an array of different technologies to do this.

The current list of features are as follows:
1. Display Bugs be able to edit/upvote them
2. Display Features and be able to edit/upvote them using points
3. Store functionality using Stripe for payments
4. Personalised Profile page for each user
5. Search functionality that searches on the name of the bug/feature

### Features Left To Implement
There are a few different features that I would have liked to implement, these are:
1. Dashboard showing bugs/features that have been progressed over time.
2. Award and have displayed forum "Titles" for those that regularly post

## Technologies Used
The following technologies were used as part of this project:
### Front End
1. HTML5 - This was used to structure the website
2. CSS3 - This was used to provide styling to the website
3. Bootstrap - This was used to help keep the forms in the same format/style and also to help with making it mobile ready
4. Fontawesome - This was used to create the social media icons in the footer
5. jQuery/JavaScript - Custom JS scripts were used in a few places to help with the functionality of the  website

### Backend
1. PostreSQL - This was used as my main data store for all the information. This is hosted on Heroku's platform
2. SQLite3 - This is used as my local data store while testing the application locally on my machine
3. Python 3 With Django - This was used for the backend logic and routing of the pages, this also is what entered the information into PostreSQL
4. AWS S3 - This was used as asset storage since I am using file uploads and needed a place that wouldn't be cleaned daily.

## Testing
To be able to achieve the user stories for the users/owner, I tested the website during development and also used Travis CI to run some automated tests as well.

#### User Testing
- I was view to existing bugs/features/forums without logging in
- I was able to register for a new account
- I was able to reset my password via the automatic email
- I was able to upvote bugs without purchasing anything
- I wasn't able to upvote a feature without any points
- I was able to purchase more points using Stripe
- I was able to upvote a feature once I had points against my account
- I was able to comment against bugs/features/forums
- I wasn't able to edit a bug or feature once it's completed
- I was able to search for a ticket (bug/feature)
- I was able to see my profile showing my activity

#### Automated Testing (Via Travis CI)
To help with the testing of this project, automated testing using Travis CI is implemented. You can see the current build status at the top of this readme.

#### Mobile Responsive Testing
The responsiveness of the website was tested using Google Devtools and using my own mobile android device (Using Google Chrome).

#### Cross Browser Testing
The website was tested using the following browsers:
1. Google Chrome
2. Firefox
3. Microsoft Edge

#### Code Validators
The website has been tested through the following:
1. W3C HTML Markup Validation Service
2. W3C CSS Validation Service (Jigsaw)
3. JSHint.com to validate the JS script
4. pep8online.com to validate the python

## Deployment
This website is hosted using Heroku, using the master branch from my git repo. Because of this, everytime i push across changes using git, the website is automatically updated without any additional input from myself. When getting the website ready for upload I had to make sure i created a requirements.txt and a Procfile so that the app would run okay with Heroku. To do this, I performed the following actions:

### Github Steps:
1. Within the project folder, i started a empty repo using `git init`
2. Created the .gitignore file to ignore certain files
3. Ran the first git commit using `git add .` and `git commit -m "Initial Commit"`
4. Went to Github and created a repo there and then linked it to my local one using the following command `git remote add origin https://github.com/Robtych121/TsundereInc-MS4.git`
5. Pushed the first commit to Github using `git push -u origin master`

### Heroku Steps:
1. Open up your command terminal and type in the following `pip3 freeze --local > requirements.txt` - this will create the requirements.txt file that is required by Heroku so that it will install all the required libraries
2. Type in the following within the command terminal `echo web: gunicorn django_ticketTracker.wsgi:application > Procfile` - This will create the procfile required by Heroku to run the application properly
3. Commit these files to Git repo and push them to Github by using the commands shown above
4. Login into Heroku's website and create a new app giving it a name and region (in my case tsundereinc and in Europe)
5. Under Deployment method, i connected to Github and connect the Tsundere Inc Repo, it will also ask for which branch to use, i selected the master branch and also enabled automatic deploys so it would rebuild everytime i pushed a commit to the master branch.

If you want to run a copy of this website locally, please follow the following instructions:
1. Within your chosen editor/terminal, run the following command `git clone https://github.com/Robtych121/TsundereInc-MS4.git`
2. Wait until the files have finished copying into your local folder
3. Once finished, run the following command `git remote rm origin`
4. You can now start changing code and commit changes without making changes to this repo.

## Credits
Bootstrap Theme Used - Bootswatch - Lux [link](https://bootswatch.com/lux/)