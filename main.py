from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
ident(transform)

'''
l = open ("script","w")

s = "line\n"
s+= "200 200 0 199 200 0\n" 
l.write(s)


for x in range (0,360,1):
    s = "rotate\n"
    s+= "z 1\n"
    s+= "draw_current\n"
    s+= "apply\n"
    l.write(s)

s = "display\n"    
s+= "save\n"
s+= "pic.png\n"
s+= "display"

l.write(s)
'''

parse_file( 'script', edges, transform, screen, color )
