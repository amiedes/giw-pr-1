<!DOCTYPE html>
<html lant="es">
<head></head>
<body>
  <h1>Results were:</h1>
  <ol>
    % for consulate in consulates:
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
  </ol>
</body>
</html>
