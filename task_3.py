world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
world_champions[2022] = 'Аргентина'

keys_list = list(world_champions.keys())
values_list = list(world_champions.values())
for i in range(len(keys_list)):
    print(str(keys_list[i]) + ' - ' + values_list[i])

country = 'Италия'
if country in values_list:
    for i in range(len(values_list)):
        if values_list[i] == country:
            print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
            break
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке')
