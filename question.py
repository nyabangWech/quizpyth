
from question import question
question prompts = [
#    "which country got its independence  1963?/n(a)kenya/southsudan(b)/uganda(c)/n/n"
#   "what color  are apples?/n(a)red/green(b)/purple(c)/n/n"
#    "what colors are mangoes ?/n(a)orange/(b)/brown-yellowish(c)/n/n"
]
questions =[
    question(question_prompts[0],"a"),
    question(question_prompts[1],"c"),
    question(question_prompts[2],"b"),
]
def run _test(questions):
         score=0
       for question in questions:
         answer =input(questio.prompt)
         if answer == question.answer:
             score +=1
             print("you got"+str(score)"|" +str(len(questions))+"correct")
             run_test(questions)
