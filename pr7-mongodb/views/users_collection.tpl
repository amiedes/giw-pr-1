<!DOCTYPE html>
<html lang="es">
<head>
</head>
<body>
  <h1>Number of matching records: {{ matches }}</h1>
  <ul>
    % for user in users:
      <li>
        <ul><p>
          <li><strong>Id</strong>: {{ user.id }}</li>
          <li><strong>Email</strong>: {{ user.email }}</li>
          <li><strong>Webpage</strong>: {{ user.webpage }}</li>
          <li><strong>Credit card</strong>: {{ user.credit_card.number }}</li>
          <li><strong>Encrypted password</strong>: {{ user.password }}</li>
          <li><strong>Name</strong>: {{ user.name }}</li>
          <li><strong>Surname</strong>: {{ user.surname }}</li>
          <li><strong>Address</strong>: {{ user.address.pretty() }}</li>
          <li><strong>Likes</strong>:
            <ul>
              % for like in user.likes:
                <li>{{ like }}</li>
              % end
            </ul>
          </li>
          <li><strong>Birthdate</strong>: {{ user.birthdate }}</li>
        </p></ul>
      </li>
    % end
  </ul>
</body>
</html>
