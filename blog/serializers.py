from django.db import transaction
from rest_framework import serializers
from blog.models import Tag, Category, ProjectChallenge, Project, SkillCategory, Skill
from .models import Post

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLASS:  TagSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name','slug']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLASS:  TagSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name','slug','description']
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLASS: PostSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#------------- List -------------#
class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id','slug', 'title','content', 'excerpt', 'tag','category', 'image']

#------------- detail -------------#
class PostDetailSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Post
        fields = ['id','slug', 'title','content', 'subtitle', 'body', 'tag','category', 'image']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLASS: PostSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ProjectTypeField(serializers.ChoiceField):

    def to_representation(self, value):
        value = super().to_representation(value)
        if isinstance(value, str):
            return value.capitalize()
        return value

    def to_internal_value(self, data):
        if isinstance(data, str):
            data = data.lower()
        return super().to_internal_value(data)


class ProjectChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectChallenge
        fields = (
            "id",
            "challenge",
            "solution",
        )
        read_only_fields = ("id",)


class ProjectListSerializer(serializers.ModelSerializer):

    type = ProjectTypeField(choices=Project.ProjectType.choices)
    shortDescription = serializers.CharField(
        source="short_description", allow_blank=True, required=False
    )
    imageUrl = serializers.URLField(
        source="image_url", allow_blank=True, required=False
    )
    techStack = serializers.ListField(
        child=serializers.CharField(), source="tech_stack", required=False
    )
    role = serializers.ListField(
        child=serializers.CharField(), source="roles", required=False
    )
    githubUrl = serializers.URLField(
        source="github_url", allow_blank=True, required=False
    )
    demoUrl = serializers.URLField(
        source="demo_url", allow_blank=True, required=False
    )

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "type",
            "shortDescription",
            "imageUrl",
            "techStack",
            "role",
            "results",
            "githubUrl",
            "demoUrl",
        )


class ProjectSerializer(serializers.ModelSerializer):

    type = ProjectTypeField(choices=Project.ProjectType.choices)

    shortDescription = serializers.CharField(
        source="short_description", allow_blank=True, required=False
    )
    imageUrl = serializers.URLField(
        source="image_url", allow_blank=True, required=False
    )

    techStack = serializers.ListField(
        child=serializers.CharField(), source="tech_stack", required=False
    )
    role = serializers.ListField(
        child=serializers.CharField(), source="roles", required=False
    )

    githubUrl = serializers.URLField(
        source="github_url", allow_blank=True, required=False
    )
    demoUrl = serializers.URLField(
        source="demo_url", allow_blank=True, required=False
    )

    challenges = ProjectChallengeSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "type",
            "shortDescription",
            "imageUrl",
            "problem",
            "solution",
            "techStack",
            "role",
            "challenges",
            "results",
            "githubUrl",
            "demoUrl",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLASS: PostSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            "name",
            "level",
            "icon",
            "href",
            "created_at",
            "updated_at",
        )


class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, required=False)
    class Meta:
        model = SkillCategory
        fields =(
            "category",
            "icon",
            "skills",
            "created_at",
            "updated_at",
        )
