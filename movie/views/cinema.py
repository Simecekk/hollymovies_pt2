from django.views.generic import ListView, DetailView

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
        # TODO Check whether solds_tickets isn't bigger than all tickets count
        # TODO add bucket to Cinema so we can add money to it
        self.object = self.get_object()
        self.object.sold_tickets += 1
        self.object.save(update_fields=['sold_tickets', ])
        return self.get(request, *args, **kwargs)