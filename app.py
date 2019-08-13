import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_SAVED_URI')

mongo = PyMongo(app)

################################################################################### Recipe Operations

def menu_info():
    global all_principles, all_difficulties, all_cuisines
    all_principles = list(mongo.db.principle_ingredients.find())    #get all principle ingredients for menu
    all_difficulties = list(mongo.db.difficulty_levels.find())    #get all difficulty levels for menu
    all_cuisines=list(mongo.db.cuisine_type.find())               #get all cuisines for menu
    return 

@app.route('/')
def get_recipes():
    menu_info()
    all_recipes=list(mongo.db.recipes.find())                     #get list of all recipes in the collection
    all_recipes.sort(key=lambda item:item['added'], reverse=True) #sort recipes by date, so newest recipe is shown first
    length_recipes = len(all_recipes)                             #calculate length of recipes list for info on how many displayed
    return render_template("/display/list_recipes.html", recipes=all_recipes, manage_cuisines=all_cuisines,\
    cuisines=all_cuisines, principles=all_principles, difficulties=all_difficulties, length_recipes=length_recipes)
    # List all recipes collected from Mongo

@app.route('/add_recipe')
def add_recipe():
    menu_info()                                                     # retrieve lists for menus from Mongo
    return render_template("/add/add_recipe.html", difficulties=all_difficulties, manage_cuisines=all_cuisines, \
    cuisines=all_cuisines, principles=all_principles)
    # Display add recipe form to user
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes                                      # set recipes as recipes collection 
    now = datetime.now()                                            # make now the time & date of now
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")                 # convert above into string format
    date_dictionary = {'added': date_string}                        # convert string to dictionary
    document_dict = request.form.to_dict()                          # get inputs of add recipe form into dictionary
    document_dict.update(date_dictionary)                           # add the now dictionary to the above (used for sorting recipes)
    recipes.insert_one(document_dict)                               # insert the combined dictionary into recipes
    return redirect(url_for('get_recipes'))
    # Insert the recipe inputted by user including the date&time that it was added
    
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    this_recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})  #find current recipe
    menu_info()                                                     # retrieve lists for menus from Mongo
    return render_template('view_recipe.html', recipe=this_recipe, manage_cuisines=all_cuisines, cuisines=all_cuisines, \
    principles=all_principles, difficulties=all_difficulties)
    # Show recipe to user using view_recipe page
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    this_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}) #find recipe being edited in Mongo
    menu_info()                                                     # retrieve lists for menus from Mongo
    return render_template('/edit/edit_recipe.html', recipe=this_recipe, cuisines=all_cuisines, \
    manage_cuisines=all_cuisines, principles=all_principles, difficulties=all_difficulties)
    # display current recipe fields, allowing user to edit them

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes =  mongo.db.recipes                                     #set recipes to recipe being updated after edit
    recipes.update({'_id': ObjectId(recipe_id)},                    #update field list from edit form
    {'recipe_name': request.form.get('recipe_name'),
    'cuisine_type': request.form.get('cuisine_type'),
    'servings': request.form.get('servings'),
    'prep_time': request.form.get('prep_time'),
    'cook_time': request.form.get('cook_time'),
    'calories_per_serve': request.form.get('calories_per_serve'),
    'difficulty': request.form.get('difficulty'),
    'blurb': request.form.get('blurb'),
    'isfreezable': request.form.get('isfreezable'),
    'ishealthy': request.form.get('ishealthy'),
    'isvegan': request.form.get('isvegan'),
    'isvegetarian': request.form.get('isvegetarian'),
    'ingredient1': request.form.get('ingredient1'),
    'measure1': request.form.get('measure1'),
    'quantity1': request.form.get('quantity1'),
    'ingredient2': request.form.get('ingredient2'),
    'measure2': request.form.get('measure2'),
    'quantity2': request.form.get('quantity2'),
    'ingredient3': request.form.get('ingredient3'),
    'measure3': request.form.get('measure3'),
    'quantity3': request.form.get('quantity3'),
    'ingredient4': request.form.get('ingredient4'),
    'measure4': request.form.get('measure4'),
    'quantity4': request.form.get('quantity4'),
    'ingredient5': request.form.get('ingredient5'),
    'measure5': request.form.get('measure5'),
    'quantity5': request.form.get('quantity5'),
    'ingredient6': request.form.get('ingredient6'),
    'measure6': request.form.get('measure6'),
    'quantity6': request.form.get('quantity6'),
    'ingredient7': request.form.get('ingredient7'),
    'measure7': request.form.get('measure7'),
    'quantity7': request.form.get('quantity7'),
    'ingredient8': request.form.get('ingredient8'),
    'measure8': request.form.get('measure8'),
    'quantity8': request.form.get('quantity8'),
    'ingredient9': request.form.get('ingredient9'),
    'measure9': request.form.get('measure9'),
    'quantity9': request.form.get('quantity9'),
    'ingredient10': request.form.get('ingredient10'),
    'measure10': request.form.get('measure10'),
    'quantity10': request.form.get('quantity10'),
    'method1': request.form.get('method1'),
    'method2': request.form.get('method2'),
    'method3': request.form.get('method3'),
    'method4': request.form.get('method4'),
    'method5': request.form.get('method5'),
    'method6': request.form.get('method6'),
    'method7': request.form.get('method7'),
    'method8': request.form.get('method8'),
    'method9': request.form.get('method9'),
    'method10': request.form.get('method10'),
    'principle_ingredient': request.form.get('principle_ingredient'),
    'contributor': request.form.get('contributor'),
    'image_url': request.form.get('image_url'),
    'added' : request.form.get('added')
    })
    return redirect(url_for('get_recipes'))
    # re-display updated recipe listing

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})                       #delete selected recipe
    return redirect(url_for('get_recipes'))
    # re-display updated recipe listing

######################################################################## Cuisine Operations


@app.route('/get_cuisines')
def get_cuisines():
    menu_info()                                                                # retrieve lists for menus from Mongo
    return render_template("/manage/manage_cuisines.html", cuisines=all_cuisines, \
    principles=all_principles, difficulties=all_difficulties)
    # re-display updated cuisine listing

@app.route('/add_cuisine')
def add_cuisine():
    menu_info()                                                                     # retrieve lists for menus from Mongo
    return render_template("/add/add_cuisine.html", cuisines=all_cuisines, manage_cuisines=all_cuisines, principles=all_principles, difficulties=all_difficulties)
    # display add_cuisine form to user
    
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    this_cuisine =  mongo.db.cuisine_type.find_one({"_id": ObjectId(cuisine_id)})   # find cuisine type rquired to edit
    menu_info()                                                                     # retrieve lists for menus from Mongo
    return render_template("edit/edit_cuisine.html", cuisine=this_cuisine, cuisines=all_cuisines, manage_cuisines=all_cuisines, principles=all_principles, difficulties=all_difficulties)
    # display current values of selected cuisine to user via edit_cuisine form
    
@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisine_type.remove({'_id': ObjectId(cuisine_id)})                     # delete required cusine document
    return redirect(url_for('get_cuisines'))
    #re-display updated cuisine listing
    
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisines = mongo.db.cuisine_type                                                # set cusines to cusine collection
    cuisines.insert_one(request.form.to_dict())                                     # insert recipe from fields in add form                     
    return redirect(url_for('get_cuisines'))                                        # re-display cuisine listing
    
@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    cuisines =  mongo.db.cuisine_type                                               # find edited cusine in Mongo
    cuisines.update({'_id': ObjectId(cuisine_id)},                                  # update document
    {'name': request.form.get('name'),
    'flag_image': request.form.get('flag_image')
    })
    return redirect(url_for('get_cuisines'))
    # re-diplay updated cuisine listing

@app.route('/get_cuisine_filtered_recipes/<cuisine_filter>', methods=['POST','GET'])
def get_cuisine_filtered_recipes(cuisine_filter):
    all_recipes=list(mongo.db.recipes.find())                                       # find all documents in recipes
    all_recipes.sort(key=lambda item:item['added'], reverse=True)                   # sort by date/time added
    menu_info()                                                                     # retrieve lists for menus from Mongo
    filtered_recipes=list(filter(lambda x:x['cuisine_type']==cuisine_filter, all_recipes)) #filter for desirec cuisine type filter
    length_filtered_recipes=len(filtered_recipes)                                   # calculate documents in listing for user
    return render_template("display/display_by_cuisine_filter.html", recipes=filtered_recipes, cuisine_filter=cuisine_filter, cuisines=all_cuisines, manage_cuisines=all_cuisines, principles=all_principles, difficulties=all_difficulties, length_recipes=length_filtered_recipes)
    # display list of filter cuisines to user

######################################################################## Principle Ingredient Operations

@app.route('/get_principles')
def get_principles():
    menu_info()                                                                     #retrieve lists for menus
    return render_template("/manage/manage_principles.html", cuisines=all_cuisines, principles=all_principles, difficulties=all_difficulties)

@app.route('/delete_principle/<principle_id>')
def delete_principle(principle_id):
    mongo.db.principle_ingredients.remove({'_id': ObjectId(principle_id)})          #delete selected principle ingredient
    return redirect(url_for('get_principles'))
    
@app.route('/add_principle')
def add_principle():
    menu_info()                                                                     #retrieve lists for menus
    return render_template("add/add_principle.html", principles=all_principles, cuisines=all_cuisines, difficulties=all_difficulties)
    #display add principle ingredient form to user
    
@app.route('/insert_principle', methods=['POST'])
def insert_principle():                                                     
    principles = mongo.db.principle_ingredients                                # set principles to priinciple ingredients collection
    principles.insert_one(request.form.to_dict())                               # insert new principle ingredient from add form
    return redirect(url_for('get_principles'))
    
@app.route('/edit_principle/<principle_id>')
def edit_principle(principle_id):
    this_principle =  mongo.db.principle_ingredients.find_one({"_id": ObjectId(principle_id)})  #find required principel ingredient to edit
    menu_info()                                                                 # retrieve lists for menus
    return render_template('edit/edit_principle.html', principle=this_principle, principles=all_principles, cuisines=all_cuisines, difficulties=all_difficulties)
    # display current principle ingredient values to user in edit form
    
@app.route('/update_principle/<principle_id>', methods=['POST'])
def update_principle(principle_id):
    principles = mongo.db.principle_ingredients                         #set principles to principle ingredient colleciton
    principles.update({'_id': ObjectId(principle_id)},                  # update the edit document to its new values
    {'name': request.form.get('name'),
    'image_url': request.form.get('image_url')})    
    return redirect(url_for('get_principles'))          
    #redisplay upadted princile ingredient list
    
@app.route('/get_principle_filtered_recipes/<principle_filter>', methods=['POST','GET'])
def get_principle_filtered_recipes(principle_filter):
    all_recipes=list(mongo.db.recipes.find())                           #retrieve all recipes in collection
    all_recipes.sort(key=lambda item:item['added'], reverse=True)       #sort recipes by date/time added
    menu_info()                                                         # retrieve menu info
    filtered_recipes=list(filter(lambda x:x['principle_ingredient']==principle_filter, all_recipes)) 
                                                                        # filter recipes by selected principle ingredient
    length_filtered_recipes=len(filtered_recipes)                       # calculate number of documents returned 
    return render_template("display/display_by_principle_filter.html", recipes=filtered_recipes, principle_filter=principle_filter, cuisines=all_cuisines, principles=all_principles, difficulties=all_difficulties,length_recipes=length_filtered_recipes)
    # display filtered listing of principle ingredients to user


######################################################################## Principle Ingredient Operations

@app.route('/get_difficulties')
def get_difficulties():
    menu_info()                                                                 # retrieve lists for menus from Mongo
    return render_template("manage/manage_difficulties.html", difficulties=all_difficulties, cuisines=all_cuisines, principles=all_principles)
    # list current collection of dificulty levels to user
    
@app.route('/delete_difficulty/<difficulty_id>')
def delete_difficulty(difficulty_id):  
    mongo.db.difficulty_levels.remove({'_id': ObjectId(difficulty_id)})         # find & delete selected difficulty document for deletion
    return redirect(url_for('get_difficulties'))
    #re-list updated difficulty level listing

@app.route('/add_difficulty')
def add_difficulty():
    menu_info()                                                                 # retrieve information for menus
    return render_template("add/add_difficulty.html", difficulties=all_difficulties, principles=all_principles, cuisines=all_cuisines)
    #display add difficulty level form to user for input.

@app.route('/insert_difficulty', methods=['POST'])
def insert_difficulty():
    difficulties = mongo.db.difficulty_levels                               #set difficulties to current list of difficulty levels
    difficulties.insert_one(request.form.to_dict())                         #insert new document from user form
    return redirect(url_for('get_difficulties'))
    #redisplay updated list of difficulty level documents
    
@app.route('/edit_difficulty/<difficulty_id>')
def edit_difficulty(difficulty_id):
    this_difficulty =  mongo.db.difficulty_levels.find_one({"_id": ObjectId(difficulty_id)})    #find the required document for editing
    menu_info()                                                                             # retrieve lists for menus from Mongo
    return render_template('edit/edit_difficulty.html', difficulty=this_difficulty, principles=all_principles, cuisines=all_cuisines, difficulties=all_difficulties)
    
@app.route('/update_difficulty/<difficulty_id>', methods=['POST'])
def update_difficulty(difficulty_id):
    difficulties =  mongo.db.difficulty_levels                                          #set difficulties to difficulty_levels collection
    difficulties.update({'_id': ObjectId(difficulty_id)},                           #update edited document to new values from user form
    {'level': request.form.get('level'),
    'image_url': request.form.get('image_url')
    })
    return redirect(url_for('get_difficulties'))
    #redisplay updated list of difficulty documents

@app.route('/get_difficulty_filtered_recipes/<difficulty_filter>', methods=['POST','GET'])
def get_difficulty_filtered_recipes(difficulty_filter):
    menu_info()                                                                     #retrieve lists for menus
    all_recipes=list(mongo.db.recipes.find())                                       #set all_recipes to recipe collection
    all_recipes.sort(key=lambda item:item['added'], reverse=True)                   #sort recipes by date&time added
    filtered_recipes=list(filter(lambda x:x['difficulty']==difficulty_filter, all_recipes)) #filter recipes by selected difficulty level
    length_filtered_recipes=len(filtered_recipes)                                   # calculate number of documents returned
    return render_template("display/display_by_difficulty_filter.html", recipes=filtered_recipes, difficulty_filter=difficulty_filter, cuisines=all_cuisines, principles=all_principles, difficulties=all_difficulties, length_recipes=length_filtered_recipes)
    #display list of recipes filtered by selected difficulty level
    

#################################################################################################

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
