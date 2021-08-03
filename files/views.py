from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FileForm
from .models import File
from pages.forms import PageForm
from pages.models import Page


# Create your views here.
@login_required
def fileView(request, id):
    file = get_object_or_404(File, pk=id)

    return render(request, 'files/fileView.html', {'file': file})

@login_required
def newFile(request, id):
    if request.method == 'POST':
        page = get_object_or_404(Page, pk=id)
        form = FileForm(request.POST)
        pages = Page.objects.all().filter(user=request.user, ident=id) 

        if form.is_valid():
            file = form.save(commit=False)
            file.done = 'fazendo'
            file.user = request.user
            file.page_id = page
            file.save()
            return redirect('pages', id=id)
        
        else:
            return redirect('new-file', id=id)

    else:
        form = FileForm()

        pages = Page.objects.all().filter(user=request.user, ident=id)

        return render(request, 'files/newFile.html', {'form': form, 'pages': pages})

@login_required
def editFile(request, id):
    file = get_object_or_404(File, pk=id)
    form = FileForm(instance=file)

    pages = Page.objects.all().filter(user=request.user, ident=id)

    if(request.method == 'POST'):
        form = FileForm(request.POST, instance=file)

        if(form.is_valid()):
            file.save()
            # return redirect('pages', id=file.id)
        
        # return redirect('boxes')
        return HttpResponse(request, "Here's the text of the Web page.")
    else:
        return render(request, 'files/editFile.html', {'form': form, 'file': file, 'pages': pages})

@login_required
def deleteFile(request, id):
    file = get_object_or_404(File, pk=id)
    file.delete()

    messages.info(request, 'File deletado com sucesso.')

    return redirect('pages', id=id)