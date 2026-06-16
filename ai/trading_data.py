from pathlib import Path
import sys

import pandas as pd

csv_path = Path(__file__).with_name('trading_data.csv')

if not csv_path.exists():
	print(f'Missing CSV file: {csv_path.name}')
	sys.exit(1)

if csv_path.stat().st_size == 0:
	print(f'{csv_path.name} is empty')
	sys.exit(0)

data = pd.read_csv(csv_path)
print(data.head())