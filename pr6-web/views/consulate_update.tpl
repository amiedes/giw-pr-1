<!DOCTYPE html>
<html lang="es">
<head>
  <link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
  Specify id of consulate you want to modify:
  <form action="modify" method="post">
        Id: <input name="id" type="text"/>
        <hr>

        Specify data you want to modify:
        <p>Name: <input name="name" type="text"/></p>
        <p>Postal code: <input name="postal_code" type="number"/></p>
        <p>Neighborhood: <input name="neighborhood" type="text"/></p>
        <p>District: <input name="district" type="text"/></p>
        <p>Latitude: <input name="latitude" type="number"/></p>
        <p>Longitude: <input name="longitude" type="number"/></p>
        <input value="Modify" type="submit"/>
  </form>
</body>
</html>
