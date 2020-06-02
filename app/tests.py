from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='a')
        self.profile = Profile.objects.create(name = self.user,bio = 'bb')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile('a')
        self.assertTrue(len(profile)== 1)

    def test_delete(self):
        self.profile.save()
        self.profile.delete()
        self.assertTrue(len(Profile.objects.all()) == 0)

    def test_search_profile(self):
        self.profile.save()
        profile = Profile.search_profile('a')
        self.assertTrue(len(profile)== 1)





