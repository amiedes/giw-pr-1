<!DOCTYPE html>
<html lant="es">
<head></head>
<body>
  <h1>All consulates</h1>
  <ul>
    % for consulate in data:
      <li>
        --------------------
        <ul>
          <li>{{consulate['id']}}</li>
          <li>{{consulate['name']}}</li>
          <li>{{consulate['postal_code']}}</li>
          <li>{{consulate['neighborhood']}}</li>
          <li>{{consulate['district']}}</li>
          <li>{{consulate['latitude']}}</li>
          <li>{{consulate['longitude']}}</li>
        </ul>
        --------------------
      </li>
    % end
  </ul>
</body>
</html>
