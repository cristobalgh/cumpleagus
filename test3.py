import datetime

now = datetime.datetime.now()

#my_birthday = datetime.datetime(now.year, 12, 27, 0, 0, 0)
my_birthday = datetime.datetime(now.year, 12, 27, 3, 3, 3)
#hora de nacimiento real, los segundos son invento mio...
#(año, mes, dia, hora, minuto, segundos
si_cumple = now.month==my_birthday.month and now.day==my_birthday.day

if my_birthday < now:
    my_birthday = my_birthday.replace(year=now.year + 1)
dt = abs(my_birthday - now)
falta = dt.days
segs = round(dt.total_seconds())
horas = round(segs/60/60)
#d=str(dt)
#d=d.replace("days","días")
#d=d.replace("day", "día")
#segs=d

# arbitrary number of seconds
days = dt.days
s = dt.seconds
# hours
hours = s // 3600 
# remaining seconds
s = s - (hours * 3600)
# minutes
minutes = s // 60
# remaining seconds
seconds = s - (minutes * 60)
# total time
#print '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
# result: 03:43:40

print(days,"d", hours,"h", minutes,"m", seconds,"s")
segs = str(days) + "d" + str(hours) + "h" + str(minutes) + "m" + str(seconds) + "s"