from django.test import TestCase

class HomeTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Test de las vistas de la App Home.")
           

    def test_view_url_home(self): 
        resp = self.client.get('/') 
        self.assertEqual(resp.status_code, 200)  