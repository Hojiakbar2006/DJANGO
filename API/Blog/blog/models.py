from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.utils.text import slugify



class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'

    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='images')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT)
    
    @property
    def average_rating(self):
        # Postga baho berilgan barcha qiymatlar
        all_ratings = Rating.objects.filter(post=self)
        
        # Barcha qiymatlar o'rtachasini hisoblash
        total_rating = sum([rating.rating for rating in all_ratings])
        avg_rating = total_rating / len(all_ratings) if len(all_ratings) > 0 else 0

        return int(avg_rating)

    @property
    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ('user', 'post')
