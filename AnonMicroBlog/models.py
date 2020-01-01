from django.db import models


class PostModel(models.Model):
    post = models.TextField()

    def _clean(self):
        self.clean()


