from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    job = request.form.get("job")
    skills = request.form.getlist("skills")
    experience = request.form.get("experience")

    questions = []

    if "SQL" in skills:
        questions.extend([
            {
                "question": "What is the difference between WHERE and HAVING in SQL?",
                "answer": "WHERE filters rows before grouping, while HAVING filters groups after GROUP BY.",
                "skill": "SQL"
            },
            {
                "question": "What are the different types of SQL JOINs?",
                "answer": "Common JOINs include INNER JOIN, LEFT JOIN, RIGHT JOIN and FULL OUTER JOIN.",
                "skill": "SQL"
            },
            {
                "question": "What is the use of GROUP BY in SQL?",
                "answer": "GROUP BY is used to group rows with the same values so aggregate functions can be applied.",
                "skill": "SQL"
            }
        ])

    if "Python" in skills:
        questions.extend([
            {
                "question": "What is Python and why is it useful for data analysis?",
                "answer": "Python is widely used for data analysis because of libraries such as Pandas and NumPy.",
                "skill": "Python"
            },
            {
                "question": "What is a list in Python?",
                "answer": "A list is an ordered and changeable collection that can store multiple values.",
                "skill": "Python"
            },
            {
                "question": "What is Pandas in Python?",
                "answer": "Pandas is a Python library used for data manipulation and analysis.",
                "skill": "Python"
            }
        ])

    if "Power BI" in skills:
        questions.extend([
            {
                "question": "What is Power BI?",
                "answer": "Power BI is a business intelligence tool used to analyze data and create interactive reports and dashboards.",
                "skill": "Power BI"
            },
            {
                "question": "What is Power Query?",
                "answer": "Power Query is used to connect, clean and transform data before analysis.",
                "skill": "Power BI"
            },
            {
                "question": "What is DAX in Power BI?",
                "answer": "DAX stands for Data Analysis Expressions and is used to create calculations in Power BI.",
                "skill": "Power BI"
            }
        ])

    if "Excel" in skills:
        questions.extend([
            {
                "question": "What is a Pivot Table in Excel?",
                "answer": "A Pivot Table is used to summarize and analyze large amounts of data.",
                "skill": "Excel"
            },
            {
                "question": "What is VLOOKUP used for?",
                "answer": "VLOOKUP is used to search for a value in a table and return a related value.",
                "skill": "Excel"
            },
            {
                "question": "What is conditional formatting in Excel?",
                "answer": "Conditional formatting changes the appearance of cells based on specified conditions.",
                "skill": "Excel"
            }
        ])

    if "Java" in skills:
        questions.extend([
            {
                "question": "What is Java?",
                "answer": "Java is an object-oriented programming language used to build applications.",
                "skill": "Java"
            },
            {
                "question": "What is a class in Java?",
                "answer": "A class is a blueprint used to create objects in Java.",
                "skill": "Java"
            },
            {
                "question": "What is inheritance in Java?",
                "answer": "Inheritance allows one class to acquire properties and methods of another class.",
                "skill": "Java"
            }
        ])

    if "HTML/CSS" in skills:
        questions.extend([
            {
                "question": "What is HTML?",
                "answer": "HTML is a markup language used to structure content on web pages.",
                "skill": "HTML/CSS"
            },
            {
                "question": "What is CSS?",
                "answer": "CSS is used to style and design HTML elements on a web page.",
                "skill": "HTML/CSS"
            },
            {
                "question": "What is the difference between HTML and CSS?",
                "answer": "HTML provides webpage structure, while CSS controls appearance and layout.",
                "skill": "HTML/CSS"
            }
        ])

    if not questions:
        questions.append({
            "question": "Please select at least one skill.",
            "answer": "Go back and select one or more skills.",
            "skill": "General"
        })

    return render_template(
        "questions.html",
        job=job,
        skills=skills,
        experience=experience,
        questions=questions
    )


@app.route("/mock-test", methods=["POST"])
def mock_test():

    job = request.form.get("job")
    skills = request.form.getlist("skills")
    experience = request.form.get("experience")

    return render_template(
        "mock_test.html",
        job=job,
        skills=skills,
        experience=experience
    )


@app.route("/result", methods=["POST"])
def result():

    correct_answers = {
        "q1": "A",
        "q2": "A",
        "q3": "A",
        "q4": "B",
        "q5": "A",
        "q6": "A",
        "q7": "B",
        "q8": "A",
        "q9": "A"
    }

    score = 0
    total = 0

    for question, correct_answer in correct_answers.items():

        if question in request.form:

            total += 1

            if request.form.get(question) == correct_answer:
                score += 1

    return render_template(
        "result.html",
        score=score,
        total=total
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)