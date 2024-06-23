from django.test import SimpleTestCase
from django.urls import resolve,reverse
from main.views import shorturl,main_url

class TestURL(SimpleTestCase):

    def test_shorturl_resolves(self):
        url = reverse("shorturl")
        self.assertEquals(resolve(url).func,shorturl)


    def test_mainurl_resolves(self):
        url = reverse("main",args=["abcdef"])
        self.assertEquals(resolve(url).func,main_url)

