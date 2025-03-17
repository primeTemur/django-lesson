from django.contrib import admin
from base.models import Company,Profile,Review,Social,Skill,Post,Comment,JobOpening

# Register your models here.
admin.site.register(Company)
admin.site.register(JobOpening)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Social)
admin.site.register(Skill)
admin.site.register(Post)
admin.site.register(Comment)
# admin.site.register(Like)
