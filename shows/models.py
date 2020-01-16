from django.db import models

class Episode(model.Models):
    title = models.CharField(max_length=128)
    description = models.TextField()
    actor = models.ForeignKey('auth.User', on_delete=models.CASCADE) """ It sets the rules about what happens when related record is deleleted. If actor is deleted, what should happen to the description"""

    def __str__(self):
        return self.title