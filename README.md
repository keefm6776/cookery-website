# MODULE 8 (Data Centric Development) PROJECT - Code Institute Full Stack Developer Diploma
# Recipe Website

## BRIEF

CREATE AN ONLINE COOKBOOK

Create a web application that allows users to store and easily access cooking recipes.

Put some effort into designing a database schema based on recipes, and any other related properties and entitites
(e.e views, upvotes, ingredietns, recipe authors, allergens, author's country of origin, cuisine etc...).
Make sure to put some thought into the relationships between them, and use either forreign keys (in the case of
a relational database) or nesting (in the case of a document store) to connect these pieces of data.

Create the backend code and frontend to allow users to add new recipes to the site (at least a basic one, if you 
havent taken the frontend course)

Create the backend code to group and summerise the recipes on the site, based on their attributes such as cuisine,
country of origin, allergens, ingredients etc. and a frontend page to show this summary, and make the categories 
clickable to drill down into a filtered based on that category.  This frontend page can be as simple or as complex
as you'd like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about
if you took the frontend modules) for visualisation.

Create the backend code to retrieve a list of recipes based on various criteria (eg allergens, cuisine, etc) and order
them baseon some reasonable aspect (eg number of views or upvotes).  Create a frontend page to display these, and to 
show some summary statistics around the list (e.g. number of matching recipes, number of new recipes.  Optionally, add
support for pagination, when the number of results is large)

Create a detailed view for each recipe, that wwould just show all attributes for that recipe, and the full preparation
instrcutions.

Allow for editing and deleting of the recipe records, either on  seperate pages, or built into the list/detail pages.

Optionally, you may choose to add basic user registration and authentication to the site.  This can be as simple as
adding a username field to the recipe creation form, without a password (for this project only, this is not expected 
to be secure)

## CHOSEN PROJECT

I decided that this is not a project that requires relational database integrity, and in fact that using this method might
frustrate the user, especially in early its early days.  Instead I decided to use MongoDB and employ this project as a 
document store.

This project has been based on cuisines of the world, that would allow users from across the planet share their local
cuisines with each other.  Each recipe will be categorised by cuisine, difficulty and principle ingredient.  Each of these
categories will be predermined from a MongoDB collection, so that they can be filtered on effectively.

## User Stories

Before Starting, I started to create some user stories:

	1.	As a User I want to be able to add my recipes for others to enjoy, and edit them as required.
	2.	As a User I want to be able to delete any unwanted recipes.
	3.	As a User I want to be able to view the recipes that are on the site.
	2.	As a User I want to be able to look for a recipe based on a main ingredient, which I have at my disposal.
	3.	AS a User I want to be able to look for a recipe based on a cuisine type, which I happen to fancy that day.
	4.	As a User I want to be able to look for a recipe based on how diffcult it is, to make sure I am able to complete it.

## Database Design

Before starting this project, I researched various Recipe website that are on the web, as mentioned in Credits -> Content,
Below.  I then set about drawing up a database schema.  Initially I worked on a SQL based project, but realised that this 
project would work better for the user as a documnet store, in MongoDB.  My initial designs are included in the Database Design
Directory.

## UX

As part of the development process I mocked up wireframes of my recipe site before starting:

See my repository's file list:

Wireframe List Recipes.pdf
Wireframe Filter By.pdf
Wireframe Manage Cuisines.pdf
Wireframe Add or Edit Content.pdf

Which are located in the Wireframe directory.


## Features

				1.	From each menu, the user can add a recipe to the database.
				2.	From each menu, the user can list all the recipes in the database.
				3.	From each menu, the user can filter the recipes by the allocated cuisine type.
				4.	From each menu, the user can filter the recipes by the allocated difficulty level.
				5.	From each menu, the user can filter the recipes by the allocated principle ingredient.
				6.	From each menu the user can manage the lists presented for the filters and as options in the addr recipe form.
				7.	Each record in each collection is presented to the user in a card format, and each instance has a button to
					edit, delete or view the recipe clicked on.
				
				

## Features Left To Implement

                1.	User registration to automate the contributed by field and to filter out user's own recipes.
                2.	User registration to limit the people who can manage the cuisine, difficulty and principle ingredient lists.

## Technologies Used

				1.	AWS CLOUD 9	    -   All the HTML/CSS/JAVASCRIPT/PYTHON was edited using AWS CLOUD 9.
	
				2.	HTML 5 		    -   The structure of the page has been created in HTML5.

				3.	CSS 3	        -   The pages were styled using SS3.

				4.	FLEXBOX	        -   Flexbox was used to centre buttons and titles.

				5.	FONT AWESOME    -   Font Awesome was used to provide the icons throughout the project, as required.
				
				6.  JAVASCRIPT      -   Javascript Was used by Materialize and JQuery, to operate and to initialise.
										Javascript was also used to provide an exit button on the view recipe form.
				
				7.  JQUERY 3.3.1    -   JQuery was used in the operation of menus.
				
				8.	MATERIALIAZECSS -	I used Materialize to provide the base them for my site.  It also provided the grid
										feature for responsiveness.  
				
				10. MONGODB			-	I used MongoDB as the document store to keep all the information required for this
										project to run.  This included the main recipe collection to store all the information 
										for each recipe, but also the cuisine, difficulty and principle ingredient lists that
										were required for the dropboxes in add/edit and in the filter options, so to keep these
										items consistent so that the filtering would work correctly.
				
				9.  Google Chrome Developer Tools - Used To Test While Developing, checking output and values during processing.  
													Testing Functions during development, general tesing of website responsiveness
				
				10. Git/GitHub		-	Used for version control with regular commits.
				
				11. Heroku          -   Used to deploy the project.

## Git Commits

I have made regular Git Commits during my project for version control and also to allow myself to go back if anything went wrong. 
I have pushed each of these commits to GitHub, so that the progress of my project can be reviewed.  I folowed the steps provided by
the GitHub site, which were:

				1.	I set up a page in AWS Cloud 9
				2.	In the terminal I typed "git init", to initialise the repository
				3.	I then created a requirements.txt file using the command: sudo pip3 freeze --local > requirements.txt
				4.  I then created my Procfile by the command: echo web : python app.py > Procfile
				3.	To add files to be committed, I typed "git add ."
				4.  To check that these files were staged, I typed "git status" (staged files should be in green font)
				5.	To commit these to git, the command "git commit -m "messsage"", was used.  With a meaningful message about the commit inside the "".
				6.	To link the my github account, I used the following: git remote add origin https://github.com/keefm6776/cookery-website.git
				7.	To push each commit to github I used : git push -u origin master
				8.	For each subsequent commit I repeated steps 3, 4, 5 & 7.

## Deployment			

I used Heroku to deploy this project by following the steps provided in the CodeInstitute course.  To initialise heroku, these were:

				1.	Create an app in heroku, which has an unique name. In my case cookery-website-flask-mongo
				2.	Next login to heroku through the CLI, using the 'heroku login' and entering your heroku credentials.
				3.  To link heroku to the git repository I used the following: 'heroku git:remote -a cookery-website-flask-mongo
				4.	I then sent the command to get it up and running : heroku ps:scale web=1
				
After each push to git, step 7, I then used the following command to push to Heroku: git push heroku master

In Heroku, I then set the following Config Variables:

				1.	PORT = 5000
				2	IP   = 0.0.0.0

I was then able to open the app, using this button in Heroku.

Before the final deployment of this project, I have set the debug variable to false in app.py, during the run command for app.  I have also
hidden my MONGO_URI using an environment variable of this name, which is used to set this value for the app.

This project has been deployed via Heroku at https://cookery-website-flask-mongo.herokuapp.com/

To run this app locally you need to use the following command : python3 app.py.


## Testing

Each new feature had been tested after each stage of development within the AWS CLOUD 9 environment.  This has included:

				1.	List Recipes         - By checking between MongoDB and my list_recipes screen to make sure that the number of documents in MongoDB
										   and the number on my list recipes page match.  Also by checking that each of the documents is displayed once
								           and that each is there.  I have also checked that the documents are sorted and presented with the newest
								           recipe first.
										   
				2.	Add		             - Each Add feature for recipes, Cusines, difficulties & principle ingredients have been checked to make sure that
										   the document supplied is added to the collection.  I have also checked that the fields match the ones that have
										   been added from the relevant form.  I have also checked that the user is not able to add a blank document.
										   
				3.	Edit			     - Each Edit feature for recipes, Cusines, difficulties & principle ingredients have been checked to make sure that
										   the document that edit is clicked on is the one that shows in the relevant edit screen.  I have also checked that 
										   the various fields match the ones that have retrieved from the document.  I have also checked that when any changes
										   updated then the relevant field(s) are updated in MongoDB.  I have also checked that the user cannot edit a document
										   and update it when it is blank.
										   
				4.  Delete               - Each Delete feature for recipes, Cusines, difficulties & principle ingredients have been checked to make sure that
										   the document that delete is clicked on is the one that is deleted from the collection.  I have also checked that  
										   the screen refreshes to reflect this deltion to the user.
				                           
				5.	Filter by Cuisine	 - I have checked each of the available options for filtering the recipes by their cuisine type.  I have checked that 
										   the number of documents returned matched the number of documents of the selected cuisine in MongoDB.  I have also checked
										   each document to make sure that it is part of that cuisine type.
				                           
				6.	Filter by Difficulty - I have checked each of the available options for filtering the recipes by their difficulty level.  I have checked that 
										   the number of documents returned matched the number of documents of the selected difficulty level in MongoDB.  I have also 
										   checked each document to make sure that it is part of that difficulty level.
				
				7.	Filter by Principle  - I have checked each of the available options for filtering the recipes by their principle ingredient.  I have checked that 
					Ingredient			   the number of documents returned matched the number of documents of the selected principle ingredient in MongoDB.  I have 
										   also checked each document to make sure that it has that principle ingredient.
				
				
After deployment the site has been tested for the above on:

				1.	iPhone 5s on portrait screen (iOS 11 - Safari).
				2.	iPhone 5s on landscape screen. (iOS 11 - Safari)
				3.	iPad Air 2 on portrait screen. (iOS 11 - Safari)
				4.	iPad Air 2 on landscape screen. (iOS 11 - Safari)	
				5.  Samsung Galaxy s9 on portrait screen. (Android 8.0.0 (Oreo) - Samsung Internet)
				6.  Samsung Galaxy s9 on landscape screen. (Android 8.0.0 - (Oreo) - Samsung Internet)
				7. 	Hanns-G 20" widescreen monitor. (Windows 10 - Google Chrome 74.0.3729.108, Firefox 66.0.3, MS Edge 42.17134.1.0, Opera 60.0.3255.56)
				
I have covered all the main browsers on the most common platforms with this testing.  I have found that they were all responsive to orientation when applicable, 
and the site ran as expected in all these scenarios.  However, I did find that the manage lists option was missing on a tablet in landscape mode, obviously too big
to have the mobile menu and too small to include this option (More Below).  I was unable to test Internet Explorer because it would not run on my Windows 10 computer, 
but I am not particularly concerned as this has a very low market share from between 3-4% from the stats quoted on Wikipedia.  At this stage this share would only be 
decreasing with desktop computers being on the decline and Windows 10 taking over this market with MS Edge.  

Resolved Issues:

				1.   I found that the user was able to add a blank document in each of the collections.  I rectified this with "required" tag on each of 
					 the input/select fields.  The user is now prompted when any of the important fields are left blank like name or description etc.  I
					 have made the first 3 ingredients and methods steps required as they will be a minimum to make a recipe, but left the others without 
					 the required tag, in case there is less than 10 ingredients/method steps.
					
			    1.a. After the required field was added, if a select field is left blank the document will not be added or updated.  However the user will not
			    	 be prompted that this is the issue, so might be a bit confusing if all the other fields are filled in correctly.  (Bearing in mind that the
			    	 normal fields will prompt the user to fill them out if they are blank or incorrect)
			    	 
			    2.	 Eaually as above, Edit would allow the user to remove the data from a document and resubmit it as empty, I employed the same required tags here.
			    	 
			    3.	 I found that adding the dynamically filled Filter by options into the menus meant that the display of the cuisines, difficulty levels and
			    	 principle ingredients would not work.  In fact only the main menu would show the dynamic list and it wouldn't display in the mobile menu.
			    	 Equally if I removed the main menu then the mobile menu would work, but the display of cuisines, difficulty levels and
			    	 principle ingredients would not work.  I managed to resolve this issue by the fact that a dictionary can only be iterated once in  Jinja, 
			    	 and I made each dictionary into a list using the list(dict) command, this meant that each list could be iterated over as many times as 
			    	 required and hence solved this problem.
			    
			    4.	 I found that the font for the hero-image text was too large on small screens along with the font used for the name of each section, like 
			    	 "Filtered By Cuisine".  This has been rectified and now renders properly.
			    
			    5.	 I found a major oversight on my part, I failed to include the add recipe link in the mobile menu, which would have meant that the site was 
			         pretty useless for mobile and small screen users!!!  Thankfully testing found this issue and it was a quick fix.
			    
			    6.	 I found that user experience was hindered by not having an exit, add or edit button whilst viewing the recipe.  While I did read that it is 
			    	 acceptable for the exit issue to be solved by the user using the browswer back button, I felt frustrated with the lack of being able to exit
			    	 this page without having to work that out.  Hence I have included these at the bottom of the form.
			    
			    6.a. I later found that these exit buttons were rendering shorter than the other buttons while displayed on mobile screens, however this did not show
			    	 whilst viewing in the IDE.  I later realised that I had not been consistent in the declaration of these buttons, declaring some as buttons and 
			    	 some as links.  I made these consistent which resolved this issue.
			    
			    7.	 As above I found that each edit page ie Recipe, Cusines, Difficulty Levels and Principle Ingredients were hindered by not having an exit option
			    	 which allowed the user to discard changes.  I have included this exit button at the bottom at each of the edit forms.
			    
			    8.	 I also found that the manage Principle Ingredients Screen did not display the name of the card in the display screen.  I found that I had referenced
			         the information incorrectly and was able to correct this.
			    
			    9.	 During testing I found that the Manage Lists option was missing from a tablet in landscape.  In portrait the user is presented with the mobile menu,
			         but in landscape this option disappears from the main menu.  I have altered the font size and removed some of the wording within the main nav bar so 
			         that all the required menu items are visible on this type of screen.
			         
			    10.	 Also during testing, I found that the filter by cuisine listing was rendered in white font which meant that they were not visble against the white 
			    	 background.  I made this consistent by changing the font colour to be consistent with the rest of the menu lists.
			    
Code Validation:

				1.  I have checked my HTML with validator.w3.org, and almost had a full validation.  However an error still remains of:
				    "Error: Start tag body seen but an element of the same type was already open.  From line 68, column 1; to line 68, column 6"
				    I am unable to establish why this error is being shown.
				1a.	The other errors are in relation to the jinja templating and extending of base.html.  The jinja templating was not recognised, and the extends keyword
					meant that the html file didn't have its full structure hence the error.  These errors still remain in the validation tool, however the site renders 
					correctly in regards to these issues.
				2.	I have checked my CSS file with jigsaw.w3.org, and this found no errors in the CSS.
				

## Credits

### Content
				- Before starting this project I looked at various sites recipe based sites, to get a flavour of what is required, these included:
					1.	https://www.bbcgoodfood.com
					2.  https://allrecipes.com
					3.  https://www.delish.com
					4.  https://greatfood.ie
				
				- I obtained the sample recipes for my site from https://www.bbcgoodfood.com.
					

### Acknowledgements

                - Code institute notes for basics on Javascript and JQuery to adapt and base my code on.
                - https://www.w3schools.com/ for information and examples to adapt and base my code on.
                - https://stackoverflow.com/ for information and examples to adapt and base my code on.
                - https://www.bbcgoodfood.com/recipes for sample recipes to include in my site.
                - My Mentor Theo Despoudis - for his general guidance.
                - The CI Tutor Team. (However a special mention for Haley Schafer for her repeated help with different issues.  Each
                  Time she guided me through what I was struggling to do, and kept at it until we got there).