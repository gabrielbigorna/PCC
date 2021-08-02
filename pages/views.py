from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import PageForm
from .models import Page
# from files.forms import FileForm
from files.models import File
from boxes.models import Box

# Create your views here.
@login_required
def pages(request, id):
    
    page = get_object_or_404(Page, pk=id)
    
    boxes = Box.objects.all().filter(user=request.user, id=id)
    
    search = request.GET.get('busca')

    if search:

        files = File.objects.filter(title__icontains=search, user=request.user, page_id=id)

    else:

        files_list = File.objects.all().order_by('-created_at').filter(user=request.user, page_id=id)

        paginator = Paginator(files_list, 5)

        pages = request.GET.get('page')

        files = paginator.get_page(pages)

    return render(request, 'pages/pages.html', {'page': page, 'boxes': boxes, 'files': files})

@login_required
def newPages(request, id):
       
    if request.method == 'POST':
        boxes = Box.objects.all().filter(user=request.user, id=id)
        form_page = PageForm(request.POST)

        if form_page.is_valid():
            page = form_page.save(commit=False)
            page.user = request.user
            page.save()
            return redirect('/boxes')

        else:
            return redirect('new-page', id=boxes.id)
        
    else:
        
        boxes = Box.objects.all().filter(user=request.user, id=id)
        
        pages = Page.objects.all().filter(user=request.user, ident=id)
        
        form_page = PageForm()

        return render(request, 'pages/newPages.html', {'form_page': form_page, 'boxes': boxes, 'pages': pages})  

