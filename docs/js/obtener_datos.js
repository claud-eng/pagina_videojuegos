$(document).ready(function () {
 
   $("#btn-obtener").click(function () {
   
       $("#btn-obtener").click(function () {
           $.get("https://mhw-db.com/monsters",
           function(data){
               //Sirve para recorrer los datos del json
               $.each(data, function(i, item){
                   var fila = "<tr><td>"+item.id+"</td><td>"+item.type +
                               "</td><td>"+item.name+
                               "</td><td>"+item.description+"</td></tr>"
                   
                   
                   $("#tabla-categorias").append(fila); 
                   
                   
               
               });
           });
     
       });


   });
   //   cierre del click 



});
 //   cierre del ready