


$(document).ready(function(){
    
    $("#runBtn").click(function(e) {

        e.preventDefault();

        $.ajax({
            url: "http://127.0.0.1:5000/prediction/" + $("#idCity").val()+"/"+$("#idArea").val(),
            dataType: 'json',
            type: 'GET',
            contentType: 'application/json',
            success : function(data){
               console.log(data)
               $(".res").html("")
               $(".res").html("We advise you to sell your parking space for "+data.data+ " euros")
            }
          });
        

    })

 $("#updateBtn").click(function(e) {

        e.preventDefault();

        $.ajax({
            url: "http://127.0.0.1:5000/cities",
            dataType: 'json',
            type: 'GET',
            contentType: 'application/json',
            success : function(data){
               var cities = data.data
               $('#idCity').html("")
               cities.forEach(function(element){
                $('#idCity').append("<option>"+element+"</option>")
               })
            }
          });
        
        

    })

    
});




/*







    
    $.ajax({
        url: "http://127.0.0.1:5000/cities"
        dataType: 'json',
        type: 'GET',
        contentType: 'application/json',
        success : function(data){
           console.log(data)
        }
      });


<select class="form-control" id="idCity">
                                    <div id="optionCity">
                                    </div>
                                </select>



*/