import random

questions = [
    "Who was your most difficult customer?",
    "Tell me about a time when you didn't meet customer expectations. What happened, and how did you deal with the situation?",
    "How do you go about prioritizing customer needs when you are dealing with a large number of customers?",
    "Tell me about a time when you took on a task that was beyond your job responsibilities.",
    "Tell me about a time when you had to work on a task with unclear responsibilities.",
    "Tell me about a time when you showed an initiative to work on a challenging project.",
    "Describe a time when you found a simple solution to a complex problem.",
    "Tell me about a time when you invented something.",
    "Tell me about a time when you tried to simplify a process but failed. What would you have done differently?",
    "Tell me about a time when you effectively used your judgment to solve a problem.",
    "Tell me about a time when you had to work with insufficient information or incomplete data.",
    "Tell me about a time when you were wrong.",
    "Tell me about an important lesson you learned over the past year.",
    "Tell me about a situation or experience you went through that changed your way of thinking.",
    "Tell me about a time when you made a smarter decision with the help of your curiosity.",
    "Tell me about a time when you mentored someone.",
    "Tell me about a time when you made a bad hire. When did you figure it out, and what did you do?",
    "What qualities do you look for in potential candidates when making hiring decisions?",
    "Tell me about a time when you were dissatisfied with the quality of a project at work. What did you do to improve it?",
    "Tell me about a time when you motivated others to go above and beyond.",
    "Describe a situation when you couldn't meet your standards and expectations on a task.",
    "Tell me about your most significant professional achievement.",
    "Tell me about a time when you had to make a bold and challenging decision.",
    "Tell me about a time when your vision led to a great impact.",
    "Provide an example of when you took a calculated risk.",
    "Describe a situation when you took the initiative to correct a problem or a mistake rather than waiting for someone else to do it.",
    "Tell me about a time when you required some information from somebody else, but they weren't responsive. What did you do?",
    "Describe a time when you had to rely on yourself to complete a task.",
    "Tell me about a time when you had to be frugal.",
    "Tell me about a time when you had to rely on yourself to complete a project.",
    "Describe a time when you had to speak up in a difficult or uncomfortable environment.",
    "What would you do to gain the trust of your team?",
    "Tell me about a time when you had to tell a harsh truth to someone.",
    "Tell me about the most complicated problem you've had to deal with.",
    "Give me an example of when you utilized in-depth data to develop a solution.",
    "Tell me about something that you have learned in your role.",
    "Describe a time when you disagreed with the approach of a team member. What did you do?",
    "Give me an example of something you believe in that nobody else does.",
    "Tell me about an unpopular decision of yours.",
    "Describe the most challenging situation in your life and how you handled it.",
    "Give an example of a time when you had to handle a variety of assignments. What was the outcome?",
    "Tell me about a time when your team gave up on something, but you pushed them to deliver results.",
    "When was the last time you built a team? What did you consider when assembling it together?",
    "Give an example of a time when you developed the careers of people on your team.",
    "How have you managed varying strengths and weaknesses of members in your team?",
    "Describe a moral or ethical dilemma you've faced in the workplace. How did you handle it?",
    "Give an example of a time when you've left a project in a better position than you've found it.",
    "What's the largest impact you've had on your environment?"
]

leadership_principles = {
    "Customer Obsession": questions[:3],
    "Ownership": questions[3:6],
    "Invent and Simplify": questions[6:9],
    "Are Right, a Lot": questions[9:12],
    "Learn and Be Curious": questions[12:15],
    "Hire and Develop the Best": questions[15:18],
    "Insist on the Highest Standards": questions[18:21],
    "Think Big": questions[21:24],
    "Bias for Action": questions[24:27],
    "Frugality": questions[27:30],
    "Earn Trust": questions[30:33],
    "Dive Deep": questions[33:36],
    "Have Backbone; Disagree and Commit": questions[36:39],
    "Deliver Results": questions[39:42],
    "Strive to be Earth's Best Employer": questions[42:45],
    "Success and Scale Bring Broad Responsibility": questions[45:48]
}

def mock_interview():
    selected_question = random.choice(questions)
    print("Question: ", selected_question)

    guess_option = input("Do you want to guess the leadership principle? (yes/no): ").strip().lower()

    if guess_option == 'yes':
        user_guess = input("Guess the leadership principle: ").strip()

        for principle, associated_questions in leadership_principles.items():
            if selected_question in associated_questions:
                correct_principle = principle
                break
        else:
            correct_principle = "Unknown"

        if user_guess.lower() == correct_principle.lower():
            print("Correct! The question is associated with the '{}' leadership principle.".format(correct_principle))
        else:
            print("Incorrect. The correct leadership principle is '{}'.".format(correct_principle))

# Run the mock interview
mock_interview()
