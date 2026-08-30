def weekly_hours_saved(tickets_per_week,baseline_minutes,new_minutes): return max(0.0,baseline_minutes-new_minutes)*tickets_per_week/60.0
def weekly_cost_saved(hours_saved,hourly_cost): return hours_saved*hourly_cost
def annualized_savings(weekly_savings): return weekly_savings*52
