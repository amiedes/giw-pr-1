<!DOCTYPE html>
<html lang="es">
<head>
<!--Import materialize.css-->
      
      <link type="text/css" rel="stylesheet" href="materialize.min.css"  media="screen,projection"/>

    <!--Let browser know website is optimized for mobile-->
       <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link href="http://fonts.googleapis.com/css?family=Inconsolata" rel="stylesheet" type="text/css">
        <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

   <!--Import jQuery before materialize.js-->
      <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
      <script type="text/javascript" src="materialize.min.js"></script>
</head>

<body>
<div class="row">
        <div class="col s12 m12  l12 ">
          <div class="card darken-1">
            <div class="card-content blue-grey darken-2 white-text">
              <span class="card-title"> ERROR </span><br/>
            </div>
                          
            <div class="card-content blue-grey darkenen-1 white-text">
               <span>{{ message }}</span>
            </div>           
          </div>
        </div>
      </div>
            
</body>
</html>
