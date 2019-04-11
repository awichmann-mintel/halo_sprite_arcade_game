from django.views import View
from django.shortcuts import render
from .models import ScoresModel
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ScoreSerializer


@api_view(['GET', 'POST'])
def score_list(request):
    if request.method == 'GET':
        scores = ScoresModel.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScoreBoardView(View):
    def get(self, request):
        return render(request, 'highscore/scoreboard.html', {"scores": ScoresModel.objects.all()})


# ViewSets define the view behavior.
class ScoreViewSet(viewsets.ModelViewSet):
    queryset = ScoresModel.objects.all()
    serializer_class = ScoreSerializer
