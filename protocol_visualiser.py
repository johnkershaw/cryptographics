# if PIL isn't working in VS Code, 
# run these three lines to find out where your Python interpreter lives:
# import sys
# print(sys.executable)
# quit()

# then force THAT Python to install pillow:
# pasted your /path/to/python/used/by/vs/code/python -m pip install pillow

import re
import turtle
import math
# import ghostscript

from PIL import Image
from PIL import ImageGrab

t = turtle.Turtle()
t.hideturtle()
turtle.tracer(5)
turtle.setup(0.3, 0.85, 0, 0)
x = -200
y = 300
w = 50
h = w
r = h/2

testing = True

#TODO head and shoulders


def draw_clock(t=turtle.Turtle(), x=0, y=0, w=100, h=100):
    t.fillcolor("#D0D0D0")
    t.begin_fill()
    t.teleport(x+w/2, y-h*3/4)
    t.circle(h/4)
    t.end_fill()
    t.teleport(x+w/2, y-h/2)
    t.seth(150)
    t.fd(h/6)
    t.bk(h/6)
    t.seth(30)
    t.fd(h/6)
    t.seth(0)
    t.fillcolor("black")
    t.teleport(x+w/2, y)

def draw_key(t=turtle.Turtle(), text="", x=0, y=0, w=100, h=100):
    t.fillcolor("#D0D0D0")
    t.begin_fill()
    t.teleport(x, y-h/4)
    t.circle(h/4, 275)
    t.seth(225)
    t.fd(h/2)
    t.lt(45)
    t.fd(h/4)
    t.lt(90)
    t.fd(h/4)
    t.lt(90)
    t.fd(h/8)
    t.rt(90)
    t.fd(h/8)
    t.lt(90)
    t.fd(h/8)
    t.rt(90)
    t.fd(h/8)
    t.lt(90)
    t.fd(h/8)
    t.rt(90)
    t.fd(h/8)
    t.end_fill()
    t.teleport(x, y-8)
    t.write(text, align="center", font = ("Arial", 8, "bold"))
    t.teleport(x+w/2, y-h/2)
    t.fillcolor("black")
    t.teleport(x+w/2, y)
    t.seth(0)

def draw_message(t=turtle.Turtle(), text="", x=0, y=0, w=100, h=100):
    t.teleport(x-w/2, y+h/2)
    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.rt(90)
    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.rt(90)
    t.teleport(x, y-8)
    t.write(text, align="center", font = ("Arial", 8, "bold"))
    t.teleport(x+w/2, y)

def draw_interceptor(t=turtle.Turtle(), text="", x=0, y=0, w=100, h=100):
    long_side = math.sqrt(pow(w/2, 2) + pow(h, 2))
    short_side = math.sqrt(pow(w/2, 2) + pow(3*h/8, 2))
    a = math.degrees(math.asin(h/long_side))
    b = math.degrees(math.asin((3*h/8) / short_side))

    t.teleport(x-w/2, y-h/2)
    t.seth(a)
    t.fd(long_side)
    t.seth(360-a)
    t.fd(long_side)
    t.seth(180-b)
    t.fd(short_side)
    t.seth(180+b)
    t.fd(short_side)
    t.seth(0)
    t.teleport(x, y-8)
    t.write(text, align="center", font = ("Arial", 8, "bold"))
    t.teleport(x+w/2, y)

def draw_server(t=turtle.Turtle(), text="", x=0, y=0, w=100, h=100):
    r = math.sqrt(pow(w/2, 2) + pow(h, 2))
    a = math.degrees(math.atan(2*h/w))
    e = 180 - 2*a

    t.teleport(x-w/2, y+3*h/8)
    t.seth(90 - a)
    t.circle(-r, e)
    t.seth(270 - a)
    t.circle(-r, e)
    t.seth(270)
    t.fd(3*h/4)
    t.seth(270 + a)
    t.circle(r, e)
    t.seth(90)
    t.fd(3*h/4)
    t.rt(90)
    t.teleport(x, y-8)
    t.write(text, align="center", font = ("Arial", 8, "bold"))
    t.teleport(x+w/2, y)

def draw_agent(t=turtle.Turtle(), text="", x=0, y=0, w=100):
    r=w/2
    t.teleport(x, y-r)
    t.circle(r)
    t.teleport(x, y-8)
    t.write(text, align="center", font = ("Arial", 8, "bold"))
    t.teleport(x+r, y)

def draw_connector(t=turtle.Turtle(), ornament="", w=100):
    t.fd(w)
    if ornament == "arrow":
        t.stamp()

def draw_lock(t=turtle.Turtle(), text="", x=0, y=0, w=100, h=100):
    t.teleport(x-w/2, y+h/2)
    t.seth(0)
    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.rt(90)
    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.rt(90)
    t.teleport(x - w/6, y+h/2)
    t.seth(90)
    t.fd(h/4)
    t.circle(-w/6, 180)
    t.fd(h/4)
    t.teleport(x - w/3, y+h/2)
    t.seth(90)
    t.fd(h/4)
    t.circle(-w/3, 180)
    t.fd(h/4)
    text_size = int(3*w/10)
    t.teleport(x, y-text_size)
    t.write(text, align="center", font = ("Arial", text_size, "bold"))
    t.teleport(x+w/2, y)
    t.seth(0)

def draw_line(t:turtle.Turtle, els=[], key="", box=False, x=0, y=0, w=100, h=100):
    margin = int(0.25 * h)
    total_w = w * (len(els)*1.25 + 0.25)
    total_h = h + 2*margin

    current_x = x + margin
    
    if type(els) == tuple:
        key = els[1].strip()
        els = els[0]
    for i, el in enumerate(els):
        if type(el) == tuple:
            sub_w, sub_h = draw_line(t, el[0], el[1], True, current_x, y-margin, w, h)
            current_x += sub_w + margin
            total_h = sub_h + 2*margin
        else:
            print("Element", i + 1, el)
            draw_element(t, el, current_x, y, w, h)
            current_x += w + margin
    total_w = current_x - x

    t.teleport(x, y+h/2+margin)
    t.seth(0)
    t.fd(total_w)
    t.rt(90)
    t.fd(total_h)
    t.rt(90)
    t.fd(total_w)
    t.rt(90)
    t.fd(total_h)
    t.rt(90)

    if key:
        draw_lock(t, key, x+total_w+w//2, y+h//2, w//2, h//2)
    
    t.teleport(x+total_w, y)
    return (total_w, total_h)

class ProtocolError(Exception):
    def __init__(self, line, msg="Protocol must be in common syntax"):
        self.line = line
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.line} -> {self.msg}'

def draw_element(t:turtle.Turtle, el="", x=0, y=0, w=100, h=100):
    el = el.strip()
    if len(el) > 1:
        eltype = el[0]
        elorn = el[1:]
    else:
        eltype = el
    t.seth(0)
    match eltype:
        case "S":
            print("server", eltype, "X =", x)
            draw_server(t, text=eltype, x=x+w//2, y=y, w=w, h=h)
        case "I":
            print("interceptor", eltype, "X =", x)
            draw_interceptor(t, text=eltype, x=x+w//2, y=y, w=w, h=h)
        case "K":
            print("key", eltype, "X =", x)
            draw_key(t, text=elorn, x=x+w//2, y=y, w=w, h=h)
        case "N":
            print("nonce", "X =", x)
            draw_message(t, elorn, x=x+w//2, y=y, w=w, h=h)
        case "T":
            print("timestamp", "X =", x)
            draw_message(t, elorn, x=x+w//2, y=y, w=w, h=h)
            draw_clock(t, x+w//2, y, w, h)
        case eltype if eltype in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("agent", eltype, "X =", x)
            draw_agent(t, eltype, x=x+w//2, y=y, w=w)
        case _:
            raise ProtocolError(el)
    x = t.pos()[0].__round__()
    return x

def decrypt(payload):
    pattern = r".+?({(.+}.+)|[^{}]+?)(})(.+)"
    breakpoint = payload.find("{")
    print(payload, breakpoint)
    if breakpoint == -1:
        print("no encrypted")
        els = payload.split(",")
    elif breakpoint == 0:
        print("no unencrypted")
        match = re.findall(pattern, payload)[0]
        print("Match 1: ", match[0], "Match 2: ", match[1], "Match 3: ", match[2], "Match 4: ", match[3])
        els = tuple([decrypt(match[0]), match[3]])
    else:
        print("both kinds")
        match = re.findall(pattern, payload[:breakpoint])[0]
        els = payload[breakpoint:].split(", ")
        pair = tuple(decrypt(match[1]), match[2])
        els.append(pair)
    return els

def process(protocol, x=0, y=0, w=50, h=50):
    print(protocol)
    pattern = r" (\d+)\. +(\w) -> (\w) +: +(.+)"

    matches = re.findall(pattern, protocol)
    stages = []
    for m in matches:
        stages.append({
            'stage': m[0],
            'from': m[1],
            'to': m[2],
            'payload': decrypt(m[3]),
            })
        print(m)
    return stages

def draw_stages(lines, x, y, w, h):
    base_x = x
    base_y = y
    for j, line in enumerate(lines):
        print("Line", j + 1, line)
        sender = line["from"]
        receiver = line["to"]
        payload = line["payload"]
        draw_agent(t, sender, x=x+w/2, y=y, w=w)
        x += w
        draw_connector(t, "", w)
        x += w
        line_w = draw_line(t, payload, "", True, x, y, w, h)[0]
        x += line_w
        draw_connector(t, "arrow", w)
        x += w
        draw_agent(t, receiver, x=x+w/2, y=y, w=w)
        x = base_x
        y = base_y - (h*2) * (j+1)
        
if __name__ == '__main__':

    if testing:
        # assert (ans := process("A -> B"))["ans"] == [["A", "->", "B"]], ans
        # assert (ans := process("Ak - #n -> B", y=-100))["ans"] == [["Ak", "-", "#n", "->", "B"]]
        # assert (ans := process("Ak - #a -> Bk\nBk - #a - #b -> Ak\nAk - #b -> Bk", x=x, y=y, w=w, h=h))["ans"] == [["Ak", "-", "#a", "->", "Bk"], ["Bk", "-", "#a", "-", "#b", "->", "Ak"], ["Ak", "-", "#b", "->", "Bk"]]
        # assert (ans := process("A -> S  :   A, {Ta, B, Kab}Kas\nS -> B  :   {Ts, A, Kab}Kbs", x=x, y=y, w=w, h=h))["ans"] == [["A", "->", "S"], ["S", "->", "B"]]
        # assert (ans := process("I -> B", x=x, y=y-300, w=w, h=h))["ans"] == [["I", "->", "B"]], ans
        # draw_lock(t, "Lock", 200, 200, 100, 100)
        # draw_lock(t, "Lock", 200, 50, 75, 75)
        # draw_lock(t, "Lock", 200, -50, 50, 50)
        # draw_lock(t, "Lock", 200, -100, 25, 25)

        kerberos = '''
 1.   C -> A  :   U, G, L1, N1
 2.   A -> C  :   U, {U, C, G, Kcg, T1start, T1expire}Kag, {G, Kcg, T1start, T1expire}Ku
 3.   C -> G  :   S, L2, N2, {U, C, G, Kcg, T1start, T1expire}Kag, {C, T1}Kcg
 4.   G -> C  :   U, {U, C, S, Kcs, T2start, T2expire}Kgs, {S, Kcs, T2start, T2expire, N2}Kcg
 5.   C -> S  :   {U, C, S, Kcs, T2start, T2expire}Kgs, {C, T2}Kcs
 6.   S -> C  :   {T2}Kcs'''

        text = ''' 
        // Lowe's fixed version of Needham-Schroder Public Key 
        
        A,B,S :                     Principal     
        Na,Nb :                     Nonce         
        KPa,KPb,KPs,KSa,KSb,KSs :   Key           
        KPa,KSa :                   is a key pair 
        KPb,KSb :                   is a key pair 
        KPs,KSs :                   is a key pair 
        
        
        1.   A -> S  :   A,B            
        2.   S -> A  :   {KPb, B}KSs    
        3.   A -> B  :   {Na, A}KPb     
        4.   B -> S  :   B,A            
        5.   S -> B  :   {KPa, A}KSs    
        6.   B -> A  :   {Na, Nb, B}KPa 
        7.   A -> B  :   {Nb}KPb        
        
        // Security Protocols Open Repository 
        // http://www.lsv.ens-cachan.fr/spore 
        
        -----------------------------------------------------------------------
        
        
                    This document was translated from LaTeX by HeVeA
                    (http://pauillac.inria.fr/~maranget/hevea/index.html). 
        '''

        draw_stages(process(text), x, y, w, h)
        
        filepath = "C:/xampp/htdocs/cryptographics/output.ps"
        t.screen.save(filepath, overwrite=True)
        
        # fails with ghostscript not found on paths message???
        image = Image.open(filepath)
        image.save("drawing.png")

        # screenshot - this works but ugly resolution
        x0, y0 = -300, -300
        x1, y1 = 300, 300
        ImageGrab.grab().crop((x0, y0, x1, y1)).save("screenshot.png")

        draw_stages(process(kerberos), x, y, w, h)
        
    else:
        lines = []
        done = False
        while not done:
            line = input("Please enter the next line of the protocol, or enter a blank line to start drawing: ")
            if line:
                lines.append(line)
            else:
                done = True
        if lines:
            print(lines)
            process(lines, x=x, y=y, w=w, h=h)
            print("Protocol finished!")
        else:
            print("Empty protocol")
                
        

t.hideturtle()
turtle.update()
turtle.done()