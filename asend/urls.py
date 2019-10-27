from django.urls import path
from .views import EntryListView, CategoryDetailView, EntryCreateView, CategoryCreateView, EntryDetailView
from . import views

urlpatterns = [
    path('', EntryListView.as_view(), name='homepage'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('entry/new/', EntryCreateView.as_view(), name='entry-create'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
]

#app/model_viewtype.html