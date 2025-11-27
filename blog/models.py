from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from blog.storage import BlogImageStorage
from core.models import GenericModel
from django.utils.text import slugify
import re



#--------------------- category ----------------------------#
class Category(GenericModel):
    name = models.CharField(
        max_length=100,
        unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True)
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#--------------------- tag ----------------------------#
class Tag(GenericModel):
    name = models.CharField(
        max_length=50,
        unique=True,
        null = True,
        blank = True
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True
    )
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
#--------------------- post ----------------------------#
class Post(GenericModel):
    title = models.CharField(
        max_length=200
    )
    subtitle = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )
    content = CKEditor5Field(
        config_name='extends'
    )
    excerpt = models.TextField(
        null=True,
        blank=True
    )
    body = models.TextField()
    tag = models.ManyToManyField(
        Tag,
        related_name='articles',
        blank=True
    )
    category = models.ManyToManyField(
        Category,
        blank=True
    )
    image = models.ImageField(
        upload_to='post/',
    storage = BlogImageStorage(),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



#--------------------- post ----------------------------#
class SkillCategory(GenericModel):
    category = models.CharField(max_length=150)
    icon = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
        ordering = ("category",)

    def __str__(self):
        return self.category


class Skill(GenericModel):

    category = models.ForeignKey(
        SkillCategory,
        related_name="skills",
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=150)
    level = models.CharField(max_length=50, blank=True, null=True)   # e.g. beginner/intermediate/advanced
    icon = models.CharField(max_length=150, blank=True, null=True)
    href = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ("name",)

    def __str__(self):
        return self.name



class Project(GenericModel):
    class ProjectType(models.TextChoices):
        ORGANIZATIONAL = "organizational", "Organizational"
        PERSONAL = "personal", "Personal"


    title = models.CharField(max_length=255)
    type = models.CharField(
        max_length=20,
        choices=ProjectType.choices,
        default=ProjectType.PERSONAL,
    )
    short_description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    problem = models.TextField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)

    # لیست تکنولوژی‌ها (مثلاً ["Django", "PostgreSQL", "React"])
    tech_stack = models.JSONField(default=list, blank=True)

    # نقش‌ها (مثلاً ["Product Manager", "Backend Developer"])
    roles = models.JSONField(default=list, blank=True)

    # نتایج و خروجی‌ها (مثلاً ["Increased conversion by 20%"])
    results = models.JSONField(default=list, blank=True)

    github_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class ProjectChallenge(GenericModel):
    project = models.ForeignKey(
        Project,
        related_name="challenges",
        on_delete=models.CASCADE,
    )

    challenge = models.TextField()
    solution = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Project Challenge"
        verbose_name_plural = "Project Challenges"
        ordering = ("project", "id")

    def __str__(self):
        return f"{self.project.title} - {self.challenge[:40]}..."


#--------------------- cv ----------------------------#
class CV(GenericModel):
    title = models.CharField(
        max_length=200
    )
    file = models.FileField(
        upload_to='post/',
        storage = BlogImageStorage(),
        blank=True,
        null=True
    )