import tkinter as tk
top = tk.Tk()
top.title('计算器')
shows = tk.Label(top, width=25,text='0',fg = 'white', bg = 'green')
shows.grid(row=0, columnspan=4)
zero = tk.Button(top, text = '0', width=5)
one = tk.Button(top, text='1', width=5)
two = tk.Button(top, text = '2', width=5)
three = tk.Button(top, text='3', width=5)
four = tk.Button(top, text = '4', width=5)
five = tk.Button(top, text='5', width=5)
six = tk.Button(top, text = '6', width=5)
seven = tk.Button(top, text='7', width=5)
eight = tk.Button(top, text = '8', width=5)
nine = tk.Button(top, text='9', width=5)
dot = tk.Button(top, text='.', width=5)
add = tk.Button(top, text = '+', width=5)
sub = tk.Button(top, text='-', width=5)
mul = tk.Button(top, text = '*', width=5)
div = tk.Button(top, text='/', width=5)
equal = tk.Button(top, text='=', width=5)
one.grid(row=1,column=0)
two.grid(row=1,column=1)
three.grid(row=1,column=2)
four.grid(row=2,column=0)
five.grid(row=2,column=1)
six.grid(row=2,column=2)
seven.grid(row=3,column=0)
eight.grid(row=3,column=1)
nine.grid(row=3,column=2)
zero.grid(row=4,column=0)
dot.grid(row=4,column=1)
add.grid(row=1,column=3)
sub.grid(row=2,column=3)
mul.grid(row=3,column=3)
div.grid(row=4,column=3)
equal.grid(row=4,column=2)

press_opt = False
def num_action(num):
    global press_opt
    if press_opt:
        shows['text'] = num
        press_opt = False
    else:
        shows['text'] = shows['text'] + num

def zero_click():
    num_action('0')
zero['command'] = zero_click
def one_click():
    num_action('1')
one['command'] = one_click
def two_click():
    num_action('2')
two['command'] = two_click
def three_click():
    num_action('3')
three['command'] = three_click
def four_click():
    num_action('4')
four['command'] = four_click
def five_click():
    num_action('5')
five['command'] = five_click
def six_click():
    num_action('6')
six['command'] = six_click
def seven_click():
    num_action('7')
seven['command'] = seven_click
def eight_click():
    num_action('8')
eight['command'] = eight_click
def nine_click():
    num_action('9')
nine['command'] = nine_click

has_dot = False
def dot_click():
    global has_dot
    if not has_dot:
        shows['text'] = shows['text'] + '.'
        has_dot = True
dot['command'] = dot_click
pre_opt = ''
pre_num = 0
def compute():
    global pre_opt
    global pre_num
    if pre_opt=='':
        return
    pre_num = float(pre_num)
    cur_num = float(shows['text'])
    if pre_opt == '+':
        new_number = pre_num + cur_num
    elif pre_opt == '-':
        new_number = pre_num - cur_num
    elif pre_opt == '*':
        new_number = pre_num * cur_num
    elif pre_opt == '/':
        new_number = pre_num / cur_num
    elif pre_opt == '=':
        new_number = cur_num
    shows['text'] = str(new_number)

def opt_click(cur_opt):
    global pre_opt
    global pre_num
    global press_opt
    global has_dot
    compute()
    pre_opt = cur_opt
    pre_num = shows['text' ]
    press_opt = True
    has_dot = False

def add_click():
    opt_click('+')
add['command'] = add_click
def sub_click():
    opt_click('-')
sub['command'] = sub_click
def mul_click():
    opt_click('*')
mul['command'] = mul_click
def div_click():
    opt_click('/')
div['command'] = div_click
def equal_click():
    opt_click('=')
equal['command'] = equal_click

top.mainloop()
