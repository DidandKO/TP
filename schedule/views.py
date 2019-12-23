from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# from openpyxl import load_workbook
# Create your views here.


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        # analyze(fs)
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'schedule/upload.html')


def show(request):
    return render(request, "schedule/schedulee.html")


def index(request):
    return render(request, 'schedule/index.html')


# def analyze(_excel_file):
#     try:
#         wb2 = load_workbook(_excel_file)
#
#     except BaseException:
#         pass
#     pass
