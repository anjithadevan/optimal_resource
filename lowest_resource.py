import re
from collections import OrderedDict

units_map = {
    'Large': 10,
    'XLarge': 20,
    '2XLarge': 40,
    '4XLarge': 80,
    '8XLarge': 160,
    '10XLarge': 320,
}

newyork_cost_map = {
    'Large': 120,
    'XLarge': 230,
    '2XLarge': 450,
    '4XLarge': 774,
    '8XLarge': 1400,
    '10XLarge': 2820,
}

india_cost_map = {
    'Large': 140,
    '2XLarge': 413,
    '4XLarge': 890,
    '8XLarge': 1300,
    '10XLarge': 2970,
}

china_cost_map = {
    'Large': 110,
    'XLarge': 200,
    '4XLarge': 670,
    '8XLarge': 1180,
}


cost_country_map = OrderedDict([
    ('New York', newyork_cost_map),
    ('India', india_cost_map),
    ('China', china_cost_map),
])


def parse_input(text):
    """
    Parse text to units and hours
    Capacity of 1150 units for 1 Hour ==> 1150, 1
    1100 units for 12 Hours ==> 110, 12
    """
    units, hours = re.findall(r'\d+', text)
    return int(units), int(hours)


def get_sorted_keys_based_on_value(dict_data):
    """
    Sort a dict keys based on value - in increasing order
    """
    sorted_keys = list()
    for key, value in sorted(dict_data.items(), key=lambda item: item[1]):
        sorted_keys.append(key)
    return sorted_keys


def get_preference_order(country):
    """
    Identify the preferred machine order.
    The lowest cost item should be considered first
    """
    machine_to_per_unit_price = dict()
    for machine, cost in cost_country_map[country].items():
        machine_to_per_unit_price[machine] = float(cost)/float(units_map.get(machine))
    return get_sorted_keys_based_on_value(machine_to_per_unit_price)


def get_optimal_resource(input_text):
    all_units, hours = parse_input(input_text)
    print(all_units, hours)

    output_list = []
    for country, cost_map in cost_country_map.items():
        machines = list()
        total_cost = 0
        pending_units = all_units
        for machine in get_preference_order(country):
            machine_cost = cost_map.get(machine)
            units = units_map[machine]
            # maximum accommodate with lowest cost machine for that country
            number_required = pending_units/units
            if number_required:
                # Find cost based on hours and machine chosen and its count
                total_cost = total_cost + number_required*machine_cost*hours
                machines.append((machine, number_required))
                pending_units = pending_units - units*number_required
                if pending_units <= 0:
                    break

        output_list.append({
            "region": country,
            "total_cost": "$%s" % total_cost,
            "machines": machines,
        })
    return {"Output": output_list}

print (get_optimal_resource("1100 units for 12 Hours"))