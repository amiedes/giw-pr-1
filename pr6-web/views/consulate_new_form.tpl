<!DOCTYPE html>
<html lant="es">
<head>
  <link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
  Create a new consulate:
  <form action="new" method="post">
    <p>Name: <input name="name" type="text"/></p>
    <p>Postal code: <input name="postal_code" type="number"/></p>
    <p>Neighborhood: <input name="neighborhood" type="text"/></p>
    <p>District: <input name="district" type="text"/></p>
    <p>Latitude: <input name="latitude" type="number"/></p>
    <p>Longitude: <input name="longitude" type="number"/></p>
    <input value="Create" type="submit"/>
  </form>
</body>
</html>
