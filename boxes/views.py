from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BoxForm
from .models import Box
from pages.forms import PageForm
from pages.models import Page
import pages.urls


# Create your views here.
@login_required
def boxes(request):
    search = request.GET.get('busca')

    if search:

        boxes = Box.objects.filter(title__icontains=search, user=request.user)

    else:

        boxes_list = Box.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(boxes_list, 5)

        page = request.GET.get('page')

        boxes = paginator.get_page(page)

    return render(request, 'boxes/boxes.html', {'boxes': boxes})

@login_required
def boxView(request, id):
    box = get_object_or_404(Box, pk=id)
    return render(request, 'boxes/boxView.html', {'box': box})

@login_required
def newBox(request):
    if request.method == 'POST':
        form = BoxForm(request.POST)

        if form.is_valid():
            box = form.save(commit=False)
            box.user = request.user
            box.save()

            return redirect('new-pages', id=box.id)

    else:
        form = BoxForm()
        return render(request, 'boxes/newBox.html', {'form': form})

@login_required
def editBox(request, id):
    box = get_object_or_404(Box, pk=id)
    form = BoxForm(instance=box)

    if(request.method == 'POST'):
        form = BoxForm(request.POST, instance=box)

        if(form.is_valid()):
            box.save()
            return redirect('/boxes')

        else:
            return render(request, 'boxes/editBox.html', {'form': form, 'box': box})

    else:
        return render(request, 'boxes/editBox.html', {'form': form, 'box': box})

@login_required
def deleteBox(request, id):
    box = get_object_or_404(Box, pk=id)
    box.delete()

    messages.info(request, 'Box deletado com sucesso.')

    return redirect('/boxes')