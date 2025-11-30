# Agentic AI & LLM Learning Project

This project is a hands-on workspace designed to learn and experiment with **Agentic AI**, **Large Language Models (LLMs)**, **prompt engineering**, and **full-stack generative AI development**. It includes different prompting techniques, environment setup, and code samples for running AI models using OpenAI or other providers.

---

## 📁 Project Structure

```
GOOGLGENAI/
│
├── env/                     # Virtual environment (Python)
│
├── prompts/                 # Various prompting style demos
│   ├── cot.py               # Chain-of-Thought prompting
│   ├── few_shot_prom_structure.py
│   ├── few_shot_prom.py     # Few-shot prompting examples
│   ├── persona.py           # Persona-based prompting
│   ├── zero_prom.py         # Zero-shot prompting
│
├── .env                     # API keys and environment variables
├── .gitignore               # Git ignored files
├── app_with_openai.py       # App using OpenAI API
├── app.py                   # Core app logic
├── requirements.txt         # Python dependencies
```

---

## 🎯 Purpose of This Project

This project focuses on understanding and implementing:

### **1. Agentic AI Development**

* Building autonomous AI agents that can reason, execute tasks, and make decisions.
* Implementing memory, tools, and multi-step workflows.
* Using prompts to guide agent behavior.

### **2. LLM Fundamentals & Prompt Engineering**

* Zero-shot prompting
* Few-shot prompting
* Chain-of-thought prompting
* Persona prompting
* Structured prompting strategies

### **3. Generative AI Full-Stack Concepts**

* Using Python backends to interact with LLM APIs
* Designing prompt-driven applications
* API integration (OpenAI or Gemini)
* Environment variable management (`.env`)
* Building scalable and reusable AI modules

---

## 🚀 Features Covered in This Repo

* Building custom prompt templates
* Creating AI personas and behavior-bounded responses
* CoT (Chain-of-Thought) examples
* Few-shot learning prompts
* Zero-shot reasoning prompts
* Full app integration using OpenAI SDK

---

## 🧪 Running the Project

### **1. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **2. Add API Keys**

Create a `.env` file (already included in project structure):

```
OPENAI_API_KEY=your_api_key_here
```

### **3. Run the App**

```bash
python app.py
```

or

```bash
python app_with_openai.py
```

---

## 📚 Learning Goals

By completing this project, you will understand:

* How LLMs interpret prompts
* Techniques to improve output quality
* How to integrate LLMs into full-stack workflows
* How to structure prompts for agents and reasoning tasks

---

## 🧩 Future Enhancements

* Add vector database (FAISS / ChromaDB) for memory
* Create an agent with tool-calling capabilities
* Build a FastAPI or Flask backend for UI apps
* Add RAG (Retrieval-Augmented Generation)

---

## 🙌 Contribution

Feel free to fork this project, improve the examples, or add more prompting techniques.

---

## 📄 License

This project is for educational and learning purposes.
