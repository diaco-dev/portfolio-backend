from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import TagListView, CategoryListView, PostListView, PostDetailView, PostDetailSlugView, ProjectViewSet, \
    SkillCategoryViewSet, SkillViewSet, CvViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"cv", CvViewSet, basename="cv")
router.register(r"skill-categories", SkillCategoryViewSet, basename="skill-category")
router.register(r"skills", SkillViewSet, basename="skill")

urlpatterns = [
    path("", include(router.urls)),
    path('tag/', TagListView.as_view(), name='tag-list'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>/', PostDetailSlugView.as_view(), name='post-detail-slug'),
    path('post-detail/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),


]
