import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import GameType


class GameTypeTests(APITestCase):
    """some text"""
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



    def test_create_game(self):
        """
        Ensure we can create a new gametype.
        """
        # DEFINE GAMETYPE PROPERTIES
        url = "/gametype"
        data = {
            "name": "board game"
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the gametype was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["name"], "Board game")
     
        
        
    def test_get_gametype(self):
        """
        Ensure we can get an existing gametype.
        """

        # Seed the database with a gametype
        gametype = GameType()
        gametype.game_type_id = 1
        gametype.name = "Board Game"

        gametype.save()

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.get(f"/gametype/{gametype.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the values are correct
        self.assertEqual(json_response["name"], "Board Game")
        
        
    def test_change_gametype(self):
        """
        Ensure we can change an existing gametype.
        """
        gametype = GameType()
        gametype.id = 1
        gametype.name = "Board Game"
        gametype.save()

        # DEFINE NEW PROPERTIES FOR GAMETYPE
        data = {
            "id": 1,
            "name": "Board Game"
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(f"/gametype/{gametype.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET GAME AGAIN TO VERIFY CHANGES
        response = self.client.get(f"/gametype/{gametype.id}")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties are correct
        self.assertEqual(json_response["name"], "Board Game")
        
        
        
    def test_delete_gametype(self):
        """
        Ensure we can delete an existing gametype.
        """
        gametype = GameType()
        gametype.id = 1
        gametype.name = "Board Game"
      
        gametype.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.delete(f"/gametype/{gametype.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET GAME AGAIN TO VERIFY 404 response
        response = self.client.get(f"/gametype/{gametype.id}")
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
