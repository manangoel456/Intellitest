function signIn(event) {
    event.preventDefault(); // Prevent form submission

    // Get user input
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    // Check credentials
    var users = getUsers();
    var found = false;
    for (var i = 0; i < users.length; i++) {
        if (users[i].email === email && users[i].password === password) {
            found = true;
            break;
        }
    }

    if (found) {
        // Redirect to dashboard
        window.location.href = "dashboard.html";
    } else {
        // Show alert for incorrect credentials
        alert("Incorrect email or password. Please try again.");
    }
}

function getUsers() {
    // This function should ideally fetch users from the server-side or a database
    // For simplicity, we'll assume users are stored in a file named 'users.txt'
    var usersText = `user1@example.com,password1,User 1,1234567890
                      user2@example.com,password2,User 2,9876543210`;
    var usersArray = usersText.split("\n");
    var users = [];
    for (var i = 0; i < usersArray.length; i++) {
        var userData = usersArray[i].split(",");
        users.push({
            email: userData[0],
            password: userData[1],
            name: userData[2],
            phone: userData[3]
        });
    }
    return users;
}

function forgotPassword() {
    alert("Please contact support for password assistance.");
}
