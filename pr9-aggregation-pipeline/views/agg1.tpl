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
          <th>Users</th>
        </tr>
      </thead>
      <tbody>
        % for record in top_countries:
          <tr>
            <td>{{record['_id']}}</td>
            <td>{{record['count']}}</td>
          </tr>
        % end
      </tbody>
    </table>
  </div>
</body>

</html>
