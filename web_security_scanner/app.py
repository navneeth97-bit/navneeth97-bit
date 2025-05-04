from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Used to encrypt session data

# Dummy User Data (Replace with actual database later if needed)
users = {
    "Navneeth@gmail.com": "Dummy123",
    "Navneeth@gmail.com": "Dummy123"
}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Check if credentials match
        if email in users and users[email] == password:
            session["user"] = email  # Store user in session
            return redirect(url_for("home"))  # Redirect to scanner
        else:
            return render_template("login.html", error="Invalid Email or Password")
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)  # Remove user session
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect(url_for("login"))  # Redirect if not logged in
    
    scan_results = None
    if request.method == "POST":
        url = request.form.get("url")
        scan_results = {
            "sql_injection": "failed",
            "sql_injection_status": "Vulnerable to SQL Injection!",
            "xss": "passed",
            "xss_status": "No XSS vulnerabilities detected.",
            "csrf": "failed",
            "csrf_status": "Vulnerable to CSRF attacks!"
        }
        return render_template("index.html", scan_results=scan_results)
    
    return render_template("index.html", scan_results=scan_results)

if __name__ == "__main__":
    app.run(debug=True)
