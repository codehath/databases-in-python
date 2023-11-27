from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/recipes.sql") # Seed our database with some test data
    repository = RecipeRepository(db_connection) # Create a new RecipeRepository

    recipes = repository.all() # Get all recipes

    # Assert on the results
    assert recipes == [
        Recipe(1, 'Mac and Cheese', 90, 5),
        Recipe(2, 'Chicken Chow Mein', 45, 3),
        Recipe(3, 'Spaghetti Bolognese', 120, 4),
        Recipe(4, 'Thai Green Curry', 45, 3),
        Recipe(5, 'Egg Fried Rice', 30, 5),
    ]

"""
When we call RecipeRepository#find
We get a single Recipe object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(3)
    assert recipe == Recipe(3, 'Spaghetti Bolognese', 120, 4)

# """
# When we call RecipeRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = RecipeRepository(db_connection)

#     repository.create(Recipe(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         Recipe(1, "Pixies", "Rock"),
#         Recipe(2, "ABBA", "Pop"),
#         Recipe(3, "Taylor Swift", "Pop"),
#         Recipe(4, "Nina Simone", "Jazz"),
#         Recipe(5, "The Beatles", "Rock"),
#     ]

# """
# When we call RecipeRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = RecipeRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         Recipe(1, "Pixies", "Rock"),
#         Recipe(2, "ABBA", "Pop"),
#         Recipe(4, "Nina Simone", "Jazz"),
#     ]
