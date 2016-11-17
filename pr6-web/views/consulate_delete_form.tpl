<!DOCTYPE html>
<html lang="es">
<head>
  <link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
  Specify ID of the consulate you want to delete:
  <form action="delete" method="post">
    <p>ID: <input name="id" type="number"/></p>
    <input value="Delete" type="submit"/>
  </form>
  <p><a href={{link}}>Go back to welcome page</p>
</body>
</html>
