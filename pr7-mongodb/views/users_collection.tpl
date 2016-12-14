<!DOCTYPE html>
<html lang="es">
<head>
</head>
% include("header.tpl", number=exercise)
<body>
        
     <div class="row">
        <div class="col s62 m62 l62">
          <div class="card darken-1">
            <div class="card-content blue-grey darken-2 white-text">
              <span class="card-title">Busqueda por {{title}}</span><br/>
              <span class="card-title">{{ matches }} Usuarios Encontrados</span>
            </div>
            
            <div class="card-content blue-grey darkenen-1 white-text">
              <table class=" bordered responsive-table">
                <tr>
                    <th></th>
                    <th>User</th>
                    <th>Email</th>
                    <th>Web Page</th>
                    <th>Credit Card</th>
                    <th>Password</th>
                    <th>Name</th>
                    <th>Surname</th>
                    <th>Address</th>
                    <th>Likes</th>
                    <th>Birthdate</th>
                </tr>
                
                %i=0
                % for user in users:
                %i=i+1
                
                <tr>
                    <td> {{i}} </td>
                    <td>{{user.id}}</td>
                    <td>{{user.email}}</td>
                    <td>{{ user.webpage }}</td>
                    <td>
                    {{ user.credit_card.number }},
                    {{ user.credit_card.expire_month }}/
                    {{ user.credit_card.expire_year }}
                    </td>
                    <td>{{ user.password }}</td>
                    <td>{{ user.name }}</td>
                    <td>{{ user.surname }}</td>
                    <td>
                    {{ user.address.street }}
                    {{ user.address.num }},
                    {{ user.address.country }} 
                    ({{ user.address.zip }})
                    </td>
                    <td>
                        % for like in user.likes:
                            {{ like }}<br>
                        % end
                    </td>
                    <td>{{user.birthdate}}</td>
                </tr>
                %end
             </table>
            </div>
            
          </div>
        </div>
      </div>
            
</body>
</html>
