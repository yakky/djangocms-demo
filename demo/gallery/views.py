from django.views.generic import ListView
from .models import SuperSizedGallery

class View(ListView):
    model = SuperSizedGallery

    def get_queryset(self):
        print self.model.objects.all()
        return self.model.objects.all()