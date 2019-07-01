import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://root:31Wirpbj6677@cookery-website-xysxa.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("list_recipes.html", recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", difficulty=mongo.db.difficulty.find(), cuisines=mongo.db.cuisine_type.find(), principle_ingredients=mongo.db.principle_ingredient.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines =  mongo.db.cuisine_type.find()
    return render_template('view_recipe.html', recipe=the_recipe, cuisines=all_cuisines)
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines =  mongo.db.cuisine_type.find()
    all_principles =  mongo.db.principle_ingredients.find()
    all_difficulties = mongo.db.difficulty_levels.find()
    return render_template('edit_recipe.html', recipe=the_recipe, cuisines=all_cuisines, principles=all_principles, difficulties=all_difficulties)

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes =  mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)}, 
    {'recipe_name': request.form.get('recipe_name')},
    {'cuisine_type': request.form.get('cuisine_type')},
    {'servings': request.form.get('servings')},
    {'prep_time': request.form.get('prep_time')},
    {'cook_time': request.form.get('cook_time')},
    {'calories_per_serve': request.form.get('calories_per_serve')},
    {'difficulty': request.form.get('difficulty')},
    {'blurb': request.form.get('blurb')},
    {'isfreezable': request.form.get('isfreezable')},
    {'ishealthy': request.form.get('ishealthy')},
    {'isvegan': request.form.get('isvegan')},
    {'isvegetarian': request.form.get('isvegetarian')},
    {'ingredients': request.form.get('ingredients')},
    {'method': request.form.get('method')},
    {'principle_ingredient': request.form.get('principle_ingredient')})
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

