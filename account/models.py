from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.slug} - {self.updated.date()}'

    def get_absolute_url(self):
        return reverse('home:post_detail', args=(self.id, self.slug))

    def like_count(self):
        return self.plikes.count()

    def user_can_like(self, user):
        user_like = user.ulikes.filter(post=self)
        if user_like.exists():
            return True
        return False


class Relation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_user} follow {self.to_user}'
