from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from .models import Post, Tag, Category


#---------------------- POST --------------------------
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='extends'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = False
        self.fields['excerpt'].required = False
        self.fields['body'].required = False

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'subtitle','slug', 'created_at', 'updated_at')
    search_fields = ('title', 'subtitle', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)


#---------------------- TAG --------------------------
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

#---------------------- CATEGORY --------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
