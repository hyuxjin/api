from django.urls import path
from .views import UserListCreate, UserDetail, PostListCreate, PostDetail, CommentListCreate, CommentDetail

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserDetail.as_view(), name='user-detail'),  # Add this line
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:id>/', PostDetail.as_view(), name='post-detail'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:id>/', CommentDetail.as_view(), name='comment-detail'),
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('users/', views.get_users, name='get_users'),
#     path('users/create/', views.create_user, name='create_user'),
#     path('users/update/<int:id>/', views.update_user, name='update_user'),
#     path('users/delete/<int:id>/', views.delete_user, name='delete_user'),
# ]