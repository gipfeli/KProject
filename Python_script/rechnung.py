from qrbill.bill import QRBill

my_bill = QRBill(
    account='CH3181190000004593766',
    creditor={
        'name': 'Chanh Dat Nguyen', 
        'street': 'Reussmatt', 'house_num': '3',
        'pcode': '6032', 'city': 'Emmen',
    },
    debtor={
        'name': 'Khanh Bang Nguyen', 
        'street': 'Reussmatt', 'house_num': '3',
        'pcode': '6032', 'city': 'Emmen',
    },
    extra_infos='Blackmail',
    due_date='2020-02-29',
    amount='100.00'
)

my_bill.as_svg('test.svg')