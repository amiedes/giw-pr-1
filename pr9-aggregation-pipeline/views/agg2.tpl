<!DOCTYPE html>
<html lang="es">

% include("head.tpl")
% include("header.tpl")

<body>
  <div class="container">
    <table class="table table-stripped">
      <thead class="thead-inverse">
        <tr>
          <th>Product</th>
          <th>Total sales</th>
          <th>Unit price</th>
        </tr>
      </thead>
      <tbody>
        % for record in products_ranking:
          <tr>
            <td>{{record['nombre_producto']}}</td>
            <td>{{record['num_ventas']}}</td>
            <td>{{record['precio_unitario']}}</td>
          </tr>
        % end
      </tbody>
    </table>
    <p>Número de resultados: {{len(products_ranking)}}</p>
  </div>
</body>

</html>
