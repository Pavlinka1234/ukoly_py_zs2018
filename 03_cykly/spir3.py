import turtle as t

n = 90
strana = 30
t.left(90)
for i in range(1, 300):
    t.forward(strana - i/10)  # pomalu zmensujeme stranu
    t.right(15)  # a kreslime "hodně"-uhelník

t.done()
