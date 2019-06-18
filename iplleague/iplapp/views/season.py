from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import resolve
from django.views import View

from iplapp.models import *


class SeasonView(View):
    def get(self,request,*args,**kwargs):
        all_seasons = Matches.objects.values('season').distinct()
        seasons_list = []
        for season in all_seasons:
            seasons_list.append(season['season'])
        seasons_list.sort(reverse=True)
        if kwargs:
            season = Matches.objects.filter(season=kwargs['year'])
        return render(
            request,
            template_name='season.html',
            context={'season': season,
                     'current_season': kwargs['year'],
                     'season_list': seasons_list},
        )


class SeasonPageView(View):
    def get(self,request,*args,**kwargs):
        all_seasons = Matches.objects.values('season').distinct()
        seasons_list = []
        for season in all_seasons:
            seasons_list.append(season['season'])
        seasons_list.sort(reverse=True)
        if kwargs:
            season = Matches.objects.filter(season=kwargs['year'])
        start_position = (kwargs['page_no']-1)*8
        max_page = list(range(1, len(season)//8+2))
        if kwargs['page_no'] != 1:
            prev_page = kwargs['page_no'] - 1
        else:
            prev_page = kwargs['page_no']
        if kwargs['page_no'] != len(max_page):
            next_page = kwargs['page_no'] + 1
        else:
            next_page = kwargs['page_no']
        season = season[start_position:start_position+8]
        return render(
            request,
            template_name='season_page.html',
            context={'season': season,
                     'current_season': kwargs['year'],
                     'season_list': seasons_list,
                     'max_page': max_page,
                     'prev_page': prev_page,
                     'next_page': next_page},
        )


class MatchView(LoginRequiredMixin, View):
    login_url='/login/'
    def get(self, request, *args, **kwargs):
        match = Deliveries.objects.filter(match=kwargs['id'])
        season = Matches.objects.get(id=kwargs['id'])
        return render(
            request,
            template_name='match.html',
            context={'match': match,
                     'season': season}
        )
