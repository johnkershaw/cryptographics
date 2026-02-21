import turtle
t = turtle.Turtle()
# turtle.tracer(0)
x = -200
y = -200
w = 50
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

def process(protocol:str, x=0, y=0, w=50, h=50):
    base_x = x
    base_y = y
    ans = []
    lines = protocol.split("\n")
    for j, line in enumerate(lines):
        stage, text = line.strip().split(":")
        els = stage.strip().split(" ")
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
                    print("?")
            x = t.pos()[0]
        t.teleport((x-base_x)/2, y+10)
        t.write(text, align="center")
        x = base_x
        y = base_y - (h+10) * (j+1)
        ans.append(els)
    return {"ans":ans, "x":x, "y":y}
        
if testing:
    # assert (ans := process("A -> B"))["ans"] == [["A", "->", "B"]], ans
    # assert (ans := process("Ak - #n -> B", y=-100))["ans"] == [["Ak", "-", "#n", "->", "B"]]
    # assert (ans := process("A -> B\nAk - #n -> B", y=-200))["ans"] == [["A", "->", "B"], ["Ak", "-", "#n", "->", "B"]]
    assert (ans := process("A -> S:A, {Ta, B, Kab}Kas\nS -> B  :   {Ts, A, Kab}Kbs", y=-200))["ans"] == [["A", "->", "S"], ["S", "->", "B"]]


t.hideturtle()
turtle.update()
turtle.done()