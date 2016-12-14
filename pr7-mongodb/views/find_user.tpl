<!DOCTYPE html>
<html lang="es">
<head>
</head>
% include("header.tpl", number=exercise)
<body>
<div class="row">
        <div class="col s12 m12  l12 ">
          <div class="card darken-1">
            <div class="card-content blue-grey darken-2 white-text">
              <span class="card-title">Busqueda por {{title}}</span><br/>
            </div>
            
            <div class="card-content blue-grey darkenen-1 white-text">
              <ul>
                %if user is not None:
                    <li><strong>Id</strong>: {{user.id}}</li>
                    <li><strong>Email</strong>: {{user.email}}</li>
                    <li><strong>Name</strong>: {{user.name}}</li>
                    <li><strong>Surname</strong>: {{user.surname}}</li>
                    <li><strong>Webpage</strong>: {{user.webpage}}</li>
                    <li><strong>Birthdate</strong>: {{user.birthdate}}</li>
                % else:
                    <li><strong> El usuario no existe</strong></li>
              </ul>
            </div>           
          </div>
        </div>
      </div>
            
</body>
</html>
