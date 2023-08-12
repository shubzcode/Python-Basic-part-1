from flask import Flask, render_template

app = Flask(__name__)

# Sample data for blog posts
blog_posts = [
    {'title': 'Introduction to Flask', 'content': 'Flask is a micro web framework...'},
    {'title': 'Python Web Development', 'content': 'Python is widely used...'},
    # Add more posts here
]

@app.route('/')
def home():
    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)