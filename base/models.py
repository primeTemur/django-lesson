from django.db import  models
from django.contrib.auth.models import  User

class Company(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(default='',upload_to='',blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    # tags=models.ManyToManyField('Tag',blank=True)
    website=models.CharField(max_length=200,blank=True,null=True)
    linkedin=models.CharField(max_length=1000,null=True,blank=True)
    twitter=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.name

class JobOpening(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    avalible=models.BooleanField(default=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    avatat=models.ImageField(default='',upload_to='',blank=True,null=True)
    name=models.CharField(max_length=200,null=True,blank=True,default='No Name')
    socials=models.ManyToManyField('Social',blank=True)
    skills=models.ManyToManyField('Skill',blank=True)
    verified=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

class Review(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Social(models.Model):
    icon=models.ImageField(default='',upload_to='',blank=True,null=True)
    link=models.CharField(max_length=200,blank=True,null=True)


class Skill(models.Model):
    name=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    OPTIONS=(
        ('collab','collab'),
        ('job','job'),
        ('default','default'),
    )
    owmer=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    post_type=models.CharField(choices=OPTIONS,default=OPTIONS[2],max_length=100)
    body=models.TextField()
    like=models.ManyToManyField(User,related_name='likes',blank=True)
    
    created=models.DateTimeField(auto_now=True,null=True,blank=True)
    # title=models.CharField(max_length=200)

    def __str__(self):
        return self.body[0:50]

# class Like(models.Model):
#     owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    
class Comment(models.Model):
    owner=models.ForeignKey(User,models.CASCADE,blank=True,null=True)
    post=models.ForeignKey(Post,models.CASCADE,blank=True,null=True)
    body=models.TextField(null=True,blank=True,default='Test')
    created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]
