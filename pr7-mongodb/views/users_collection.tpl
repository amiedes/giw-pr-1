<!DOCTYPE html>
<html lang="es">
<head>
</head>
<body>
  <h1>Number of matching records: {{ matches }}</h1>
  <table>
      <tr>
          <th><strong>Id</strong></th>
          <th><strong>Email</strong></th>
          <th><strong>Webpage</strong></th>
          <th><strong>Credit card</strong></th>
          <th><strong>Encrypted password</strong></th>
          <th><strong>Name</strong></th>
          <th><strong>Surname</strong></th>
          <th><strong>Address</strong></th>
          <th><strong>Likes</strong></th>
          <th><strong>Birthdate</strong></th>
      </tr>
      % for user in users:
        <tr>
            <td>{{user.id}}</td>
            <td>{{user.email}}</td>
            <td>{{ user.webpage }}</td>
            <td>{{ user.credit_card.number }}</td>
            <td>{{ user.password }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.surname }}</td>
            <td>{{ user.address.street }}</td>
            <td>
                % for like in user.likes:
                {{ like }}<br>
                % end
            </td>
            <td>{{user.birthdate}}</td>
        </tr>
      % end        
  </table>
  
  
</body>
</html>
