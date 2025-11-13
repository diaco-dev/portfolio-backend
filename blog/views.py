from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import generics, mixins, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from .models import Tag, Category, Post, Project, SkillCategory, Skill
from .serializers import TagSerializer, CategorySerializer, PostListSerializer, PostDetailSerializer, \
    ProjectListSerializer, ProjectSerializer, SkillCategorySerializer, SkillSerializer


# ------------- Tag List -------------#
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('name',)
    search_fields = ('name',)

# ------------- Category List -------------#
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('name',)
    search_fields = ('name',)
# ------------- Post List -------------#
class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('category','category__slug')
    search_fields = ('title',)
# ------------- Post Detail slug -------------#
class PostDetailSlugView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('category',)
    search_fields = ('title',)

# ------------- Post Detail id -------------#
class PostDetailView(mixins.RetrieveModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('category',)
    search_fields = ('title',)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# ------------- Post Detail id -------------#
class ProjectViewSet(viewsets.ModelViewSet):

    permission_classes = [AllowAny]

    def get_queryset(self):
        return (
            Project.objects.all()
            .prefetch_related("challenges")
            .order_by("-created_at")
        )

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        return ProjectSerializer


class SkillCategoryViewSet(viewsets.ModelViewSet):


    permission_classes = [AllowAny]

    def get_queryset(self):
        return (
            SkillCategory.objects.all()
            .prefetch_related("skills")
            .order_by("category")
        )

    serializer_class = SkillCategorySerializer


class SkillViewSet(viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Skill.objects.all().select_related("category").order_by("name")
    serializer_class = SkillSerializer