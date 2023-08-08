import time

# Sample data for user profiles (username: (password, score))
users = {
    'user1': ('password1', 0),
    'user2': ('password2', 0),
    # Add more users here
}

# Sample data for MCQ questions and options
mcq_questions = {
    1: {
        'question': 'What is the capital of France?',
        'options': ['New York', 'Paris', 'London', 'Berlin'],
        'correct_answer': 1,
    },
    2: {
        'question': 'Which planet is closest to the Sun?',
        'options': ['Venus', 'Mars', 'Mercury', 'Jupiter'],
        'correct_answer': 2,
    },
    # Add more questions here
}

# Function to log in
def login():
    print("Login:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username][0] == password:
        print("Login successful.")
        return username
    else:
        print("Invalid credentials.")
        return None

# Function to update profile (change password)
def update_profile(username):
    print(f"Update Profile for {username}:")
    new_password = input("Enter new password: ")
    users[username] = (new_password, users[username][1])
    print("Profile updated successfully.")

# Function to display questions and get user answers
def take_exam(username):
    print("Start the exam:")
    time_left = 60  # 60 seconds timer
    score = 0

    for question_id, question_data in mcq_questions.items():
        print(f"\nQuestion {question_id}: {question_data['question']}")
        for i, option in enumerate(question_data['options']):
            print(f"{i + 1}. {option}")

        start_time = time.time()
        user_answer = int(input("Enter your choice (1/2/3/4): "))

        if time.time() - start_time > time_left:
            print("\nTime's up! Submitting your answers...")
            break

        if user_answer == question_data['correct_answer']:
            score += 1

    users[username] = (users[username][0], score)
    print("Exam completed. Your score:", score)

# Main program
def main():
    print("Welcome to the Online Examination System!")
    username = login()
    if username is not None:
        while True:
            print("\nMenu:")
            print("1. Update Profile")
            print("2. Take Exam")
            print("3. Logout")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                update_profile(username)
            elif choice == '2':
                take_exam(username)
            elif choice == '3':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
