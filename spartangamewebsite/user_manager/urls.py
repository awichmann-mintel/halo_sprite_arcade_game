from django.urls import re_path
from user_manager.views import MyView

urlpatterns = [
    re_path(r"^users", MyView.as_view()),
]
