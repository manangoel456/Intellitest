<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Forgot Password</title>
<style>
body {
font-family: Arial, sans-serif;
margin: 20px;
}
.container {
max-width: 400px;
margin: 0 auto;
padding: 20px;
border: 1px solid #ccc;
border-radius: 5px;
}
.form-group {
margin-bottom: 15px;
}
.form-group label {
display: block;
margin-bottom: 5px;
}
.form-group input[type="email"] {
width: 100%;
padding: 10px;
border: 1px solid #ccc;
border-radius: 4px;
}
.form-group input[type="submit"] {
background-color: #333366;
color: #fff;
padding: 10px 15px;
border: none;
border-radius: 4px;
cursor: pointer;
}
.form-group input[type="submit"]:hover {
background-color: #555;
}
</style>
</head>
<body>

<div class="container">
<h2>Forgot Password</h2>
<p>Please enter your email address below to reset your password.</p>

<form action="reset_password.php" method="post">
<div class="form-group">
<label for="email">Email:</label>
<input type="email" id="email" name="email" required>
</div>
<div class="form-group">
<input type="submit" value="Reset Password">
</div>
</form>
</div>

</body>
</html>