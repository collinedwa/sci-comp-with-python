def add_time(start, duration, day=None):
  week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
  days = 0
  time = duration.split(':')
  start_time = start.split(':')
  time_of_day = start_time.pop(1).split(' ')
  start_time.append(time_of_day[0])
  time_secondstep = [int(time[0])+int(start_time[0]),int(time[1])+int(start_time[1])]
  hours = time_secondstep[0]
  minutes = time_secondstep[1]
  final_AMPM = time_of_day[1]
  if minutes >= 60:
    minuteoverlap = minutes // 60
    minutes -= (60*minuteoverlap)
    hours += minuteoverlap
  if hours >= 24:
    days = hours // 24
    if hours%24 != 0:
        hours -= (24*days)
    elif hours%24 == 0:
        hours = (int(time[0])%24) + int(start_time[0])
  if hours >= 12:
    if hours > 12:
        hours -= 12
    if time_of_day[1] == 'PM':
        final_AMPM = 'AM'
        days += 1
    elif time_of_day[1] == 'AM':
        final_AMPM = 'PM'
  if minutes < 10:
    minutes = '0'+str(minutes)    
  if day != None:
    finalday = week.index(str(day).lower())
    finalday += days
    if finalday > 6:
      if days%7 == 0:
        finalday = week.index(str(day).lower())
      else:
        finalday = week.index(str(day).lower()) + (days%7 - 6)-1
    if days == 0:
        return(f'{hours}:{minutes} {final_AMPM}, {week[finalday].capitalize()}')
    elif days == 1:
        return(f'{hours}:{minutes} {final_AMPM}, {week[finalday].capitalize()} (next day)')
    else:
        return(f'{hours}:{minutes} {final_AMPM}, {week[finalday].capitalize()} ({days} days later)')   
  if day == None:
    if days == 0:
        return(f'{hours}:{minutes} {final_AMPM}')
    elif days == 1:
        return(f'{hours}:{minutes} {final_AMPM} (next day)')
    else:
        return(f'{hours}:{minutes} {final_AMPM} ({days} days later)')  