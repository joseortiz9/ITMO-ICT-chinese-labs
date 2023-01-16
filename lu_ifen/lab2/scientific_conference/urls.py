from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('conferences/<int:user_id>', views.list_conferences, name='list_conferences'),
    path('my_conference/<int:user_id>', views.list_my_conference, name='my_conference'),
    path('authors/<int:conference_id>', views.list_Presentation, name='authors'),
    path('create_presentation/<int:user_id>/<int:conference_id>', views.create_presentation, name='create_presentation'),
    path('presentation_edit/<int:user_id>/<int:conference_id>', views.presentation_edit, name='presentation_edit'),
    path('review/<int:user_id>/<int:conference_id>', views.list_review, name='list_review'),
    path('create_review/<int:user_id>/<int:conference_id>', views.create_review, name='create_review'),
    
]
