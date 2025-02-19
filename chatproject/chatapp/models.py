from django.db import models

class ModelProvider(models.Model):
    provider_name = models.CharField(max_length=50, default="")
    model_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.provider_name}/{self.model_name}" 


class GlobalResponseCounter(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Global Response Count: {self.count}"


class RoutingRule(models.Model):
    original_model = models.CharField(max_length=255)
    regex_pattern = models.CharField(max_length=255)
    redirect_model = models.CharField(max_length=255)

    def __str__(self):
        return f"Rule: {self.original_model} -> {self.redirect_model} (Regex: {self.regex_pattern})"

from django.db import models

class ChatMessage(models.Model):
    sender = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="uploads/", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.message or 'File Upload'}"

class FileRoutingRule(models.Model):
    file_type = models.CharField(max_length=50, unique=True)  
    provider = models.CharField(max_length=100) 
    model = models.CharField(max_length=100)  

    def __str__(self):
        return f"File Type: {self.file_type} -> {self.provider} ({self.model})"