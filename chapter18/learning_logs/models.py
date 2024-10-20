from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)  # Name of the topic
    date_added = models.DateTimeField(auto_now_add=True)  # Timestamp when the topic was added

    def __str__(self):
        return self.text
