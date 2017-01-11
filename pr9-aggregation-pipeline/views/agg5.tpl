<!DOCTYPE html>
<html lang="es">

% include("head.tpl")
% include("header.tpl")

<body>
  <div class="container">
    <table class="table table-stripped">
      <thead class="thead-inverse">
        <tr>
          <th>Country</th>
          <th>Total euro</th>
        </tr>
      </thead>
      <tbody>
        % for record in countries:
          <tr>
            <td>{{record['_id']}}</td>
            <td>{{record['total']}}</td>
          </tr>
        % end
      </tbody>
    </table>
    <p>Número de resultados: {{len(countries)}}</p>
  </div>
</body>

</html>
