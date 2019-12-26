from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from mscripts import exploree


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        # analyze(fs)
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'schedule/upload.html')


def index(request):
    return render(request, 'schedule/index.html')


def view_func(request):
    values = exploree.cargo_axis_pointer(0, 2)
    return render(request, "schedule/upload.html", {'values': values})
