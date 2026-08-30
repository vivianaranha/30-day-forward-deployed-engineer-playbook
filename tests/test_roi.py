from metrics.roi import weekly_hours_saved,weekly_cost_saved,annualized_savings
def test_roi():
 h=weekly_hours_saved(100,6,3); assert h==5; w=weekly_cost_saved(h,40); assert w==200; assert annualized_savings(w)==10400
