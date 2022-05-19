from django.db import models

TYPE_CHOICES = {
    ('math', 'math'),
    ('science', 'science'),
    ('language', 'language'),
    ('art', 'art'),
}


class djangoClasses(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=255, default="", blank=True)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title
