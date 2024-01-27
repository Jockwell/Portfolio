# Here are some predefined questions and answers
questions = [
    "where is the fees office",
    "who can help me with my curriculum form",
    "where can i find out for about student accommodation",
    "what clubs do the unversity offer",
    "which courses should i take",
    "who is my student mentor"
]

answers = [
    "The fees office is located in the blue building on Camp Lane.",
    "You can speak to your course advisor.",
    "The SRC can help with that",
    "The university offers a wide range of clubs.",
    "You can talk to your orientation leader or course advisor about this.",
    "You can find out who your student mentor is by reporting to room 14."
]

# UniBuddy introduces itself.
print('''
        Hi! My name is unibuddy and I am here to help you through your university journey!
        I'm going to ask you a few questions to get to know you a little better.
      ''')

# Asks for the user's name.
user_name = input("What's your name? : ")
print(f"Hi {user_name}!")

# Asks the user to input there age and outputs a specfic anwser.
user_age = int(input('''How old are you? : '''))
if user_age < 18:
    print('''Wow! You're are stating university at a really young age!
You must be really talented!''')
elif 25 < user_age < 35:
    print('''Hmm, you're much older than I expected!''')
elif user_age > 35 :
    print('''That's amazing, It's never too late to learn and grow!''')
else:
    print(f'''{user_age} is a fun age to start university at!
I started university when I was 18 years old.''')

# Continously prompt the user for questions.
while True:
    user_question = input("Do you have a question to ask (say 'bye' to exit)? :")
    user_question = user_question.strip("?")
    user_question = user_question.lower()

    if user_question in questions:
        question_num = questions.index(user_question)
        print(answers[question_num])
        continue
    if user_question == "bye":
        print("Thank you for chatting with me! I hope the rest of your uni journey goes well!")
        break
    else:
        print("I don't understand your response. Please try again.")
        continue
