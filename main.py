# -*- coding: utf-8 -*-
import os
import logging
import pandas as pd


_logger = logging.getLogger(__name__)
OUTPUT_DIR = './data'


def get_input_file_name():
    # Get input file name from user input in terminal
    input_file_name = input('Enter the input file name: ')
    return input_file_name


if __name__ == '__main__':
    filename = get_input_file_name()
    df = pd.read_excel(filename, sheet_name='Sheet1', header=0)
    content = df['Nội dung']

    content = content.astype('string')
    # noi_dung = (
    #     content.str.replace(',', ' ')
    #     .str.replace('-', ' ')
    #     .str.replace('_', ' ')
    #     .str.replace(';', ' ')
    #     .str.replace('.', ' ')
    # )
    content = content.str.replace("[^0-9:]+", ' ', regex=True)
    render_ids = []
    for items in content:
        try:
            split_items = items.split(' ')
            ids = ', '.join(list(filter(
                lambda i: len(i) == 8 and i.isnumeric(), split_items))
            )
            render_ids.append(ids)
        except Exception as e:
            render_ids.append('')
            _logger.error(f'Can not get ID with  error :{e}')
    final = df.assign(Data=pd.Series(render_ids))
    output_file_dir = os.path.join(OUTPUT_DIR, 'final.xlsx')
    final.to_excel(output_file_dir)
