# AI-Paper-Finder-API

An interactive web application built with Python and Streamlit. This tool connects to the **Semantic Scholar API** to search for academic papers, extracting key information like titles, authors, abstracts, and direct links to the full texts.

This is my first complete Python API project, built to practice API integrations, data handling, and web interfaces.

## Key Features

* **Real-Time Search:** Queries the Semantic Scholar database directly based on user input.
* **Clean User Interface:** Built entirely with Streamlit for a simple, responsive, and intuitive user experience.
* **Robust Error Handling:** Implements defensive programming (using the `.get()` method and conditional checks) to prevent crashes if the API reaches its limit or if some papers are missing data.
* **Efficient Data Processing:** Uses Python list comprehensions and JSON parsing to clean and format complex data structures on the fly.

## Tech Stack

* **Language:** Python 3
* **Web Framework:** Streamlit
* **HTTP Library:** Requests
* **Data Format:** JSON

## How to Run the Project Locally

If you want to test this project on your own machine, follow these steps in your terminal:

**1. Create a virtual environment**
This keeps the project dependencies isolated.
```bash
python3 -m venv .venv
```
**2. Activate the virtual environment**
For Linux/Mac/WSL:
```bash
source .venv/bin/activate
```
For Windows (Command Prompt):
```bash
.venv\Scripts\activate
```
**3. Install dependencies
```bash
pip install requests streamlit
```
**4. Run the application
```bash
streamlit run app.py
```

## Project Structure
ai-paper-finder/->
app.py               # Main application code (UI and API logic)
.venv/               # Virtual environment (ignored in git)
README.md            # Project documentation

## Learned skills
Building this project helped me understand how the web works behind the scenes. I learned how to build dynamic URLs with f-strings, how to make network requests, how to navigate complex JSON dictionaries, and why handling silent errors is crucial for a good user experience.
