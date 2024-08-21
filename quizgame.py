import pgzrun

WIDTH = 600
HEIGHT = 600
TITLE = "Quiz Game"
questions = []
time = 10
score  = 0
isgameover = False

skip = Rect(430,220,150,60)
timer = Rect(430,150,150,60)
welcomemessage = Rect(0,10,600,50)
questionbox = Rect(0,70,600,60)
answerbox1 = Rect(0,150,200,60)
answerbox2 = Rect(210,150,200,60)
answerbox3 = Rect(0,220,200,60)
answerbox4 = Rect(210,220,200,60)
answerboxes = [answerbox1,answerbox2,answerbox3,answerbox4]
def draw():
    screen.draw.filled_rect(welcomemessage,'sky blue')
    screen.draw.filled_rect(questionbox,'sky blue')
    screen.draw.filled_rect(skip,'skyblue')
    screen.draw.textbox('SKIP',skip,color = 'red',shadow= (0.5,0.5))
    screen.draw.filled_rect(timer,'skyblue')
    screen.draw.textbox(str(time),timer,color = 'yellow',shadow= (0.5,0.5))
    for i in answerboxes:
        screen.draw.filled_rect(i,'sky blue')
    screen.draw.textbox('Welcome to the cool quiz!', welcomemessage,color='white',shadow = (0.5,0.5),scolor = 'black')
    screen.draw.textbox(splitting[0],questionbox,color = 'white',shadow= (0.5,0.5))
    for i in range(4):
        screen.draw.textbox(splitting[i+1],answerboxes[i],color = 'white',shadow = (0.5,0.5),scolor = 'black')




def readyquestion():
    return questions.pop(0).split(',')
    


def qread():
    global questions
    question = open('questions.txt')
    for i in question:
        questions.append(i)
qread()
splitting = readyquestion()
print(splitting)
def on_mouse_down(pos):
    index = 1
    for i in answerboxes: 
        if i.collidepoint(pos):
            if index == int(splitting[5]):
                correct()
            else: 
                gameover()
        index = index+1
    if skip.collidepoint(pos):
        skipped()
      
def skipped():
    global splitting
    global time
    if isgameover == False:
        if questions:
            splitting= readyquestion()
            print(splitting)
            time = 10
        else:
            splitting = ["Congratulations! You scored: "+str(score),'-','-','-','-','-']
            time = 0
         

def correct():
    global splitting 
    global score
    global time
    score = score+1 
    if questions:
        splitting = readyquestion()
        time  = 10
        print(splitting)
    else:
        splitting = ["Congratulations! You scored: "+str(score),'-','-','-','-','-']
        time = 0

def gameover():
    global splitting
    global time
    global isgameover
    splitting = ["GAME OVER",'-','-','-','-','-']
    time = 0
    isgameover = True


def clockschedule():
    global time
    global splitting
    global score
    if questions:
        if time > 0:
            time = time-1
        else:

            splitting = ["GAME OVER",'-','-','-','-','-']
            time = 0
    else: 
        splitting = ["Congratulations! You scored: "+str(score),'-','-','-','-','-']


clock.schedule_interval(clockschedule,1)

    
   



pgzrun.go()
