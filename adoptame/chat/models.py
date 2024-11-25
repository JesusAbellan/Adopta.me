from django.contrib.auth.models import User
from django.db import models
from pet.models import Pet

class Chat(models.Model):
    pet = models.ForeignKey(Pet, related_name='chats', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)


class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)