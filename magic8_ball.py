# Import the random module to generate random responses
import random  # Import the random module to generate random responses

def magic_8_ball():
    # Possible responses sagrigated into affirmation, non-committal, and negative
    affirmation_responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes."
    ]
    non_committal_responses = [
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again."
    ]
    negative_responses = [
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

  # Randomly choose one response from all categories
    all_responses = affirmation_responses + non_committal_responses + negative_responses
    chosen_response = random.choice(all_responses)  # Randomly select a response

    # Print the chosen response
    print(chosen_response)  # Print the randomly selected response

# Main function
def main():
    print("Welcome to the Magic 8 Ball!")  # Print a welcome message
    question = input("Ask me a yes/no question: ")  # Prompt the user to ask a question
    magic_8_ball()  # Call the magic_8_ball function to generate a response

if __name__ == "__main__":  # Check if the script is executed as the main program
    main()  # Call the main function to start the program
