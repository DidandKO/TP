from openpyxl import load_workbook


# метод для получения значений тока на осях робота при нулевой нагрузке
# возвращает набор точек (название операции/среднее значение тока за 3 итерации)
def cargo_axis_pointer(_cargo, _axis):
    zero_axis = []
    vb_cargo = {0: 3, 1: 15, 2: 27, 3: 39, 4: 51}
    vb_axis = {1: 'S', 2: 'T', 3: 'U', 4: 'V', 5: 'W', 6: 'X'}
    wb = load_workbook("D:\Python\PyProjs\TP\media\DATATP.xlsx", data_only=True)
    print(wb.sheetnames)
    table = wb['Таблица']
    for i in range(12):
        _adressX = 'R' + str(vb_cargo.get(_cargo)+i)
        _adressY = str(vb_axis.get(_axis)) + str(vb_cargo.get(_cargo)+i)
        print(str(table[_adressX].value) + '-' + str(table[_adressY].value))
        zero_axis.append([table[_adressX].value, table[_adressY].value])
    print(zero_axis)

