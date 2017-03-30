# Register your models here.
from django.contrib import admin

from .models import Question

from .models import Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text','votes']

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, ChoiceAdmin)
