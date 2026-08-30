from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from metrics.roi import weekly_hours_saved,weekly_cost_saved,annualized_savings
b=json.loads((ROOT/'data'/'baseline-metrics.json').read_text()); t=json.loads((ROOT/'data'/'target-metrics.json').read_text())
h=weekly_hours_saved(b['tickets_per_week'],b['manual_median_triage_minutes'],t['target_median_triage_minutes'])
w=weekly_cost_saved(h,b['estimated_loaded_hourly_cost_usd'])
print(f"Estimated weekly hours saved: {h:.1f}")
print(f"Estimated weekly labor value: ${w:,.0f}")
print(f"Estimated annualized labor value: ${annualized_savings(w):,.0f}")
