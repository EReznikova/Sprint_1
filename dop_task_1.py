types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

def delete_duplicates(tickets):
    keys_list = list(tickets.keys())
    value_list = list(tickets.values())
    for i in range(len(value_list)):
        line = value_list[i]
        for j in range(len(line)):
            for k in range(i+1,len(value_list)):
                if line[j] in value_list[k]:
                    arr = value_list[k]
                    arr.remove(line[j])
                    value_list[k] = arr

    for i in range(len(value_list)):
        tickets[keys_list[i]] = value_list[i]

def create_tickets_by_type(types, tickets):
    result = {}
    for key in types.keys():
        result[types[key]] = tickets[key]
    return result

delete_duplicates(tickets)
tickets_by_type = create_tickets_by_type(types, tickets)