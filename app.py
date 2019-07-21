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
    return render_template("add_recipe.html", difficulties=all_difficulties, cuisines=all_cuisines, principles=all_principles)
    
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
    'ingredients': request.form.get('ingredients'),
    'method': request.form.get('method'),
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

    
@app.route('/manage_cuisines')
def manage_cuisines():
    all_cuisines=mongo.db.cuisine_type.find()
    return render_template("manage_cuisines.html", cuisines=all_cuisines)
    
@app.route('/add_cuisine')
def add_cuisine():
    all_cuisines=mongo.db.cuisine_type.find()
    return render_template("add_cuisine.html", cuisines=all_cuisines)
    
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    this_cuisine =  mongo.db.recipes.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=this_cuisine)

@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisine_type.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('manage_cuisines'))
    
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisines = mongo.db.cuisine_type
    cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('manage_cuisines'))
    
@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    cuisines =  mongo.db.cuisine_type
    cuisines.update({'_id': ObjectId(cuisine_id)}, 
    {'name': request.form.get('name'),
    'flag_image': request.form.get('flag_image')
    })
    return redirect(url_for('manage_cuisines'))
    
######################################################################## Principle Ingredient Operations

@app.route('/get_principles')
def get_principles():
    all_principles=mongo.db.principle_ingredients.find()
    return render_template("manage_principles.html", principles=all_principles)
    
@app.route('/delete_principle/<principle_id>')
def delete_principle(principle_id):
    mongo.db.principle_ingredients.remove({'_id': ObjectId(principle_id)})
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

#################################################################################################






if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

