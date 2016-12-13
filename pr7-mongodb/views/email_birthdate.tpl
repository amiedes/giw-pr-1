<!DOCTYPE html>
<html lang="es">
<head>
</head>
<body>
	
  <h1>Find email birthdate</h1>
  <h1>Number of matching records: {{ matches }}</h1>
  <table>
      <tr>
          <th>id</th>
          <th>email</th>
          <th>fecha de nacimiento</th>
      </tr>
      % for user in users:
        <tr>
            <td>{{user.id}}</td>
            <td>{{user.email}}</td>
            <td>{{user.birthdate}}</td>
        </tr>
      % end        
  </table>
</body>
</html>