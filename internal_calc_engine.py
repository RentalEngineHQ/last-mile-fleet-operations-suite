# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(gross_route_revenue, fleet_fuel_costs, route_maintenance_fees):
    total_system_expense = float(fleet_fuel_costs) + float(route_maintenance_fees)
    gross_revenue = float(gross_route_revenue)
    true_net_cash_margin = gross_revenue - total_system_expense
    return [gross_revenue, total_system_expense, true_net_cash_margin]
