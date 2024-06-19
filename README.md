# AI-Powered eCommerce Chatbot for WhatsApp

## Overview
This project introduces an innovative AI-powered eCommerce chatbot that integrates seamlessly with WhatsApp, leveraging Twilio's robust API. Designed to enhance the shopping experience, it enables customers to inquire about products, receive detailed information, and be directed to relevant purchasing pages through a simple and intuitive chat interface on WhatsApp.

## Features

### WhatsApp Integration
- **Twilio API**: Utilizes Twilio's API for seamless integration with WhatsApp, allowing the chatbot to send and receive messages efficiently.
- **User-Friendly Interface**: Offers a straightforward chat interface on WhatsApp, making it accessible and easy to use for customers.

### AI-Powered Responses
- **Advanced NLP**: Employs the Llama3-70b model running on the Groq inference engine, equipped with advanced natural language processing (NLP) and machine learning algorithms to understand user queries.
- **Contextual Relevance**: Provides accurate and contextually relevant responses, enhancing the user experience.

### Real-Time Product Information
- **Direct Database Access**: Capable of accessing the eCommerce database in real-time to fetch up-to-date product information, ensuring that users receive the latest details.
- **Accurate Responses**: Delivers precise information in response to customer inquiries about products.

### User Engagement
- **Reliable Messaging**: Ensures prompt and reliable message delivery through Twilio’s API, boosting user engagement and satisfaction.

## Getting Started

### Prerequisites
- Twilio Account
- Groq Account for AI model hosting
- Django environment for backend operations

### Installation
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your `.env` file with the necessary API keys and secrets (refer to the provided `.env` excerpt for guidance).
4. Run the Django server to start the chatbot.

### Configuration
Ensure your `.env` file is correctly set up with the following keys:
- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `GROQ_API_KEY`
- `OPENAI_API_KEY`
- Other relevant keys as per your project's requirements.

## Usage
Interact with the chatbot through WhatsApp by sending messages to the configured Twilio phone number. The AI agent will respond with product information, links to purchase pages, and more, based on your queries.

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or add new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
