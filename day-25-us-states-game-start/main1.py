import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('USA states game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

df = pd.read_csv('50_states.csv')
state = df.state.to_list()
guessed_state = []

while len(guessed_state) < 50:  
    answer_state = screen.textinput(title = f"{len(guessed_state)}/50 states correct", prompt = 'what is another states name? ').strip().title()
    print(answer_state)
    
    
    if answer_state == 'Exit':
        states_to_learn = [stat for stat  in state if stat not in guessed_state] 

        learn = pd.DataFrame({
        'state': states_to_learn
        })

        learn.to_csv('learn.csv')
        print(states_to_learn)
        
        break
    if answer_state in state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))


