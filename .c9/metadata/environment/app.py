{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":59,"position":59,"stack":[[{"start":{"row":10,"column":0},"end":{"row":14,"column":23},"action":"remove","lines":["","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":7}],[{"start":{"row":194,"column":0},"end":{"row":198,"column":23},"action":"insert","lines":["","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":8}],[{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":106,"column":0},"end":{"row":107,"column":0},"action":"insert","lines":["",""]},{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"insert","lines":["",""]},{"start":{"row":108,"column":0},"end":{"row":109,"column":0},"action":"insert","lines":["",""]},{"start":{"row":109,"column":0},"end":{"row":110,"column":0},"action":"insert","lines":["",""]},{"start":{"row":110,"column":0},"end":{"row":111,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":106,"column":0},"end":{"row":107,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"insert","lines":["",""],"id":12}],[{"start":{"row":108,"column":0},"end":{"row":130,"column":43},"action":"insert","lines":["@app.route('/update_recipe/<recipe_id>', methods=['POST'])","def update_recipe(recipe_id):","    recipes =  mongo.db.recipes","    recipes.update({'_id': ObjectId(recipe_id)}, ","    {'recipe_name': request.form.get('recipe_name'),","    'cuisine_type': request.form.get('cuisine_type'),","    'servings': request.form.get('servings'),","    'prep_time': request.form.get('prep_time'),","    'cook_time': request.form.get('cook_time'),","    'calories_per_serve': request.form.get('calories_per_serve'),","    'difficulty': request.form.get('difficulty'),","    'blurb': request.form.get('blurb'),","    'isfreezable': request.form.get('isfreezable'),","    'ishealthy': request.form.get('ishealthy'),","    'isvegan': request.form.get('isvegan'),","    'isvegetarian': request.form.get('isvegetarian'),","    'ingredients': request.form.get('ingredients'),","    'method': request.form.get('method'),","    'principle_ingredient': request.form.get('principle_ingredient'),","    'contributor': request.form.get('contributor'),","    'image_url': request.form.get('image_url')","    })","    return redirect(url_for('get_recipes'))"],"id":13}],[{"start":{"row":114,"column":45},"end":{"row":128,"column":4},"action":"remove","lines":["","    'prep_time': request.form.get('prep_time'),","    'cook_time': request.form.get('cook_time'),","    'calories_per_serve': request.form.get('calories_per_serve'),","    'difficulty': request.form.get('difficulty'),","    'blurb': request.form.get('blurb'),","    'isfreezable': request.form.get('isfreezable'),","    'ishealthy': request.form.get('ishealthy'),","    'isvegan': request.form.get('isvegan'),","    'isvegetarian': request.form.get('isvegetarian'),","    'ingredients': request.form.get('ingredients'),","    'method': request.form.get('method'),","    'principle_ingredient': request.form.get('principle_ingredient'),","    'contributor': request.form.get('contributor'),","    "],"id":14}],[{"start":{"row":114,"column":45},"end":{"row":115,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":115,"column":0},"end":{"row":115,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":119,"column":0},"end":{"row":120,"column":0},"action":"remove","lines":["",""],"id":16},{"start":{"row":119,"column":0},"end":{"row":120,"column":0},"action":"remove","lines":["",""]},{"start":{"row":119,"column":0},"end":{"row":120,"column":0},"action":"remove","lines":["",""]},{"start":{"row":119,"column":0},"end":{"row":120,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":108,"column":0},"end":{"row":108,"column":58},"action":"remove","lines":["@app.route('/update_recipe/<recipe_id>', methods=['POST'])"],"id":17}],[{"start":{"row":109,"column":0},"end":{"row":109,"column":29},"action":"remove","lines":["def update_recipe(recipe_id):"],"id":18}],[{"start":{"row":110,"column":0},"end":{"row":110,"column":31},"action":"remove","lines":["    recipes =  mongo.db.recipes"],"id":19}],[{"start":{"row":111,"column":0},"end":{"row":111,"column":49},"action":"remove","lines":["    recipes.update({'_id': ObjectId(recipe_id)}, "],"id":20}],[{"start":{"row":112,"column":0},"end":{"row":112,"column":52},"action":"remove","lines":["    {'recipe_name': request.form.get('recipe_name'),"],"id":21}],[{"start":{"row":113,"column":0},"end":{"row":113,"column":53},"action":"remove","lines":["    'cuisine_type': request.form.get('cuisine_type'),"],"id":22}],[{"start":{"row":114,"column":0},"end":{"row":114,"column":45},"action":"remove","lines":["    'servings': request.form.get('servings'),"],"id":23}],[{"start":{"row":115,"column":0},"end":{"row":115,"column":46},"action":"remove","lines":["    'image_url': request.form.get('image_url')"],"id":24}],[{"start":{"row":116,"column":0},"end":{"row":116,"column":6},"action":"remove","lines":["    })"],"id":25}],[{"start":{"row":117,"column":4},"end":{"row":117,"column":43},"action":"remove","lines":["return redirect(url_for('get_recipes'))"],"id":26},{"start":{"row":117,"column":0},"end":{"row":117,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""],"id":27},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""],"id":28},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]},{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["",""],"id":29,"ignore":true},{"start":{"row":90,"column":37},"end":{"row":90,"column":41},"action":"remove","lines":["type"]},{"start":{"row":90,"column":37},"end":{"row":90,"column":39},"action":"insert","lines":["id"]},{"start":{"row":91,"column":27},"end":{"row":91,"column":28},"action":"remove","lines":["'"]},{"start":{"row":91,"column":27},"end":{"row":91,"column":28},"action":"insert","lines":["\""]},{"start":{"row":91,"column":45},"end":{"row":91,"column":46},"action":"remove","lines":["'"]},{"start":{"row":91,"column":45},"end":{"row":91,"column":46},"action":"insert","lines":["\""]},{"start":{"row":111,"column":29},"end":{"row":111,"column":33},"action":"remove","lines":["mana"]},{"start":{"row":111,"column":31},"end":{"row":111,"column":32},"action":"insert","lines":["t"]},{"start":{"row":194,"column":0},"end":{"row":198,"column":0},"action":"insert","lines":["","","","",""]}],[{"start":{"row":91,"column":69},"end":{"row":92,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":92,"column":0},"end":{"row":92,"column":4},"action":"insert","lines":["    "]},{"start":{"row":92,"column":4},"end":{"row":93,"column":0},"action":"insert","lines":["",""]},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]},{"start":{"row":93,"column":4},"end":{"row":94,"column":0},"action":"insert","lines":["",""]},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"remove","lines":["    "],"id":31}],[{"start":{"row":94,"column":0},"end":{"row":95,"column":0},"action":"insert","lines":["",""],"id":32}],[{"start":{"row":94,"column":0},"end":{"row":97,"column":75},"action":"insert","lines":["@app.route('/edit_principle/<principle_id>')","def edit_principle(principle_id):","    this_principle =  mongo.db.principle_ingredients.find_one({\"_id\": ObjectId(principle_id)})","    return render_template('edit_principle.html', principle=this_principle)"],"id":33}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":44},"action":"remove","lines":["@app.route('/edit_principle/<principle_id>')"],"id":34},{"start":{"row":94,"column":0},"end":{"row":95,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":33},"action":"remove","lines":["def edit_principle(principle_id):"],"id":35}],[{"start":{"row":94,"column":0},"end":{"row":95,"column":0},"action":"remove","lines":["",""],"id":36}],[{"start":{"row":90,"column":37},"end":{"row":90,"column":38},"action":"remove","lines":["i"],"id":37},{"start":{"row":90,"column":37},"end":{"row":90,"column":38},"action":"remove","lines":["d"]}],[{"start":{"row":90,"column":37},"end":{"row":90,"column":38},"action":"insert","lines":["t"],"id":38},{"start":{"row":90,"column":38},"end":{"row":90,"column":39},"action":"insert","lines":["y"]},{"start":{"row":90,"column":39},"end":{"row":90,"column":40},"action":"insert","lines":["p"]},{"start":{"row":90,"column":40},"end":{"row":90,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":93,"column":0},"end":{"row":98,"column":0},"action":"remove","lines":["    ","    this_principle =  mongo.db.principle_ingredients.find_one({\"_id\": ObjectId(principle_id)})","    return render_template('edit_principle.html', principle=this_principle)","","",""],"id":39}],[{"start":{"row":111,"column":29},"end":{"row":111,"column":30},"action":"remove","lines":["g"],"id":40},{"start":{"row":111,"column":29},"end":{"row":111,"column":30},"action":"remove","lines":["e"]}],[{"start":{"row":111,"column":28},"end":{"row":111,"column":29},"action":"remove","lines":["'"],"id":41}],[{"start":{"row":111,"column":28},"end":{"row":111,"column":29},"action":"insert","lines":["'"],"id":42},{"start":{"row":111,"column":29},"end":{"row":111,"column":30},"action":"insert","lines":["m"]},{"start":{"row":111,"column":30},"end":{"row":111,"column":31},"action":"insert","lines":["a"]},{"start":{"row":111,"column":31},"end":{"row":111,"column":32},"action":"insert","lines":["n"]},{"start":{"row":111,"column":32},"end":{"row":111,"column":33},"action":"insert","lines":["a"]},{"start":{"row":111,"column":33},"end":{"row":111,"column":34},"action":"insert","lines":["g"]},{"start":{"row":111,"column":34},"end":{"row":111,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":111,"column":35},"end":{"row":111,"column":36},"action":"remove","lines":["t"],"id":43}],[{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["g"],"id":44},{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["e"]},{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["t"]}],[{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"insert","lines":["m"],"id":45},{"start":{"row":134,"column":30},"end":{"row":134,"column":31},"action":"insert","lines":["a"]},{"start":{"row":134,"column":31},"end":{"row":134,"column":32},"action":"insert","lines":["n"]},{"start":{"row":134,"column":32},"end":{"row":134,"column":33},"action":"insert","lines":["a"]},{"start":{"row":134,"column":33},"end":{"row":134,"column":34},"action":"insert","lines":["g"]},{"start":{"row":134,"column":34},"end":{"row":134,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":187,"column":29},"end":{"row":187,"column":30},"action":"remove","lines":["g"],"id":46},{"start":{"row":187,"column":29},"end":{"row":187,"column":30},"action":"remove","lines":["e"]},{"start":{"row":187,"column":29},"end":{"row":187,"column":30},"action":"remove","lines":["t"]}],[{"start":{"row":187,"column":29},"end":{"row":187,"column":30},"action":"insert","lines":["m"],"id":47},{"start":{"row":187,"column":30},"end":{"row":187,"column":31},"action":"insert","lines":["a"]},{"start":{"row":187,"column":31},"end":{"row":187,"column":32},"action":"insert","lines":["n"]},{"start":{"row":187,"column":32},"end":{"row":187,"column":33},"action":"insert","lines":["a"]},{"start":{"row":187,"column":33},"end":{"row":187,"column":34},"action":"insert","lines":["g"]},{"start":{"row":187,"column":34},"end":{"row":187,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":187,"column":34},"end":{"row":187,"column":35},"action":"remove","lines":["e"],"id":48},{"start":{"row":187,"column":33},"end":{"row":187,"column":34},"action":"remove","lines":["g"]},{"start":{"row":187,"column":32},"end":{"row":187,"column":33},"action":"remove","lines":["a"]},{"start":{"row":187,"column":31},"end":{"row":187,"column":32},"action":"remove","lines":["n"]},{"start":{"row":187,"column":30},"end":{"row":187,"column":31},"action":"remove","lines":["a"]},{"start":{"row":187,"column":29},"end":{"row":187,"column":30},"action":"remove","lines":["m"]}],[{"start":{"row":187,"column":29},"end":{"row":187,"column":30},"action":"insert","lines":["g"],"id":49},{"start":{"row":187,"column":30},"end":{"row":187,"column":31},"action":"insert","lines":["e"]},{"start":{"row":187,"column":31},"end":{"row":187,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["m"],"id":50},{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["a"]},{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["n"]},{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["a"]},{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["g"]},{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["e"]}],[{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"insert","lines":["g"],"id":51},{"start":{"row":134,"column":30},"end":{"row":134,"column":31},"action":"insert","lines":["e"]},{"start":{"row":134,"column":31},"end":{"row":134,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":192,"column":0},"end":{"row":193,"column":0},"action":"remove","lines":["",""],"id":52},{"start":{"row":192,"column":0},"end":{"row":193,"column":0},"action":"remove","lines":["",""]},{"start":{"row":192,"column":0},"end":{"row":193,"column":0},"action":"remove","lines":["",""]},{"start":{"row":192,"column":0},"end":{"row":193,"column":0},"action":"remove","lines":["",""]},{"start":{"row":192,"column":0},"end":{"row":193,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":111,"column":29},"end":{"row":111,"column":30},"action":"remove","lines":["m"],"id":53}],[{"start":{"row":111,"column":46},"end":{"row":112,"column":4},"action":"remove","lines":["","    "],"id":54}],[{"start":{"row":111,"column":46},"end":{"row":112,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":112,"column":0},"end":{"row":112,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":111,"column":33},"end":{"row":111,"column":34},"action":"remove","lines":["e"],"id":56},{"start":{"row":111,"column":32},"end":{"row":111,"column":33},"action":"remove","lines":["g"]},{"start":{"row":111,"column":31},"end":{"row":111,"column":32},"action":"remove","lines":["a"]},{"start":{"row":111,"column":30},"end":{"row":111,"column":31},"action":"remove","lines":["n"]},{"start":{"row":111,"column":29},"end":{"row":111,"column":30},"action":"remove","lines":["a"]}],[{"start":{"row":111,"column":29},"end":{"row":111,"column":30},"action":"insert","lines":["g"],"id":57},{"start":{"row":111,"column":30},"end":{"row":111,"column":31},"action":"insert","lines":["e"]},{"start":{"row":111,"column":31},"end":{"row":111,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"remove","lines":["m"],"id":58},{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"remove","lines":["a"]},{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"remove","lines":["n"]},{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"remove","lines":["a"]},{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"remove","lines":["g"]},{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"remove","lines":["e"]}],[{"start":{"row":102,"column":29},"end":{"row":102,"column":30},"action":"insert","lines":["g"],"id":59},{"start":{"row":102,"column":30},"end":{"row":102,"column":31},"action":"insert","lines":["e"]},{"start":{"row":102,"column":31},"end":{"row":102,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"remove","lines":["m"],"id":60},{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"remove","lines":["a"]}],[{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"remove","lines":["n"],"id":61},{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"remove","lines":["a"]},{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"remove","lines":["g"]},{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"remove","lines":["e"]}],[{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"insert","lines":["g"],"id":62},{"start":{"row":96,"column":30},"end":{"row":96,"column":31},"action":"insert","lines":["e"]},{"start":{"row":96,"column":31},"end":{"row":96,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"remove","lines":["m"],"id":63},{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"remove","lines":["a"]},{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"remove","lines":["n"]},{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"remove","lines":["a"]},{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"remove","lines":["g"]},{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"remove","lines":["e"]}],[{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"insert","lines":["g"],"id":64},{"start":{"row":78,"column":14},"end":{"row":78,"column":15},"action":"insert","lines":["e"]},{"start":{"row":78,"column":15},"end":{"row":78,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":79,"column":4},"end":{"row":79,"column":5},"action":"remove","lines":["m"],"id":65},{"start":{"row":79,"column":4},"end":{"row":79,"column":5},"action":"remove","lines":["a"]},{"start":{"row":79,"column":4},"end":{"row":79,"column":5},"action":"remove","lines":["n"]},{"start":{"row":79,"column":4},"end":{"row":79,"column":5},"action":"remove","lines":["a"]},{"start":{"row":79,"column":4},"end":{"row":79,"column":5},"action":"remove","lines":["g"]},{"start":{"row":79,"column":4},"end":{"row":79,"column":5},"action":"remove","lines":["e"]}],[{"start":{"row":79,"column":4},"end":{"row":79,"column":5},"action":"insert","lines":["g"],"id":66},{"start":{"row":79,"column":5},"end":{"row":79,"column":6},"action":"insert","lines":["e"]},{"start":{"row":79,"column":6},"end":{"row":79,"column":7},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":600,"scrollleft":0,"selection":{"start":{"row":79,"column":7},"end":{"row":79,"column":7},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":40,"state":"start","mode":"ace/mode/python"}},"timestamp":1563829543428,"hash":"73d79c3c5ff73aa29eb2088b678f0b5a7aac0ad6"}