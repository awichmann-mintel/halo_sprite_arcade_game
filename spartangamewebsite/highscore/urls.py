from .views import ScoreBoardView, ScoreViewSet, score_list
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register('scores/', ScoreViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
#    url(r'^/', include(router.urls)),
    url(r"^scoreboard/", ScoreBoardView.as_view()),
    url(r"^api/", score_list)
]

urlpatterns = format_suffix_patterns(urlpatterns)