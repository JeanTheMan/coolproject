import textrender as tr
from time import sleep
import requests
#component()
elines = tr.editablelist([])
tr.setstartscreen(elines)
pic = tr.strtopic(""".-.   .-..-.   .-..----.            
| |   | ||  `.'  || {_              
| `--.| || |\ /| || {__             
`----'`-'`-' ` `-'`----'            
 .----. .-. .-.  .--.  .----. .----.
/  {}  \|  `| | / {} \ | {}  \| {_  
\      /| |\  |/  /\  \|     /| {__ 
 `----' `-' `-'`-'  `-'`----' `----'""")
tr.picture(7, 7, pic.picture, elines)
#tr.component(3, 4 ,6 ,6, elines)
pic = tr.strtopic('Type "start" to start')
tr.picture(15, 15, pic.picture, elines)
tr.updatescreen(elines.list)
started = False
while not started:
  i = input().lower()
  if i == 'start':
    started = True
  else:
    tr.updatescreen(elines.list)
