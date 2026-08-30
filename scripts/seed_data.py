from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'data'/'tickets.csv').open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
print(f"Loaded {len(rows)} sample tickets.")
for row in rows[:3]: print(row['ticket_id'],'-',row['subject'])
