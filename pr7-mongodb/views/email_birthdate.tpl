<!DOCTYPE html>
<html lang="es">
<head>
</head>
% include("header.tpl", number=exercise)
<body>
  <div class="row">
        <div class="col s62 offset-s3 m62 offset-m3 l62 offset-l3">
          <div class="card darken-1">
            <div class="card-content blue-grey darken-2 white-text">
              <span class="card-title">Busqueda por {{title}}</span><br/>
              <span class="card-title">{{ matches }} Usuarios Encontrados</span>
            </div>
            
            <div class="card-content blue-grey darkenen-1 white-text">
              <table class=" bordered responsive-table">
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
            </div>
            
          </div>
        </div>
      </div>
</body>
</html>