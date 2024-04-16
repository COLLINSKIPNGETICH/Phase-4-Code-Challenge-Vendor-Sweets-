# serializers.py

class UserSerializer:
    @staticmethod
    def serialize(user):
        return {
            'id': user.id,
            'username': user.username,
            'recipes': [recipe.serialize() for recipe in user.recipes]
        }

class RecipeSerializer:
    @staticmethod
    def serialize(recipe):
        return {
            'id': recipe.id,
            'title': recipe.title,
            'instructions': recipe.instructions,
            'minutes_to_complete': recipe.minutes_to_complete,
            'author': UserSerializer.serialize(recipe.author)
        }
