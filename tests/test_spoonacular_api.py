import os
import unittest
from spoonacular import api

# Import API keys from environment variables
api_key_name = "SPOONACULAR_API_KEY"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = api.API(api_key, timeout=5, sleep_time=0.5)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} API tests...\n".format("Spoonacular"))
        cls.api = api

    def test_quota_restrictions(self):
        """ Test that the proper amounts are set """
        msg = "Quota amount does not matched specified number"
        name = 'parse_ingredients'
        ingredients = {'ingredientList': '1 pound of bacon\n3 apples'}
        response = self.api.determineCostOfEndpoint(name, query=ingredients)
        expected = {'requests': 1, 'tinyrequests': 0, 'results': 2}
        self.assertEqual(response, expected, msg)

    """ --------------- Compute Endpoints --------------- """

    def test_classify_a_grocery_product(self):
        """Test the 'classify a grocery product' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'product': {"title": "Kroger Vitamin A & D Reduced Fat 2% Milk",
                    "upc": "", "plu_code": ""}}
        response = self.api.classify_a_grocery_product(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_classify_cuisine(self):
        """Test the 'classify cuisine' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'ingredientList': '3 oz pork shoulder', 'title': 'Pork roast with green beans'}
        response = self.api.classify_cuisine(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_classify_grocery_products_batch(self):
        """Test the 'classify grocery products (batch)' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'products': [{"title": "Kroger Vitamin A & D Reduced Fat 2% Milk",
                    "upc": "", "plu_code": ""}]}
        response = self.api.classify_grocery_products_batch(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_convert_amounts(self):
        """Test the 'convert amounts' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'ingredientName': 'flour', 'sourceAmount': '2.5', 'sourceUnit': 'cups', 'targetUnit': 'grams'}
        response = self.api.convert_amounts(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_generate_meal_plan(self):
        """Test the 'generate meal plan' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'diet': 'vegetarian', 'exclude': 'shellfish, olives', 'targetCalories': '2000', 'timeFrame': 'day'}
        response = self.api.generate_meal_plan(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_guess_nutrition_by_dish_name(self):
        """Test the 'guess nutrition by dish name' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'title': 'Spaghetti Aglio et Olio'}
        response = self.api.guess_nutrition_by_dish_name(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_map_ingredients_to_grocery_products(self):
        """Test the 'map ingredients to grocery products' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {"ingredients": ["eggs", "bacon"], "servings": 2}
        response = self.api.map_ingredients_to_grocery_products(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_match_recipes_to_daily_calories(self):
        """Test the 'match recipes to daily calories' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'targetCalories': '2000', 'timeFrame': 'day'}
        response = self.api.match_recipes_to_daily_calories(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_quick_answer(self):
        """Test the 'quick answer' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'q': 'How much vitamin c is in 2 apples?'}
        response = self.api.quick_answer(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_summarize_recipe(self):
        """Test the 'summarize recipe' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'id': '4632'}
        response = self.api.summarize_recipe(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_visualize_equipment(self):
        """Test the 'visualize equipment' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'defaultCss': 'true', 'instructions': 'Use a blender for the nuts and put them in the pan.', 'showBacklink': 'true', 'view': 'grid'}
        response = self.api.visualize_equipment(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_visualize_ingredients(self):
        """Test the 'visualize ingredients' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'defaultCss': 'true', 'ingredientList': '3 oz flour', 'measure': 'metric', 'servings': '2', 'showBacklink': 'true', 'view': ''}
        response = self.api.visualize_ingredients(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_visualize_price_breakdown(self):
        """Test the 'visualize price breakdown' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'defaultCss': 'true', 'ingredientList': '3 oz flour', 'mode': '1', 'servings': '2', 'showBacklink': 'true'}
        response = self.api.visualize_price_breakdown(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_visualize_recipe_nutrition(self):
        """Test the 'visualize recipe nutrition' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'defaultCss': 'true', 'ingredientList': '3 oz flour', 'servings': '2', 'showBacklink': 'true'}
        response = self.api.visualize_recipe_nutrition(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_visualize_recipe_nutrition_by_id(self):
        """Test the 'visualize recipe nutrition by id' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'defaultCss': False, 'id': '1003464'}
        response = self.api.visualize_recipe_nutrition_by_id(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    """ --------------- Search Endpoints --------------- """

    def test_autocomplete_ingredient_search(self):
        """Test the 'autocomplete ingredient search' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'intolerances': 'egg', 'metaInformation': False, 'number': '10', 'query': 'appl'}
        response = self.api.autocomplete_ingredient_search(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_autocomplete_recipe_search(self):
        """Test the 'autocomplete recipe search' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'number': '10', 'query': 'chicken'}
        response = self.api.autocomplete_recipe_search(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_comparable_products(self):
        """Test the 'get comparable products' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'upc': '033698816271'}
        response = self.api.get_comparable_products(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_dish_pairing_for_wine(self):
        """Test the 'get dish pairing for wine' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'wine': 'merlot'}
        response = self.api.get_dish_pairing_for_wine(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_ingredient_substitutes(self):
        """Test the 'get ingredient substitutes' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'ingredientName': 'butter'}
        response = self.api.get_ingredient_substitutes(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_ingredient_substitutes_by_id(self):
        """Test the 'get ingredient substitutes by id' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'id': '1001'}
        response = self.api.get_ingredient_substitutes_by_id(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_random_recipes(self):
        """Test the 'get random recipes' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'limitLicense': False, 'number': '1', 'tags': 'vegetarian,dessert'}
        response = self.api.get_random_recipes(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_similar_recipes(self):
        """Test the 'get similar recipes' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'id': '156992'}
        response = self.api.get_similar_recipes(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_wine_description(self):
        """Test the 'get wine description' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'wine': 'malbec'}
        response = self.api.get_wine_description(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_wine_pairing(self):
        """Test the 'get wine pairing' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'food': 'steak', 'maxPrice': '50'}
        response = self.api.get_wine_pairing(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_wine_recommendation(self):
        """Test the 'get wine recommendation' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'maxPrice': '50', 'minRating': '0.7', 'number': '3', 'wine': 'merlot'}
        response = self.api.get_wine_recommendation(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_search_grocery_products_by_upc(self):
        """Test the 'search grocery products by upc' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'upc': '041631000564'}
        response = self.api.search_grocery_products_by_upc(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_search_recipes_by_ingredients(self):
        """Test the 'search recipes by ingredients' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'fillIngredients': False, 'ingredients': 'apples,flour,sugar', 'limitLicense': False, 'number': '5', 'ranking': '1'}
        response = self.api.search_recipes_by_ingredients(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_search_recipes_complex(self):
        """Test the 'search recipes complex' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'query': 'pasta', 'cuisine': 'italian', 'excludeCuisine': 'greek'}
        response = self.api.search_recipes_complex(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_search_site_content(self):
        """Test the 'search site content' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'query': 'past'}
        response = self.api.search_site_content(**testArgs)
        self.assertEqual(response.status_code, 200, msg)
        
    def search_restaurants(self):
        """Test the 'search restaurants' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'lat':'43.00441722228767','lng':'-81.27617531329763'}
        response = self.api.search_restaurants(**testArgs)
        self.assertEqual(response.status_code,200,msg)
    
    """ --------------- Chat Endpoints --------------- """

    def test_get_conversation_suggests(self):
        """Test the 'get conversation suggests' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'number': '10', 'query': 'tell'}
        response = self.api.get_conversation_suggests(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_talk_to_a_chatbot(self):
        """Test the 'talk to a chatbot' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'contextId': '342938', 'text': 'donut recipes'}
        response = self.api.talk_to_a_chatbot(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    """ --------------- Data Endpoints --------------- """

    def test_get_a_random_food_joke(self):
        """Test the 'get a random food joke' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {}
        response = self.api.get_a_random_food_joke(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_analyzed_recipe_instructions(self):
        """Test the 'get analyzed recipe instructions' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'id': '324694', 'stepBreakdown': 'true'}
        response = self.api.get_analyzed_recipe_instructions(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_food_information(self):
        """Test the 'get food information' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'amount': '100', 'id': '9266', 'unit': 'gram'}
        response = self.api.get_food_information(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_product_information(self):
        """Test the 'get product information' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'id': '22347'}
        response = self.api.get_product_information(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_random_food_trivia(self):
        """Test the 'get random food trivia' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {}
        response = self.api.get_random_food_trivia(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_recipe_information(self):
        """Test the 'get recipe information' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'id': '479101', 'includeNutrition': False}
        response = self.api.get_recipe_information(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_recipe_information_bulk(self):
        """Test the 'get recipe information bulk' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'ids': ['715538,716429'], 'includeNutrition': False}
        response = self.api.get_recipe_information_bulk(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    """ --------------- Extract Endpoints --------------- """

    def test_analyze_a_recipe_search_query(self):
        """Test the 'analyze a recipe search query' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'q': 'salmon with fusilli and no nuts'}
        response = self.api.analyze_a_recipe_search_query(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_analyze_recipe_instructions(self):
        """Test the 'analyze recipe instructions' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'instructions': 'Put the garlic in a pan and then add the onion.'}
        response = self.api.analyze_recipe_instructions(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_detect_food_in_text(self):
        """Test the 'detect food in text' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'text': 'I like to eat delicious tacos. Only cheeseburger with cheddar are better than that. But then again, pizza with pepperoni, mushrooms, and tomatoes is so good!'}
        response = self.api.detect_food_in_text(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_extract_recipe_from_website(self):
        """Test the 'extract recipe from website' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'forceExtraction': False, 'url': 'http://www.melskitchencafe.com/the-best-fudgy-brownies/'}
        response = self.api.extract_recipe_from_website(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_parse_ingredients(self):
        """Test the 'parse ingredients' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'ingredientList': '3 oz pork shoulder', 'servings': '2', 'includeNutrition': False}
        response = self.api.parse_ingredients(**testArgs)
        self.assertEqual(response.status_code, 200, msg)
