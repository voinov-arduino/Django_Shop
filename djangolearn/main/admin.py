from .models import Task, News
from django import forms
from django.contrib import admin

class TaskAdminForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm


admin.site.register(Task, TaskAdmin)


admin.site.register(News,NewsAdmin)