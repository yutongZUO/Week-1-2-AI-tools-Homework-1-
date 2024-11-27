from flask import Flask, render_template

app = Flask(__name__)

answers = [
    {
        "question": "How do cloud platforms enable the storage and processing of large datasets required for real-world AI projects?",
        "answer": "Cloud platforms provide scalable storage systems and powerful computation resources (e.g., GPUs and TPUs) to handle large datasets efficiently."
    },
    {
        "question": "Why are web applications essential for providing user-friendly interfaces to deploy and interact with AI models?",
        "answer": "Web applications offer accessible and intuitive interfaces, allowing non-technical users to interact with AI models easily."
    },
    {
        "question": "How do cloud services support the scalability of AI projects when handling high volumes of real-time data?",
        "answer": "Cloud services provide auto-scaling and load-balancing features to manage fluctuating workloads and ensure consistent performance."
    },
    {
        "question": "How do web applications facilitate the integration of AI models into end-user environments for real-world applications?",
        "answer": "Web apps use APIs to integrate AI models seamlessly into existing workflows, making them accessible in familiar environments."
    },
    {
        "question": "How do cloud-based AI services simplify model training, deployment, and monitoring in real-world scenarios?",
        "answer": "They offer automated tools and pre-built frameworks to streamline processes like training, deployment, and performance monitoring."
    }
]

@app.route("/")
def index():
    return render_template("index.html", answers=answers)

if __name__ == "__main__":
    app.run(debug=True)
