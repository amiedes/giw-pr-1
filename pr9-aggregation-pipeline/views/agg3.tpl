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
          <th>Age range</th>
        </tr>
      </thead>
      <tbody>
        % for record in countries:
          <tr>
            <td>{{record['pais']}}</td>
            <td>{{record['rango_edades']}}</td>
          </tr>
        % end
      </tbody>
    </table>
    <p>Número de resultados: {{len(countries)}}</p>
  </div>
</body>

</html>
