<!DOCTYPE html>
<html>
<head>
    <title>IntelliTest Signup</title>
    <link rel="stylesheet" type="text/css" href="signup.css">

</head>
<body>
    <div class="container">
        
        <div class="form-container">
            <h2>Begin your journey</h2>
            <form id="signupForm" method="post">
                <label for="fname">First name:</label><br>
                <input type="text" id="fname" name="fname"><br>
                <label for="lname">Last name:</label><br>
                <input type="text" id="lname" name="lname"><br>
                <label for="phone">Phone No:</label><br>
                <input type="tel" id="phone" name="phone"><br>
                <label for="email">Email:</label><br>
                <input type="email" id="email" name="email"><br>
                <label for="password">Password (Enter at least 8+ characters):</label><br>
                <input type="password" id="password" name="password"><br>
                <input type="checkbox" id="terms" name="terms">
                <label for="terms">By signing up, I agree with the <a href="http://localhost/tnc.php">Terms of Use & Privacy Policy</a></label><br>
                <input type="submit" value="Register">
            </form>
            <p>Returning user? <a href="http://localhost/signin.php">Log in here</a></p>
        </div>
        <div class="image-container">
        <img src="image.png" alt="Signup Image">        </div>
    </div>
</body>
</html>

<?php
if (isset($_SERVER["REQUEST_METHOD"]) && $_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $password = $_POST["password"];
    $fname = $_POST["fname"];
    $lname = $_POST["lname"];
    $phone = $_POST["phone"];

    $user = $email . "," . $password . "," . $fname . " " . $lname . "," . $phone . "\n";

    file_put_contents("users.txt", $user, FILE_APPEND);
}
?>
