<!DOCTYPE html>
<html>
<head>
    <title>Intellitest Sign In</title>
    <link rel="stylesheet" type="text/css" href="signin.css">

</head>
<body>
    <button id="signupButton" onclick="window.location.href='http://localhost/signup.php'">Signup</button>

    <h2>Intellitest</h2>
    <h3>Enter your details to Sign in to your account</h3>
    <form id="loginForm">
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br>
        <input type="submit" value="Continue">

    </form>
    <button onclick="forgotPassword()">Forgot Password</button>

    <script>
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault();
            var email = document.getElementById('email').value;
            var password = document.getElementById('password').value;
            fetch('users.txt')
                .then(response => response.text())
                .then(data => {
                    var users = data.split('\n');
                    for (var i = 0; i < users.length; i++) {
                        var user = users[i].split(',');
                        if (user[0] === email && user[1] === password) {
                            window.location.href = 'dashboard.html';
                            return;
                        }
                    }
                    alert('Incorrect password. Please try again.');
                });
        });

        function forgotPassword() {
            // Handle forgot password
        }
    </script>
</body>
</html>
