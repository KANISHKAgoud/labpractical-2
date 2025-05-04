def chatbot():
    print("Welcome to ShopEasy Customer Support!")
    print("Type 'exit' anytime to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if 'exit' in user_input:
            print("Thank you for contacting ShopEasy. Have a great day!")
            break

        elif 'order' in user_input:
            print("You can track your order at: www.shopeasy.com/track")

        elif 'return' in user_input or 'refund' in user_input:
            print("To return a product, go to 'My Orders' and click on 'Return'. Refunds are processed within 3-5 days.")

        elif 'cancel' in user_input:
            print("To cancel an order, visit 'My Orders' and click 'Cancel' next to the item.")

        elif 'contact' in user_input or 'help' in user_input:
            print("You can call us at 1800-123-456 or email support@shopeasy.com")

        elif 'payment' in user_input:
            print("We accept credit/debit cards, UPI, and COD (Cash on Delivery).")

        else:
            print("I'm sorry, I didn't understand that. Could you please rephrase your question?")

# Run the chatbot
chatbot()
