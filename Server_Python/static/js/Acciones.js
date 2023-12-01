$(document).ready(function() {
    $("#boton").click(function(e){
        var nombre=$("#nombre").val();
        var correo=$("#correo").val();
        var tel=$("#tel").val();
        //alert("n: "+nombre+"; c: "+correo+"; t: "+tel);
        
        var resp_json
		var reqs=new XMLHttpRequest();// se crea una variable XMLHttpRequest para poder hacer peticiones GET, POST, PUT
		
        reqs.onreadystatechange=function(){
        	//alert(reqs.readyState)
        	//alert(reqs.status)
			//document.getElementById('imagen_espera').style.display='block'; //mostrar imagen de espera de proceso
			
            if (reqs.readyState == 4 && reqs.status== 200){
                resp_json=JSON.parse(reqs.responseText); // se recibe la respuesta del servidor python
                
		        alert(resp_json.Respuesta);
		                
		    }   // llega un String en formato JSON, por lo cual se hace un parse a JSON
        };
        reqs.open("GET","http://127.0.0.1:5000/"+ nombre+" "+correo+" "+tel,true); // se hace peticion GET. El parámetro true indica petición al servidor asíncrona. Es decir, continúa la ejecución de los elementos animados en la página mientras recibe respuesta del servidor
        //reqs.open("POST","http://127.0.0.1:5000/webhook",false); // se hace peticion GET
 
        reqs.send();
    });
});


