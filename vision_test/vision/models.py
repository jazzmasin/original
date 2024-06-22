from django.db import models

class VisionTest(models.Model):
    left_eye = models.FloatField()
    right_eye = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Left Eye: {self.left_eye}, Right Eye: {self.right_eye}"
