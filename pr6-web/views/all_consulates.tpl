<!DOCTYPE html>
<html lant="es">
<head></head>
<body>
  <h1>All consulates</h1>
  <ul>
    % for consulate in data:
      <li>{{consulate['name']}}</li>
    % end
  </ul>
</body>
</html>
