from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages

from movie.models import Cinema, CinemaMovieScreening


class CinemaListView(ListView):
    model = Cinema
    template_name = 'cinemas/list.html'


class CinemaDetailView(DetailView):
    model = Cinema
    template_name = 'cinemas/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CinemaDetailView, self).get_context_data(**kwargs)
        screenings = self.object.screenings.all()

        active_screenings = []
        for screening in screenings:
            if screening.is_closed:
                continue
            elif screening.soldout:
                continue
            active_screenings.append(screening)

        context.update({
            'screenings': active_screenings
        })
        return context


class ScreeningDetailView(DetailView):
    model = CinemaMovieScreening
    template_name = 'cinemas/screening_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.available_tickets <= 0:
            messages.error(request, 'There are is no more tickets left. Please look for another screening')
            return redirect('cinema:list')
        self.object.sold_tickets += 1
        cinema = self.object.cinema
        cinema.finances += self.object.ticket_price
        cinema.save(update_fields=['finances'])
        self.object.save(update_fields=['sold_tickets', ])
        return self.get(request, *args, **kwargs)
