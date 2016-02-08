from django.views.generic import DetailView

from .models import Ad


class AdDetailVew(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        result = super(AdDetailVew, self).get(request, *args, **kwargs)
        Ad.hits_plus(self.object, request.user)
        return result
