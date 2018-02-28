# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        # Validate first name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be more than 2 characters"
        elif postData['first_name'].replace(' ','').isalpha() == False:
            errors['first_name'] = "First name cannot contain numbers"
        
        # Validate last name
        if(len(postData['last_name'])) < 2:
            errors['last_name'] = "Last name must be more than 2 characters"
        elif postData['last_name'].replace(' ','').isalpha() == False:
            errors['last_name'] = "Last name cannot contain numbers"
        
        # Validate Email
        if len(postData['email']) < 1:
            errors['email'] = "email must be more than 2 characters"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "email be a valid email address"
        
        # Validate Password
        if len(postData['password']) < 1:
            errors['password'] = "Password cannot be blank"
        elif len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        elif not PASSWORD_REGEX.match(postData['password']):
            errors['password'] = "Invalid Password, must contain at least one uppercase and one number"

        # Validate Confrim Password
        if len(postData['confirm_password']) < 1:
            errors['confirm'] = "Confirm Password cannot be blank"
        elif postData['password'] != postData['confirm_password']:
            errors['confirm'] = "Passwords do not match"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_level = models.CharField(max_length=6)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    full_name = property(_get_full_name)

    objects = UserManager()

class Message(models.Model):
    content = models.TextField()
    profile_id = models.ForeignKey(User, related_name="profile",on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    content = models.TextField()
    message_id = models.ForeignKey(Message, related_name="message",on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, default=1, related_name="user",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)