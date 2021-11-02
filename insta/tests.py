from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post,Profile

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='rash3590')
        self.profile = Profile(id=1,profile_pic='path/to/photo',user = self.user,biography='test bio')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

     #Testing save method
    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

        #Testing updtae method
    def test_update_profile(self):
        self.profile.save_profile()
        self.profile = Profile.objects.get(pk = 1)
        self.profile.update_bio('updated bio')
        self.updated_profile = Profile.objects.get(pk = 1)
        self.assertEqual(self.updated_profile.biography,"updated bio")

       #Testing Delete Method
    def test_delete_image(self):
        self.profile.delete_profile()
        self.assertTrue(len(Profile.objects.all()) == 0)


class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.post = Post(id=1,image = 'path/to/image',location='test',caption='test caption')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

     #Testing Save method
    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

      #Testing Delete Method
    def test_delete_image(self):
        self.post.delete_image()
        self.assertTrue(len(Post.objects.all()) == 0)
