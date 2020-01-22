"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

def prn_imncome_report(arr):
    """
    function calculates average anual income of companies in array arr and
    prints:
        - list of companies with the income above average
        - list of companies with the income below average

    :param arr: array of namedtuple CompanyInfo
    :return: integer - average income
    """
    profitable = []
    unprofitable = []
    income = 0

    for j, _ in enumerate(arr):
        income = income + int(arr[j].first_q) + int(arr[j].second_q) + \
                 int(arr[j].third_q) +  int(arr[j].forth_q)
    income /= len(arr)

    for k, _ in enumerate(arr):
        if int(arr[k].first_q) + int(arr[k].second_q) + int(arr[k].third_q) + \
                int(arr[k].forth_q) < income:
            unprofitable.append(arr[k].c_name)
        else:
            profitable.append(arr[k].c_name)
    print(f"Average annual income is: {income}")
    print(f"Profitable companies with above than average income are: {profitable}")
    print(f"Unprofitable companies with below than average income are: {unprofitable}")
    return income

CompanyInfo = namedtuple("CompanyInfo", ["c_name", "first_q", "second_q", "third_q", "forth_q"])

DATASET = []
DATA_RECORDS = int(input("Input records number: "))

for i in range(DATA_RECORDS):
    input_data = input("""Input company info (split separated):
    'Company Name' 'Q1 income' 'Q2 income' 'Q3 income' 'Q4 income': """)
    input_data = input_data.split(" ")
    COMPANY = CompanyInfo(input_data[0], input_data[1], input_data[2], \
                            input_data[3], input_data[4])
    DATASET.append(COMPANY)
    del COMPANY
prn_imncome_report(DATASET)
