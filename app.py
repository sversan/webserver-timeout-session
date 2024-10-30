from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # HTML template with updated background color
    html_template = '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Deauthenticate User</title>
        <style>
          body {
            background-color: #FFDB58; /* Mustard color */
            color: green;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
          }
        </style>
      </head>
      <body>
        <h1>User Deauthentication</h1>
        <p>To deauthenticate a user, you can use the following code:</p>
        <pre>
# PHP
session_start();
session_destroy(); // Destroys the current session

# Node.js (Express)
req.session.destroy(err => {
    // Handle error if needed
});

# Apache
sudo htpasswd -D /path/to/.htpasswd username
        </pre>
      </body>
    </html>
    '''
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
