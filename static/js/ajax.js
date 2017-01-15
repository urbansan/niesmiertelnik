$(document).ready(function() {

    function get_content(data, status){
        $("#boczniaczek").html(data);
    }

    $.ajax({
        type: "GET",
        url: "/sidebar/",
        success: get_content
    });

    
    // $("#it_blog").attr("class", "active");

    // $("#it_blog").on("click", function(){
    //         $.ajax({
    //             type: "GET",
    //             url: "/it_blog/",
    //             success: get_content
    //         });
    //         $("#main_navbar li").attr("class", "");
    //         $(this).attr("class", "active");
    //     }
    // );

    // $("#moto").on("click", function(){
    //         $.ajax({
    //             type: "GET",
    //             url: "/moto/",
    //             success: get_content
    //         });
    //         $("#main_navbar li").attr("class", "");
    //         $(this).attr("class", "active");        }
    // );

    // $("#climbing").on("click", function(){
    //         $.ajax({
    //             type: "GET",
    //             url: "/climbing/",
    //             success: get_content
    //         });
    //         $("#main_navbar li").attr("class", "");
    //         $(this).attr("class", "active");
    //     }
    // );
    // $("#guitar").on("click", function(){
    //         $.ajax({
    //             type: "GET",
    //             url: "/guitar/",
    //             success: get_content
    //         });
    //         $("#main_navbar li").attr("class", "");
    //         $(this).attr("class", "active");
    //     }
    // );


});
