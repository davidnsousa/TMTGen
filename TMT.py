from tkinter import *
import datetime
import time
import webbrowser


class subject:

	def __init__(self):
		self.info = Label(root, text="'Esc' to exit at any time")
		self.info.pack()
		self.frame = Frame(root, bd=2, relief=GROOVE)
		self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

		id_label = Label(self.frame, text="Id")
		id_label.grid(row=0, column=0, sticky=E)
		self.id = Entry(self.frame)
		self.id.insert(END, 'test')
		self.id.grid(row=0, column=1)

		gender_label = Label(self.frame, text="Gender")
		gender_label.grid(row=1, column=0, sticky=E)
		self.gender = Entry(self.frame)
		self.gender.insert(END, 'F')
		self.gender.grid(row=1, column=1)

		age_label = Label(self.frame, text="Age")
		age_label.grid(row=2, column=0, sticky=E)
		self.age = Entry(self.frame)
		self.age.insert(END, '20')
		self.age.grid(row=2, column=1)

		trail_label = Label(self.frame, text="Trail")
		trail_label.grid(row=3, column=0, sticky=E)
		self.trail = Entry(self.frame)
		self.trail.insert(END, 'default')
		self.trail.grid(row=3, column=1)

		condition_label = Label(self.frame, text="Condition")
		condition_label.grid(row=4, column=0, sticky=E)
		self.condition = Entry(self.frame)
		self.condition.insert(END, '0')
		self.condition.grid(row=4, column=1)

		submit_button = Button(self.frame, text="Submit")
		submit_button.bind('<ButtonPress-1>', self.submit)
		submit_button.grid(columnspan=2)
		submit_button.focus_set()

	def submit(self, event):
		global level, node_pos_i, trail_input
		level = 0
		node_pos_i = 0
		self.ID = self.id.get()
		self.GENDER = self.gender.get()
		self.AGE = self.age.get()
		self.CONDITION = self.condition.get()
		self.DATE = datetime.datetime.now().strftime("%Y-%m-%d")
		self.trail_input = self.trail.get()
		self.frame.destroy()
		self.info.destroy()
		with open(self.ID + ".csv","w") as F:
			F.write("Id,Gender,Age,Date,Trail,Condition,Level,Tag,Time,Correct\n")
		read_trail_input(self.trail_input)
		reset_canvas()
		message(messages[level])


class node:
	
	def __init__(self, x, y, tag):
		self.circle = canvas.create_oval(x, y, x+node_size, y+node_size, width=1, fill="white")
		self.content = canvas.create_text(x+node_size/2, y+node_size/2, fill="black", \
										  font="Times "+str(int(node_size*0.4)), text=tag)
		self.tag = tag
		canvas.tag_bind(self.circle, '<ButtonPress-1>', self.register)
		canvas.tag_bind(self.content, '<ButtonPress-1>', self.register)


	def register(self, event):
		global node_i
		expected_now = node_sequence[level][node_i]
		time_elapsed = time.time() - start_time
		
		if self.tag == expected_now:			
			x, y = event.x, event.y
			if canvas.old_coords:
				x1, y1 = canvas.old_coords
				canvas.create_line(x, y, x1, y1)
			canvas.old_coords = x, y
			with open(S.ID + ".csv","a") as F:
				F.write("%s,%s,%s,%s,%s,%s,%d,%s,%s,%d\n" % (S.ID, S.GENDER, S.AGE, S.DATE, S.trail_input, S.CONDITION, \
														 level, self.tag, time_elapsed, 1))
			node_i = node_i + 1
		else:
			with open(S.ID + ".csv","a") as F:
				F.write("%s,%s,%s,%s,%s,%s,%d,%s,%s,%d\n" % (S.ID, S.GENDER, S.AGE, S.DATE, S.trail_input, S.CONDITION, \
														 level, self.tag, time_elapsed, 0))
		if node_i == len(node_sequence[level]):
			next_level()
			

def close(event):
	root.destroy()

def read_trail_input(NAME):
	global container_size, node_size, node_sequence, messages, end_message, node_sequence_pos
	with open('cfg/'+NAME) as f:
		lines = f.read().splitlines()
		container_size = [int(lines[0]), int(lines[1])]
		node_size = int(lines[2])
		n_levels = int(lines[3])

		node_sequence = []
		for l in lines[4:4 + n_levels]:
			node_sequence.append(l.split(" "))

		messages = []
		for l in lines[4 + n_levels:4 + 2 * n_levels]:
			messages.append(l.replace('\\n', '\n'))

		end_message = lines[4 + 2 * n_levels].replace('\\n', '\n')
		
		node_sequence_pos = []
		for l in lines[4 + 2 * n_levels + 2:]:
			node_sequence_pos.append(list(map(int, l.split(" "))))


def place_container():
	midW = root.winfo_screenwidth()/2
	midH = root.winfo_screenheight()/2
	x0 = midW-container_size[0]/2
	y0 = midH-container_size[1]/2
	x1 = midW+container_size[0]/2
	y1 = midH+container_size[1]/2
	canvas.create_rectangle(x0, y0, x1, y1)


def place_nodes():
	global node_pos_i
	for tag in node_sequence[level]:
		x = node_sequence_pos[node_pos_i][0]
		y = node_sequence_pos[node_pos_i][1]
		node(x, y, tag)
		node_pos_i = node_pos_i + 1


def reset_canvas():
	global canvas
	canvas = Canvas(root)
	canvas.delete("all")
	canvas.config(background="white")
	canvas.focus_set()
	canvas.pack(fill='both', expand=True)

def message(msg):
        canvas.create_text(root.winfo_screenwidth()/2, root.winfo_screenheight()/2, fill="black", font="Times 16", \
					   justify=CENTER, text=msg)
        canvas.bind('<space>', start)

def start(event):
	global node_i, start_time
	canvas.unbind('<space>')
	canvas.delete("all")
	node_i = 0
	place_container()
	place_nodes()
	canvas.old_coords = None
	start_time = time.time()


def next_level():
	global level
	level = level + 1
	if level == len(node_sequence):
		canvas.destroy()
		reset_canvas()
		message(end_message)
		canvas.unbind('<space>')
		canvas.bind('<space>',leave_to_questionnaire)	
	else:
		canvas.destroy()
		reset_canvas()
		message(messages[level])
		

def leave_to_questionnaire(event):
	root.destroy()	

root = Tk()
root.title("TMT")
root.attributes('-fullscreen', True)

root.bind('<Escape>', close)

S = subject()

root.mainloop()
