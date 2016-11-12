<!DOCTYPE html>
<html lant="es">
<head>
  <link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
  <h1>Results were:</h1>
  <ul class="no-bullets">
    % for consulate in consulates:
      <li>
        <ul class="no-bullets">
          <li><strong>Id</strong>: {{consulate.id}}</li>
          <li><strong>Name</strong>: {{consulate.name}}</li>
          <li><strong>Postal code</strong>: {{consulate.postal_code}}</li>
          <li><strong>Neighborhood</strong>: {{consulate.neighborhood}}</li>
          <li><strong>District</strong>: {{consulate.district}}</li>
          <li><strong>Latitude</strong>: {{consulate.latitude}}</li>
          <li><strong>Longitude</strong>: {{consulate.longitude}}</li>
        </ul>
      </li>
      <p>----------------------------------</p>
    % end
  </ul>
</body>
</html>
