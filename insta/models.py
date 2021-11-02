from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_pic = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def update_bio(self,biography):
        self.biography=biography
        self.save()

    def delete_profile(self):
        self.delete()


    def split_biography(self):
        return self.biography.split("\n")

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()



class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    posted_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField()
    image = CloudinaryField('image')
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.caption

    def save_post(self):
        self.save()

    def delete_image(self):
        self.delete()
    



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_linked = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    description = models.CharField(max_length=500)
    comment_posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Comment by {} on {}".format(self.user.username, self.post_linked.caption)

    class Meta:
        ordering = ('-comment_posted_on',)


class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_linked = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return 'User :{} Liked {} Post '.format(self.user.username,self.post_linked.caption)

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'