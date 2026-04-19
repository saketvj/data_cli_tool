import sys
import csv


# Input Layer
# ------------------------
if(len(sys.argv) != 2):
    print("Usage: python info.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename,'r',newline='',encoding='utf-8-sig') as f:
        content = list(csv.reader(f,delimiter=';'))
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)
    # for row in content:
        # print(row)
# -------------------------

# Data Processing Layer
#--------------------------
row_cnt = len(content) -1 if content else 0
col_cnt = len(content[0]) if content else 0

if content:
    columns = content[0]
else:
    columns = []

data_rows = content[1:] if row_cnt > 0 else []
top_5_rows = data_rows[:5]
# -------------------------
# Output Layer
#--------------------------

print(f"Number of rows: {row_cnt}")
print(f"Number of columns: {col_cnt}")
print("Column names:")
for col in columns:
    print(col) 
print("Top 5 rows:")
for row in top_5_rows:
    print(', '.join(row))
