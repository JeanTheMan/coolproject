import textrender as tr
from time import sleep
#component()
elines = tr.editablelist([])
tr.setstartscreen(elines)
pic = tr.strtopic('''O       O
{_______}''')
tr.picture(7, 7, pic.picture, elines)
tr.component(3, 4 ,6 ,6, elines)
pic = tr.strtopic('Yay')
tr.picture(3, 13, pic.picture, elines)
tr.updatescreen(elines.list)
    
