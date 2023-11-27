from lib.recipe import Recipe

"""
Recipe constructs with an id, title and author_name
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test Recipe", 90, 1)
    assert recipe.id == 1
    assert recipe.name == "Test Recipe"
    assert recipe.cooking_time == 90
    assert recipe.rating == 1

"""
We can format recipes to strings nicely
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, "Test Recipe", 90, 1)
    assert str(recipe) == "Recipe(1, Test Recipe, 90 mins, 1/5)"

"""
We can compare two identical recipes
And have them be equal
"""
def test_recipes_are_equal():
    recipe1 = Recipe(1, "Test Recipe", 90, 1)
    recipe2 = Recipe(1, "Test Recipe", 90, 1)
    assert recipe1 == recipe2
