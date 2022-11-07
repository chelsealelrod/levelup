import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import Event


class EventTests(APITestCase):
    """some text"""
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "game": 2,
            "organizer": 1,
            "description": "Friday night Settlers and drinks",
            "date": "12021-08-14",
            "time": "19:30"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # SEED DATABASE WITH ONE EVENT
        # This is needed because the API does not expose a /events
        # endpoint for creating events
        event = Event()
        event.game = 2
        event.save()


    def test_create_event(self):
        """
        Ensure we can create a new event.
        """
        # DEFINE EVENT PROPERTIES
        url = "/events"
        data = {
            "eventId": 1,
            "game": 2,
            "organizer": 1,
            "description": "Friday night Settlers and drinks",
            "date": "12021-08-14",
            "time": "19:30"
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["description"], "Friday night Settlers and drinks")
        self.assertEqual(json_response["organizer"], 1)
        self.assertEqual(json_response["game"], 2)
        self.assertEqual(json_response["date"], "12021-08-14")
        self.assertEqual(json_response["time"], "19:30")
        
        
    def test_get_event(self):
        """
        Ensure we can get an existing event.
        """

        # Seed the database with a event
        event = Event()
        event.event_id = 1
        event.game = 5
        event.organizer = 1
        event.description = "Friday night Settlers and drinks"
        event.date = "12021-08-14"
        event.time = "19:30"

        event.save()

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.get(f"/events/{event.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the values are correct
        self.assertEqual(json_response["description"], "Friday night Settlers and drinks")
        self.assertEqual(json_response["organizer"], 1)
        self.assertEqual(json_response["game"], 2)
        self.assertEqual(json_response["date"], "12021-08-14")
        self.assertEqual(json_response["time"], "19:30")
        
    def test_change_event(self):
        """
        Ensure we can change an existing event.
        """
        event = Event()
        event.event_id = 1
        event.game = 5
        event.organizer = 1
        event.description = "Friday night Settlers and drinks"
        event.date = "12021-08-14"
        event.time = "19:30"
        event.save()

        # DEFINE NEW PROPERTIES FOR EVENT
        data = {
             "eventId": 1,
             "organizer": 1,
             "description": "Welcome To at lunch",
             "game": 1,
             "date": "2021-10-04",
             "time": "12:00"
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(f"/events/{event.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET EVENT AGAIN TO VERIFY CHANGES
        response = self.client.get(f"/events/{event.id}")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties are correct
        self.assertEqual(json_response["description"], "Welcome To at lunch")
        self.assertEqual(json_response["organizer"], 1)
        self.assertEqual(json_response["game"], 1)
        self.assertEqual(json_response["date"], "12021-10-14")
        self.assertEqual(json_response["time"], "12:00")
        
        
    def test_delete_game(self):
        """
        Ensure we can delete an existing event.
        """
        event = Event()
        event.event_id = 1
        event.game = 5
        event.organizer = 1
        event.description = "Friday night Settlers and drinks"
        event.date = "12021-08-14"
        event.time = "19:30"
        event.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.delete(f"/games/{event.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET EVENT AGAIN TO VERIFY 404 response
        response = self.client.get(f"/events/{event.id}")
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
