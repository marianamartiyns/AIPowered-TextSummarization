# 📝 AI Powered - Text Summarization

> Web application for text summarization using LangChain and DeepSeek, with an interactive interface in Streamlit.

## 📋 Description

This project allows automatic text summarization using the DeepSeek API integrated with the LangChain framework. The application features an interface developed in Streamlit, making it easy to input text and display the generated summaries.

## 🔧 Technologies Used

- [x] **Python**
- [x] **Streamlit** (for the web interface)
- [x] **LangChain** (for text manipulation and interaction with LLMs)
- [x] **DeepSeek API** (AI model used for generating summaries)
- [x] **Dotenv** (for managing environment variables)

## 🚀  How to Run the Project

1. Clone this repository:
   ```sh
   git clone https://github.com/marianamartiyns/AIPowered-TextSummarization.git
   cd AIPowered-TextSummarization
   ```
2. Create a virtual environment (optional, but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a .env file at the root of the project and add your DeepSeek API key:
   ```sh
   DEEPSEEK_API_KEY=sua_chave_aqui
   ```
5. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```
6. Access the application in your browser:
   - **http://localhost:8501**

## 🎨 Features

- Text input for summarization
- Summarization generation using LangChain and DeepSeek
- Interactive interface built with Streamlit

![App Demo](assets/demo.gif)

```py
# Author Info

# LinkedIn: https://www.linkedin.com/in/profile-mariana-martins/
# GitHub: https://github.com/marianamartiyns
# Email: marianamartiyns@gmail.com
```
> [!IMPORTANT] 
> This project is for educational and experimental purposes only. Using the DeepSeek API may be subject to limits and costs.
