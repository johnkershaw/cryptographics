import turtle
import math

t = turtle.Turtle()
turtle.tracer(0)
x = -300
y = 200
w = 75
h = w
r = h/2

testing = True

#TODO head and shoulders


def draw_clock(t, x, y, w, h):
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

def draw_key(t:turtle.Turtle, x:float, y:float, w:float, h:float):
    t.fillcolor("#D0D0D0")
    t.begin_fill()
    t.teleport(x+w/2, y-h*5/8)
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
    t.teleport(x+w/2, y-h/2)
    t.fillcolor("black")
    t.teleport(x+w/2, y)
    t.seth(0)

def draw(t=None, element="agent", ornament="", text="", x=0, y=0, w=100, h=100):
    if not t:
        t=turtle.Turtle()
    
    if element == "connection":
        t.forward(w)
        if ornament == "arrow":
            t.stamp()
    elif element == "agent":
        r=w/2
        t.teleport(x, y-r)
        t.circle(r)
        t.teleport(x, y-8)
        t.write(text, align="center", font = ("Arial", 8, "bold"))
        t.teleport(x+r, y)
    elif element == "server":
        r = math.sqrt(pow(w/2, 2) + pow(h, 2))
        a = math.degrees(math.atan(2*h/w))
        e = 180 - 2*a

        t.teleport(x-w/2, y+3*h/8)
        t.seth(90 - a)
        t.circle(-r, e)
        t.seth(270 - a)
        t.circle(-r, e)
        t.seth(270)
        t.forward(3*h/4)
        t.seth(270 + a)
        t.circle(r, e)
        t.seth(90)
        t.forward(3*h/4)
        t.right(90)
        t.teleport(x, y-8)
        t.write(text, align="center", font = ("Arial", 8, "bold"))
        t.teleport(x+w/2, y)
    elif element == "interceptor":
        long_side = math.sqrt(pow(w/2, 2) + pow(h, 2))
        short_side = math.sqrt(pow(w/2, 2) + pow(3*h/8, 2))
        a = math.degrees(math.asin(h/long_side))
        b = math.degrees(math.asin((3*h/8) / short_side))

        t.teleport(x-w/2, y-h/2)
        t.seth(a)
        t.forward(long_side)
        t.seth(360-a)
        t.forward(long_side)
        t.seth(180-b)
        t.forward(short_side)
        t.seth(180+b)
        t.forward(short_side)
        t.seth(0)
        t.teleport(x, y-8)
        t.write(text, align="center", font = ("Arial", 8, "bold"))
        t.teleport(x+w/2, y)
    elif element == "message":
        t.teleport(x-w/2, y+h/2)
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
        t.teleport(x, y-8)
        t.write(text, align="center", font = ("Arial", 8, "bold"))
        t.teleport(x+w/2, y)

    if ornament == "clock":
        draw_clock(t, x, y, w, h)
    elif ornament == "key":
        draw_key(t, x, y, w, h)

def draw_encrypted(t=None, elements=[], key="X", x=0, y=0, w=100, h=100):
    total_w = w * (len(elements)*1.25 + 0.25)
    t.teleport(x, y+h)
    t.forward(total_w)
    t.right(90)
    t.forward(2*h)
    t.right(90)
    t.forward(total_w)
    t.right(90)
    t.forward(2*h)
    t.right(90)
    t.teleport(x+w*0.25, y)
    current_x = x + w*0.25
    for el in elements:
        draw(t, el[0], el[1], el[2], current_x, y, w, h)
        current_x = current_x + w*1.25
    t.teleport(x+total_w/2, y-h)
    draw_key(t, x-w/2, y-h/2, w, h)
    t.teleport(x+total_w, y)

class ProtocolError(Exception):
    def __init__(self, line, msg="Protocol must be in common syntax"):
        self.line = line
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.line} -> {self.msg}'

def process(protocol, x=0, y=0, w=50, h=50):
    base_x = x
    base_y = y
    ans = []
    has_text = False
    print(protocol)
    if type(protocol) == str:
        lines = protocol.split("\n")
    else:
        lines = protocol
    for j, line in enumerate(lines):
        print("Line", j + 1, line)
        line_parts = line.split(":")
        stage = line_parts[0].strip()
        if len(line_parts) > 1:
            text = line_parts[1].strip()
            has_text = True
        els = stage.split(" ")
        print("There are ", len(els), "elements")
        for i, el in enumerate(els):
            print("Element", i + 1, el)
            eltype = el[0]
            if len(el) > 1:
                elorn = el[1:]
            else:
                elorn = ""
            match eltype:
                case "S" if elorn == "k":
                    print("server", eltype, "X =", x)
                    draw(t, element='server', ornament="key", text=eltype, x=x+w/2, y=y, w=w, h=h)
                case "S":
                    print("server", eltype, "X =", x)
                    draw(t, element='server', text=eltype, x=x+w/2, y=y, w=w, h=h)
                case "I" if elorn == "k":
                    print("interceptor", eltype, "X =", x)
                    draw(t, element='interceptor', ornament="key", text=eltype, x=x+w/2, y=y, w=w, h=h)
                case "I":
                    print("server", eltype, "X =", x)
                    draw(t, element='interceptor', text=eltype, x=x+w/2, y=y, w=w, h=h)
                case eltype if eltype in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and elorn == "k":
                    print("agent", eltype, "X =", x)
                    draw(t, element='agent', ornament="key", text=eltype, x=x+w/2, y=y, w=w, h=h)
                case eltype if eltype in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    print("agent", eltype, "X =", x)
                    draw(t, element='agent', text=eltype, x=x+w/2, y=y, w=w, h=h)
                case "-" if elorn == ">":
                    print("arrow", "X =", x)
                    draw(t, element='connection', ornament="arrow", w=w)
                case "-":
                    print("line", "X =", x)
                    draw(t, element='connection', w=w)
                case "#":
                    print("nonce", "X =", x)
                    draw(t, element='message', ornament="clock", text=elorn, x=x+w/2, y=y, w=w, h=h)
                case "m":
                    print("message", "X =", x)
                    draw(t, element='message', text=elorn, x=x+w/2, y=y, w=w, h=h)
                case _:
                    raise ProtocolError(line)
            x = t.pos()[0].__round__()
        if has_text:
            t.teleport((base_x+x)/2, y+10)
            text_size = 3*(w-10)//(len(text))
            t.write(text, align="center", font=("Consolas", text_size, "normal"))
        x = base_x
        y = base_y - (h*2) * (j+1)
        ans.append(els)
    return {"ans":ans, "x":x, "y":y}
        
if __name__ == '__main__':

    if testing:
        # assert (ans := process("A -> B"))["ans"] == [["A", "->", "B"]], ans
        # assert (ans := process("Ak - #n -> B", y=-100))["ans"] == [["Ak", "-", "#n", "->", "B"]]
        assert (ans := process("Ak - #a -> Bk\nBk - #a - #b -> Ak\nAk - #b -> Bk", x=x, y=y, w=w, h=h))["ans"] == [["Ak", "-", "#a", "->", "Bk"], ["Bk", "-", "#a", "-", "#b", "->", "Ak"], ["Ak", "-", "#b", "->", "Bk"]]
        # assert (ans := process("A -> S  :   A, {Ta, B, Kab}Kas\nS -> B  :   {Ts, A, Kab}Kbs", x=x, y=y, w=w, h=h))["ans"] == [["A", "->", "S"], ["S", "->", "B"]]
        # assert (ans := process("I -> B", x=x, y=y-300, w=w, h=h))["ans"] == [["I", "->", "B"]], ans
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