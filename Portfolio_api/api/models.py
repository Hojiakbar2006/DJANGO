from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # delay = models.DecimalField()
    demo_link = models.URLField
    github_link = models.URLField
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
