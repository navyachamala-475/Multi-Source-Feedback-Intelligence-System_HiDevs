
def analyze_feedback(feedback):
    positive_words = ["good", "great", "excellent", "amazing", "nice", "love"]
    negative_words = ["bad", "worst", "poor", "hate", "terrible", "slow"]

    feedback = feedback.lower()

    if any(word in feedback for word in positive_words):
        return "Positive Feedback 😊"
    elif any(word in feedback for word in negative_words):
        return "Negative Feedback 😞"
    else:
        return "Neutral Feedback 😐"


def main():
    print("Welcome to Multi-Source Feedback Intelligence System")
    user_feedback = input("Enter your feedback: ")
    result = analyze_feedback(user_feedback)
    print("Analysis Result:", result)


if __name__ == "__main__":
    main()

    