from django.db import models

class ModelProvider(models.Model):
    provider_name = models.CharField(max_length=50, default="")
    model_name = models.CharField(max_length=50)
    
    def __str__(self):
        return {self.provider_name} + "/" + {self.model_name}


class GlobalResponseCounter(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Global Response Count: {self.count}"
