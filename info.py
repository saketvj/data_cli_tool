import sys
import csv


# Input Layer
# ------------------------
if(len(sys.argv) < 2):
    print("Usage: python info.py <filename> <col_nm>")
    sys.exit(1)

filename = sys.argv[1]
col_nm = sys.argv[2].lower() if len(sys.argv) > 2 else None


try:
    with open(filename,'r',newline='',encoding='utf-8-sig') as f:
        content = list(csv.reader(f,delimiter=','))
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)
    # for row in content:
        # print(row)
# -------------------------

# Data Processing Layer
#--------------------------

def str_to_float(item):
    try:
        return float(item)
    except (ValueError, TypeError):
        pass

def max_min_avg(data):
    try:
        data = [x for x in (str_to_float(item) for item in data) if x is not None]
        # print(data)
        avg = sum(data) / len(data)
        print(avg)
        return max(data), min(data), avg
    except ValueError:
        return "This col does not contain numerical values."


row_cnt = len(content) -1 if content else 0
col_cnt = len(content[0]) if content else 0

if content:
    columns = content[0]
else:
    columns = []

data_rows = content[1:] if row_cnt > 0 else []
top_5_rows = data_rows[:5]


def get_col_data(col_nm):
    headers = [c.lower() for c in content[0]]
    try:
        col_idx = headers.index(col_nm)
        # print(col_idx)
    except ValueError:
        print(f"Column '{col_nm}' not found.")
        sys.exit(1)
    col_data = []
    for row in data_rows:
        col_data.append(row[col_idx])
    # print(col_data[:5])
    return col_data

if col_nm:
    result = max_min_avg(get_col_data(col_nm))
    if isinstance(result, tuple):
        max_value,min_value,avg_value = result
    else:
        print(result)
        sys.exit(1)
# -------------------------
# Output Layer
#--------------------------

if col_nm:
    print('Maximum:', max_value, 'Minimum:' ,min_value,'Average:',avg_value)
else :
    print(f"Number of rows: {row_cnt}")
    print(f"Number of columns: {col_cnt}")
    print("Column names:")
    for col in columns:
        print(col) 
    print("Top 5 rows:")
    for row in top_5_rows:
        print(', '.join(row))

