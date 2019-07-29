import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://root:31Wirpbj6677@cookery-website-xysxa.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)

################################################################################### Recipe Operations

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    all_recipes=mongo.db.recipes.find()
    return render_template("list_recipes.html", recipes=all_recipes)

@app.route('/add_recipe')
def add_recipe():
    all_difficulties=mongo.db.difficulty_levels.find()
    all_cuisines=mongo.db.cuisine_type.find()
    all_principles=mongo.db.principle_ingredients.find()
    all_measures=mongo.db.measures.find()
    return render_template("add_recipe.html", difficulties=all_difficulties, cuisines=all_cuisines, principles=all_principles, measures=all_measures)
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    this_recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines=mongo.db.cuisine_type.find()
    return render_template('view_recipe.html', recipe=this_recipe, cuisines=all_cuisines)
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    this_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines =  mongo.db.cuisine_type.find()
    all_principles =  mongo.db.principle_ingredients.find()
    all_difficulties = mongo.db.difficulty_levels.find()
    return render_template('edit_recipe.html', recipe=this_recipe, cuisines=all_cuisines, principles=all_principles, difficulties=all_difficulties)

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes =  mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)}, 
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
    'image_url': request.form.get('image_url')
    })
    return redirect(url_for('get_recipes'))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

######################################################################## Cuisine Operations

    
@app.route('/get_cuisines')
def get_cuisines():
    all_cuisines=mongo.db.cuisine_type.find()
    return render_template("manage_cuisines.html", cuisines=all_cuisines)
    
@app.route('/add_cuisine')
def add_cuisine():
    all_cuisines=mongo.db.cuisine_type.find()
    return render_template("add_cuisine.html", cuisines=all_cuisines)
    
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    this_cuisine =  mongo.db.cuisine_type.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=this_cuisine)
    
@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisine_type.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisines'))
    
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisines = mongo.db.cuisine_type
    cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('get_cuisines'))
    
@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    cuisines =  mongo.db.cuisine_type
    cuisines.update({'_id': ObjectId(cuisine_id)}, 
    {'name': request.form.get('name'),
    'flag_image': request.form.get('flag_image')
    })
    return redirect(url_for('get_cuisines'))

@app.route('/filter_by_cuisine')
def filter_by_cuisine():
    all_cuisines=mongo.db.cuisine_type.find()
    return render_template("filter_by_cuisine.html", cuisines=all_cuisines)

@app.route('/get_cuisine_filtered_recipes')
def get_cuisine_filtered_recipes():
    all_recipes=mongo.db.recipes.find()
    
    return render_template("display_by_cuisine_filter.html", recipes=all_recipes, cuisine_type=cuisine_filter)

######################################################################## Principle Ingredient Operations

@app.route('/get_principles')
def get_principles():
    all_principles=mongo.db.principle_ingredients.find()
    return render_template("manage_principles.html", principles=all_principles)
    
@app.route('/delete_principle/<principle_id>')
def delete_principle(principle_id):
    mongo.db.principle_ingredients.remove({'_id': ObjectId(principle_id)})
    return redirect(url_for('get_principles'))
    
@app.route('/add_principle')
def add_principle():
    all_principles=mongo.db.principle_ingredients.find()
    return render_template("add_principle.html", principles=all_principles)
    
@app.route('/insert_principle', methods=['POST'])
def insert_principle():
    principles = mongo.db.principle_ingredients
    principles.insert_one(request.form.to_dict())
    return redirect(url_for('get_principles'))
    
@app.route('/edit_principle/<principle_id>')
def edit_principle(principle_id):
    this_principle =  mongo.db.principle_ingredients.find_one({"_id": ObjectId(principle_id)})
    return render_template('edit_principle.html', principle=this_principle)
    
@app.route('/update_principle/<principle_id>', methods=['POST'])
def update_principle(principle_id):
    principles =  mongo.db.principle_ingredients
    principles.update({'_id': ObjectId(principle_id)}, 
    {'name': request.form.get('name'),
    'image_url': request.form.get('image_url')
    })
    return redirect(url_for('get_principles'))

    

######################################################################## Principle Ingredient Operations

@app.route('/get_difficulties')
def get_difficulties():
    all_difficulties=mongo.db.difficulty_levels.find()
    return render_template("manage_difficulties.html", difficulties=all_difficulties)
    
@app.route('/delete_difficulty/<difficulty_id>')
def delete_difficulty(difficulty_id):
    mongo.db.difficulty_levels.remove({'_id': ObjectId(difficulty_id)})
    return redirect(url_for('get_difficulties'))

@app.route('/add_difficulty')
def add_difficulty():
    all_difficulties=mongo.db.difficulty_levels.find()
    return render_template("add_difficulty.html", difficulties=all_difficulties)
    
@app.route('/insert_difficulty', methods=['POST'])
def insert_difficulty():
    difficulties = mongo.db.difficulty_levels
    difficulties.insert_one(request.form.to_dict())
    return redirect(url_for('get_difficulties'))
    
@app.route('/edit_difficulty/<difficulty_id>')
def edit_difficulty(difficulty_id):
    this_difficulty =  mongo.db.difficulty_levels.find_one({"_id": ObjectId(difficulty_id)})
    return render_template('edit_difficulty.html', difficulty=this_difficulty)
    
@app.route('/update_difficulty/<difficulty_id>', methods=['POST'])
def update_difficulty(difficulty_id):
    difficulties =  mongo.db.difficulty_levels
    difficulties.update({'_id': ObjectId(difficulty_id)}, 
    {'level': request.form.get('level'),
    'image_url': request.form.get('image_url')
    })
    return redirect(url_for('get_difficulties'))
    
    

#################################################################################################

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

