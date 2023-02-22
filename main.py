import limeonade as li
#component()
elines = li.newscreen()
li.loadstartscreen(elines)
started = False
while not started:
  i = input().lower()
  if i == 'start':
    started = True
  else:
    li.refresh(elines)
elines = li.newscreen()
pic = li.loadstr('new')
