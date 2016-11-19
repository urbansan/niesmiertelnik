$(document).ready(function() {
    $("#it_blog").on("click", function(){
            $.ajax({
                type: "GET",
                url: "/it_blog/",
                success: get_content
            });
        }
    );

    $("#moto").on("click", function(){
            $.ajax({
                type: "GET",
                url: "/moto/",
                success: get_content
            });
        }
    );

    $("#climbing").on("click", function(){
            $.ajax({
                type: "GET",
                url: "/climbing/",
                success: get_content
            });
        }
    );
    $("#guitar").on("click", function(){
            $.ajax({
                type: "GET",
                url: "/guitar/",
                success: get_content
            });
        }
    );

    function get_content(data, status){
        $("#currently_displayed").html(data);        
    }

});
