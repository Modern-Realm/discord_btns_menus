"""
Simple Response Button
"""

btn = SButton(label="Hello", response="Hello, Have a nice day !")
view_ = Button(author, btn).view()

"""
2 Simple Responsive Buttons 
"""

btn1 = SButton(label="Hello", response="Hello, Have a nice day !")
btn2 = SButton(label="Bye", response="Bye, see you later !")

view_ = DuoButton(author, btn1, btn2).view()

"""
3 Simple Responsive Buttons
"""

btn1 = SButton(label="username", response=f"{ctx.author} ")
btn2 = SButton(label="Bye", response="")
btn3 = SButton(label="Bye", response="")
