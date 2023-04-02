from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView

from .models import Notes

class NotesCreateView(CreateView):
    model= Notes
    fields =['title', 'text']
    success_url = '/smart/notes'

"""
def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})
    """

class NotesViewList(ListView):
    model= Notes
    context_object_name= 'notes'
    template_name= "notes/notes_list.html"

class NotesDetailView(DetailView):  #DetailView also takes care of the exception
    model= Notes
    context_object_name= 'note'
    template_name= "notes/notes_details.html"

'''
def details(request, pk):
    try:
        note= Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exixt")
    return render(request, 'notes/notes_details.html', {'note': note})
'''