daily_energy_consumption = 5

#TO DO: Build and return an array which stores the energy value at each row at a separate index in the array
def individual_energy_totals(energy_data):
    totals = []
    row = energy_data.fetchone()
    index = 0
    while row:
        totals.append(row[0])
        row = energy_data.fetchone()
        index = index + 1
    return totals

#TO DO: Return the sum of the values at each index of the passed array
def total_energy(individial_energy_totals):
    total = 0
    for sub_total in individial_energy_totals:
        if sub_total == None:
            break
        total += sub_total
    return total

#TO DO: Return value obtained by dividing the total energy by the energy unit
def energy_analogy_value(total_energy, energy_unit):
    return total_energy / energy_unit

#TO DO: Given the total energy produced and the price per KWh, return the money saved
def money_saved(total_energy, price_per_kwh):
    return total_energy * price_per_kwh

#TO DO: Given the total energy produced and the timescale, use the global variable to calculate
#what percentage of the building's total energy consumption is accounted for by the panels
def energy_percentage(total_energy, days):
    return total_energy / (daily_energy_consumption * days)