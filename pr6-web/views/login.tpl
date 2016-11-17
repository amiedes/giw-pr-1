<!DOCTYPE html>
<html lang="es">
<head>
    <link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
    <h1>Welcome!</h1>
    <h2>If you have an account enter your login and password</h2>
    <form action="login" method="post">
        <p>Login: <input name="username" type="text"/></p>
        <p>Password: <input name="password" type="text"/></p>
        <input value="Login" type="submit"/>
    </form>
    <hr>
    <h2>If you don't have an account register now!</h2>
    <form action="register" method="post">
        <p>Name: <input name="name" type="text"/></p>
        <p>Surname: <input name="surname" type="text"/></p>
        <p>Login: <input name="new_username" type="text"/></p>
        <p>Password: <input name="new_password" type="text"/></p>
        <input value="Create account" type="submit"/>
    </form>
</body>
</html>
