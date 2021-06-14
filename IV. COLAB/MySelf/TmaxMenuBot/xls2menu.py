"""
This code is for get menu from a xlsx file.
Parsing str(xlsx) to menu.
"""

import pandas as pd
from dataclasses import dataclass


@dataclass
class Application:
    xlsx_path: str = 'input\\'


df = pd.DataFrame()
