# -*- coding: utf-8 -*-
# Copyright 2022 Init, Ltd (https://www.init.vn/)
import pandas
import pandas as pd

if __name__ == '__main__':
    hssv = pd.read_excel('hssv.xlsx', sheet_name='TH-7777', header=0)
    noi_dung = hssv['Nội dung']

    noi_dung = noi_dung.astype('string')
    # noi_dung = noi_dung.str.replace(',', ' ').str.replace('-', ' ').str.replace('_', ' ').str.replace(';', ' ').str.replace('.', ' ')
    noi_dung = noi_dung.str.replace("[^0-9:]+", ' ', regex=True)
    render_mssv = []
    for items in noi_dung:
        split_items = items.split(' ')
        mssvs = ', '.join(list(filter(lambda i: len(i) == 8 and i.isnumeric(), split_items)))
        render_mssv.append(mssvs)
    final = hssv.assign(MSSV=pandas.Series(render_mssv))
    final.to_excel('final-hssv.xlsx')
