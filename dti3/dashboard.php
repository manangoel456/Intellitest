
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Dashboard</title>
<style>
body {
font-family: Arial, sans-serif;
margin: 0;
padding: 0;
background: #f4f4f4;
}
.header {
background: #333366;
color: white;
padding: 10px 20px;
text-align: center;
}
.header h1 {
margin: 0;
}
.container {
width: 80%;
margin: 20px auto;
background: white;
padding: 20px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.user-info {
text-align: center;
margin-bottom: 20px;
}
.user-info .avatar {
background: #00bcd4;
border-radius: 50%;
width: 100px;
height: 100px;
line-height: 100px;
font-size: 50px;
color: white;
margin: 0 auto;
}
.user-info h2 {
margin: 10px 0;
}
.user-info .email, .user-info .phone {
margin: 5px 0;
font-size: 16px;
}
.button {
background: #00bcd4;
color: white;
border: none;
padding: 10px 20px;
text-align: center;
text-decoration: none;
display: inline-block;
margin: 10px 0;
cursor: pointer;
border-radius: 4px;
}
</style>
</head>
<body>

<div class="header">
<h1>Dashboard</h1>
</div>

<div class="container">
<div class="user-info">
<div class="avatar">A</div>
<h2><?php echo htmlspecialchars($_GET['name']); ?></h2>
<p class="email">Email id: <?php echo htmlspecialchars($_GET['email']); ?></p>
<p class="phone">Phone no. <?php echo htmlspecialchars($_GET['phno']); ?></p>
<button class="button" onclick="location.href='select_subject.html'">Attempt Mock Test</button>
</div>
</div>

</body>
</html>