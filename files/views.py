from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FileForm
from .models import File



# Create your views here.
@login_required
def files(request):
    search = request.GET.get('busca')

    if search:

        files = File.objects.filter(title__icontains=search, user=request.user)

    else:

        files_list = File.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(files_list, 5)

        page = request.GET.get('page')

        files = paginator.get_page(page)

    return render(request, 'files/files.html', {'files': files})

@login_required
def fileView(request, id):
    file = get_object_or_404(File, pk=id)
    return render(request, 'files/fileView.html', {'file': file})

@login_required
def newFile(request):
    if request.method == 'POST':
        form = FileForm(request.POST)

        if form.is_valid():
            file = form.save(commit=False)
            file.done = 'fazendo'
            file.user = request.user
            file.save()
            return redirect('/files')

    else:
        form = FileForm()
        return render(request, 'files/newFile.html', {'form': form})

@login_required
def editFile(request, id):
    file = get_object_or_404(File, pk=id)
    form = FileForm(instance=file)

    if(request.method == 'POST'):
        form = FileForm(request.POST, instance=file)

        if(form.is_valid()):
            file.save()
            return redirect('/files')

        else:
            return render(request, 'files/editFile.html', {'form': form, 'file': file})

    else:
        return render(request, 'files/editFile.html', {'form': form, 'file': file})

@login_required
def deleteFile(request, id):
    file = get_object_or_404(File, pk=id)
    file.delete()

    messages.info(request, 'File deletado com sucesso.')

    return redirect('/files')