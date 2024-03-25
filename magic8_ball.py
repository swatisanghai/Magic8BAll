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

    # Choose one response from each category
    affirmation_response = random.choice(affirmation_responses)  # Randomly select an affirmation response
    non_committal_response = random.choice(non_committal_responses)  # Randomly select a non-committal response
    negative_response = random.choice(negative_responses)  # Randomly select a negative response

    # Print the chosen responses
    print(affirmation_response)  # Print the randomly selected affirmation response
    print(non_committal_response)  # Print the randomly selected non-committal response
    print(negative_response)  # Print the randomly selected negative response

    # Repeat the process two more times to fulfill the requirement of 3 responses from each category
    for _ in range(2):
        affirmation_response = random.choice(affirmation_responses)  # Randomly select another affirmation response
        non_committal_response = random.choice(non_committal_responses)  # Randomly select another non-committal response
        negative_response = random.choice(negative_responses)  # Randomly select another negative response

        print(affirmation_response)  # Print the randomly selected affirmation response
        print(non_committal_response)  # Print the randomly selected non-committal response
        print(negative_response)  # Print the randomly selected negative response

# Main function
def main():
    print("Welcome to the Magic 8 Ball!")  # Print a welcome message
    question = input("Ask me a yes/no question: ")  # Prompt the user to ask a question
    magic_8_ball()  # Call the magic_8_ball function to generate responses

if __name__ == "__main__":  # Check if the script is executed as the main program
    main()  # Call the main function to start the program
