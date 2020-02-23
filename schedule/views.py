from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from mscripts import exploree


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        uploaded_file.name = 'DATATP.xlsx'
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'schedule/upload.html')


def index(request):
    print(")))")
    return render(request, 'schedule/index.html')


def view_func(request):
    exploree.cargo_axis_pointer(4, 2)
    print("!!!")
    return render(request, "schedule/schedul.html")
