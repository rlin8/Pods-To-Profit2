from django.contrib import admin
from . import models

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description', 
                    'information_url',
                    'choice_a', 
                    'choice_b', 
                    'choice_c', 
                    'choice_d', 
                    'answer',
                    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'research_experience',
        'subject',
        'description')