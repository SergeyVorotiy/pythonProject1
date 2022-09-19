from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView

from .models import FileWordCounts
from .forms import FileForm
# Create your views here.


class FileModelView(CreateView):
    model = FileWordCounts
    form_class = FileForm
    context_object_name = 'file_word_counter'
    template_name = 'template.html'

    def get(self, request, *args, **kwargs):
        get = self.request.GET['wordcount'] if 'wordcount' in self.request.GET.keys() else ''
        return render(request=request, template_name='template.html', context={
            'wordcount':FileWordCounts.word_count(get),
        })


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['uniwordcount'] = FileWordCounts.uni_count()
        if 'wordcount' in self.request.GET.keys():
            context['wordcount'] = FileWordCounts.word_count(self.request.GET['wordcount'])
        return context

    def form_valid(self, form):
        file_word = form.save()
        file = FileWordCounts.objects.last()
        file.set_text()
        context = self.get_context_data()

        context['uniwordcount'] = FileWordCounts.uni_count()
        return HttpResponseRedirect('/')


def clear(request):
    FileWordCounts.objects.all().delete()
    return HttpResponseRedirect('/')

