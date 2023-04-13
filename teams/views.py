# from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict
from .utils import data_processing
from .models import Team


# Create your views here.
class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        teams_list = [model_to_dict(team) for team in teams]

        return Response(teams_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_201_CREATED)
