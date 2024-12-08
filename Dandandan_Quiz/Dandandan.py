#Dandandan python quiz game

questions = ("What are the two main supernatural beliefs that the protagonists, Momo and Ken, have?: ",
             "What is the main premise of Dandadan?: ",
             "Which of the following best describes the tone of Dandadan?: ",
             "What is the primary setting of the series Dandadan?: ",
             "Which of the following genres best describes Dandadan?: ")

options = (("A) Ghosts and Demons", "B) Aliens and Ghosts", "C) Vampires and Werewolves", "D) Zombies and Magic"),
           ("A) A group of high school students get trapped in a haunted school.", "B) Two students are forced to fight demons in an underground tournament.", "C) Two high school students are caught up in a supernatural conflict involving aliens and ghosts.", "D) A cursed object causes a war between humans and spirits."),
           ("A) Dark and melancholic", "B) High-energy action mixed with comedy and quirky moments", "C) Slow-paced and philosophical", "D) Romance and drama-focused"),
           ("A) A mystical forest in the mountains", "B) A small, haunted town", "C) A high school and its surrounding areas", "D) An intergalactic spaceship"),
           ("A) Slice of life, comedy, and romance", "B) Supernatural, action, comedy, and fantasy", "C) Mystery, crime, and thriller", "D) Historical fiction and drama"))

answers = ("B", "C", "B", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input ("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else: 
        print('INCORRECT!')
        print(f"{answers[question_num]} is the correct answer!") 
    
    question_num += 1