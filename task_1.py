str = '1h 45m,360s,25m,30m 120s,2h 60s'
hours = 0
min = 0
sec = 0
times = str.replace(' ', ',').split(',')
for time in times:
    if 'h' in time:
        hours += int(time[0 : len(time)-1])
    elif 'm' in time:
        min += int(time[0 : len(time)-1])
    elif 's' in time:
        sec += int(time[0 : len(time)-1])   
total = hours * 60 + min + sec / 60
print(total)     