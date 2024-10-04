from django.urls import path

from aboutcars.controllers import ItemList, Item, CommentList

urlpatterns = [
    path('cars/', ItemList.as_view()),
    path('cars/<int:id>/', Item.as_view()),
    path('cars/<int:id>/comments/', CommentList.as_view())
]