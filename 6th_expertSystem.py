def evaluate_employee():
    print("Welcome to the Employee Performance Evaluation System\n")

    try:
        punctuality = int(input("Rate punctuality (1-10): "))
        quality_of_work = int(input("Rate quality of work (1-10): "))
        teamwork = int(input("Rate teamwork (1-10): "))
        communication = int(input("Rate communication skills (1-10): "))
    except ValueError:
        print("Please enter valid integer values from 1 to 10.")
        return

    total_score = punctuality + quality_of_work + teamwork + communication
    average_score = total_score / 4

    print("\nEvaluation Result:")
    if average_score >= 8:
        print("Outstanding Employee")
    elif average_score >= 6:
        print("Good Performance")
    elif average_score >= 4:
        print("Needs Improvement")
    else:
        print("Unsatisfactory Performance")

# Run the expert system
evaluate_employee()
