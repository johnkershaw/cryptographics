import turtle
t = turtle.Turtle()
# turtle.tracer(0)
x = -200
y = 200
w = 100
h = w
r = h/2

testing = False

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
    t.teleport(x+w/2, y-h*3/4)
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
        t.forward(2*w)
        if ornament == "arrow":
            t.stamp()
    elif element == "agent":
        r=w/2
        t.teleport(x, y-r)
        t.circle(r)
        t.teleport(x, y-8)
        t.write(text, align="center", font = ("Arial", 8, "bold"))
        t.teleport(x+r, y)
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
    if type(protocol) == "String":
        lines = protocol.split("\n")
    else:
        lines = protocol
    for j, line in enumerate(lines):
        line_parts = line.split(":")
        stage = line_parts[0].strip()
        text = line_parts[1].strip()
        els = stage.split(" ")
        for i, el in enumerate(els):
            eltype = el[0]
            if len(el) > 1:
                elorn = el[1]
            else:
                elorn = ""
            match eltype:
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
                case "#" if elorn == "n":
                    print("nonce", "X =", x)
                    draw(t, element='message', ornament="clock", text="a", x=x+w/2, y=y, w=w, h=h)
                case "#":
                    print("message", "X =", x)
                    draw(t, element='message', text="a", x=x+w/2, y=y, w=w, h=h)
                case _:
                    raise ProtocolError(line)
            x = t.pos()[0]
        t.teleport((base_x+x)/2, y+10)
        text_size = 3*(w-10)//(len(text))
        t.write(text, align="center", font=("Consolas", text_size, "normal"))
        x = base_x
        y = base_y - (h*1.2) * (j+1)
        ans.append(els)
    return {"ans":ans, "x":x, "y":y}
        
if testing:
    # assert (ans := process("A -> B"))["ans"] == [["A", "->", "B"]], ans
    # assert (ans := process("Ak - #n -> B", y=-100))["ans"] == [["Ak", "-", "#n", "->", "B"]]
    # assert (ans := process("A -> B\nAk - #n -> B", y=-200))["ans"] == [["A", "->", "B"], ["Ak", "-", "#n", "->", "B"]]
    assert (ans := process("A -> S  :   A, {Ta, B, Kab}Kas\nS -> B  :   {Ts, A, Kab}Kbs", x=x, y=y, w=w, h=h))["ans"] == [["A", "->", "S"], ["S", "->", "B"]]
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
        print(Protocol finished!)
    else:
        print("Empty protocol")
            
    

t.hideturtle()
turtle.update()
turtle.done()