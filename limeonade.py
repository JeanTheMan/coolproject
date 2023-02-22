import textrender as tr
def loadstartscreen(elines):
  tr.setstartscreen(elines)
  pic = tr.strtopic(""".-.   .-..-.   .-..----.            
| |   | ||  `.'  || {_              
| `--.| || |\ /| || {__             
`----'`-'`-' ` `-'`----'            
 .----. .-. .-.  .--.  .----. .----.
/  {}  \|  `| | / {} \ | {}  \| {_  
\      /| |\  |/  /\  \|     /| {__ 
 `----' `-' `-'`-'  `-'`----' `----'""")
  tr.picture(30, 12, pic.picture, elines)
  #tr.component(3, 4 ,6 ,6, elines)
  pic = tr.strtopic('''Type "start" to start
  Type "load" to check for a game
  Type "credits" to view credits''')
  tr.picture(30, 20, pic.picture, elines)
  tr.updatescreen(elines.list)

def newscreen():
  return tr.editablelist([])

def refresh(el):
  elines = el.list
  return tr.updatescreen(elines)

def loadstr(string):
  return tr.strtopic(string)