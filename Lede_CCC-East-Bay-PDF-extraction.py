import pandas as pd

import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('max_seq_item', None)


from PyPDF2 import PdfReader


readerall = PdfReader('ccc_eastbay_mergedsalaries.pdf')
for pageall in readerall.pages:
    salaries_all = pageall.extract_text()
    print(salaries_all)