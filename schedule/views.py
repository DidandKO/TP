from django.shortcuts import render
from .models import Amperage
from openpyxl import load_workbook


def upload(request):
    ampers_cargo_axis = [[[], [], [], [], []]]
    Amperage.objects.all().delete()
    operation_array = [31, 36, 37, 38, 40, 41, 44, 46, 49, 50, 51, 55]
    try:
        if request.method == 'POST':
            uploaded_file = request.FILES['document']
            wb = load_workbook(uploaded_file, data_only=True)
            table = wb['Таблица']
            vb_cargo = {0: 3, 1: 15, 2: 27, 3: 39, 4: 51}
            vb_axis = {0: 'S', 1: 'T', 2: 'U', 3: 'V', 4: 'W', 5: 'X'}
            for i in range(6):  # ось
                ampers_cargo = []
                for j in range(5):  # нагрузка
                    ampers = []
                    for k in range(12):  # операция
                        _adressX = 'R' + str(vb_cargo.get(j) + k)
                        _adressY = str(vb_axis.get(i)) + str(vb_cargo.get(j) + k)
                        amper = Amperage(cargo=j, operation=int(table[_adressX].value), axis=i+1,
                                         value=table[_adressY].value)
                        amper.save()  # сохранение значения тока по операции
                        ampers.append(amper.value)
                    ampers_cargo.append(ampers)
                ampers_cargo_axis.append(ampers_cargo)
                ampers_cargo_axis.pop(0)
    except Exception:
        print('Find a problem!')
        pass
    print(ampers_cargo_axis)
    return render(request, 'schedule/upload.html', context={'ampers_cargo_axis00': ampers_cargo_axis[0][0],
                                                            'ampers_cargo_axis01': ampers_cargo_axis[0][1],
                                                            'ampers_cargo_axis02': ampers_cargo_axis[0][2],
                                                            'ampers_cargo_axis03': ampers_cargo_axis[0][3],
                                                            'ampers_cargo_axis04': ampers_cargo_axis[0][4],
                                                             'operation_array': operation_array})


def index(request):
    print(")))")
    return render(request, 'schedule/index.html')
