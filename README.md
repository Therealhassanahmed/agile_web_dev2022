# agile_web_dev2022

### Description of repository:

A collaborative repository for the development of our web application (A higher/lower guessing game based on global city populations)

### Front-end description:

The front-end of this project utilizes all of the following technologies: 
- HMTL
- CSS
- JAVASCRIPT
- PYTHON
- BOOTSTRAP

##### STYLES
The styling was done in a way to emphasise strong colours and fluid animations on buttons/menus.
The vast majority of styling is found in "app/static/styles/style.css"
Styling focused on using the theme of yellow+black as well as smooth transition effects.

##### JAVASCRIPT
The javascript can be found imbedded within the html files with respect to the template they work for.
The majority of javascript utilizes the DocumentObjectModel too access objects through their ID's.
With access, the styling of those objects are changed on button clicks and hovers.
A majority of javascript functions have bodies which alter the display style of objects.
This is an easy way to have objects disappear (display: none).
And then to re-appear (display: block/flex).
This is how the pop-ups (eg. login) were implemented.

##### FONT-AWESOME
The font-awesome library was used to get icons for the web-page.
Icons such as close buttons, and list buttons were used.

##### TEMPLATES
The main template is index.html which contains login, leaderboards and various other links.
register.html contains the register form which adds accounts to the database.
about.html contains information regarding the game/website/developers.
There are 3 gaming templates, those being easy.html, normal.html, hard.hmtl.
They all contains a version of the higher or lower game corresponding to it's difficulty levels.

##### SMALL-SCREENS
For changes when the screen is small (<700px), @media was used.
This allowed for style changes to automatically change at the necessary screen size. A feature that accomodates mobile-phone users as well as Desktop users.

------------------------------------------------------------------------------------------------------------------------------------------------------

### Back-end descrtiption:

##### DATABASE
 The database contains 2 tables: one for user data and one for population data.
 The user model contains an id which is an auto-generated integer; a username, email and password that are strings
 provided by registering users and integer high scores for each of the difficulties that are managed by the game but
 are up to the users to post when they achieve a high score.
 The other table in the database contains the data for each city and its corresponding country and population.
 The city and country are strings and the population is stored as an integer.
 This data was scraped from worldpopulationreview.com who I believed to have the most consistent data in terms
 of defining city borders. When the app is run the database is migrated into the app.

 ##### REGISTRATION & LOGIN
 When the user accesses the registration or login page a form is created which the user is required to fill out with their
 account details (username, email, password). Once the user posts this data the database gets updated with the new user
 or if its an existing user accessing the login page it will login the user.
 If the user incorrectly fills out the form they are prompted with a helpful error message and the form is discarded.
 When the app is run the LoginManager is created.

 ##### GAME
 The game utilises an sqlite database that contains user data as well as the population data that the game draws from.
 When the user accesses the game a query is run to obtain the data for all (top 100/500 for easy/normal difficulty) of the
 city populations. This query results gets passed through python functions that splits it up into three arrays for
 cities,countries,populations. These arrays are what are passed into the game where the rest is done through javascript.
 A request form is also created when a user accesses the game. When the user posts their highscore it gets stored in this
 form which is used to update the users highscore in the database. The leaderboards are routinely updated and constantly
 show the top 5 scores for each difficulty which is managed through querying the top 5 scores in the database.

