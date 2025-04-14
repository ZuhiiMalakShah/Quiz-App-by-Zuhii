import streamlit as st  # for the web interface
import random  # for randomizing the questions
import time  # for the timer

# Title of the Application
st.title("📝 Python Quiz Application")

# Define quiz questions, options, and answers in the form of a list of dictionaries
questions = [
    {"question": "What is the keyword used to define a function in Python?", "options": ["func", "define", "def", "function"], "answer": "def"},
    {"question": "Which of the following is a mutable data type in Python?", "options": ["Tuple", "String", "List", "Integer"], "answer": "List"},
    {"question": "What is the output of 3 * 3 ** 3?", "options": ["81", "27", "9", "None of the above"], "answer": "81"},
    {"question": "Which of these is used for single-line comments in Python?", "options": ["//", "#", "/* */", "--"], "answer": "#"},
    {"question": "Which function is used to get user input in Python?", "options": ["get()", "input()", "read()", "scan()"], "answer": "input()"},
    {"question": "What will be the output of type(5)?", "options": ["int", "float", "str", "None"], "answer": "int"},
    {"question": "Which of the following is NOT a Python data type?", "options": ["int", "float", "double", "list"], "answer": "double"},
    {"question": "How do you start a loop that iterates over a range of numbers?", "options": ["for i in range(5):", "for(i=0; i<5; i++)", "loop range(5):", "repeat 5"], "answer": "for i in range(5):"},
    {"question": "Which operator is used to check if two values are equal?", "options": ["=", "==", "!=", "equals"], "answer": "=="},
    {"question": "How do you create a list in Python?", "options": ["[]", "()", "{}", "<>"], "answer": "[]"},
    {"question": "Which function is used to find the length of a string in Python?", "options": ["size()", "count()", "length()", "len()"], "answer": "len()"},
    {"question": "What is the output of bool([])?", "options": ["True", "False", "Error", "None"], "answer": "False"},
    {"question": "Which method is used to remove the last element of a list?", "options": ["pop()", "delete()", "remove()", "discard()"], "answer": "pop()"},
    {"question": "Which keyword is used to handle exceptions in Python?", "options": ["catch", "error", "except", "try"], "answer": "try"},
    {"question": "What is the output of 10 // 3 in Python?", "options": ["3", "3.33", "3.0", "4"], "answer": "3"},
    {"question": "Which function is used to open a file in Python?", "options": ["open()", "read()", "file()", "load()"], "answer": "open()"},
    {"question": "What is the correct way to define a dictionary in Python?", "options": ["{key: value}", "[key: value]", "(key, value)", "<key=value>"], "answer": "{key: value}"},
    {"question": "Which of these is a valid Python variable name?", "options": ["1var", "_var", "var-name", "class"], "answer": "_var"},
    {"question": "Which built-in function can be used to sort a list in Python?", "options": ["order()", "sort()", "sorted()", "arrange()"], "answer": "sorted()"},
    {"question": "What is the result of 'Hello' + 'World'?", "options": ["HelloWorld", "Hello World", "Error", "Hello+World"], "answer": "HelloWorld"},
]

# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", question["options"], key="answer")

# Submit button to check the answer
if st.button("Submit Answer"):
    # Check if the answer is correct
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect! The correct answer is " + question["answer"])
    
    # Wait for 3 seconds before showing the next question
    time.sleep(5)
    
    # Select a new random question
    st.session_state.current_question = random.choice(questions)
    
    # Rerun the app to display the next question    
    st.rerun()

# Footer
st.markdown("---")
st.markdown("**Developed by Azra Talib**")
st.markdown("[GitHub Profile](https://github.com/Azratalib123)")
