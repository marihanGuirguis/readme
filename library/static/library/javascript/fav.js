$("#fav").click(function () {
      console.log($(this).val() );
      value=$(this).val()
       $.ajax({
        url: 'ajax/favourite/',
          data: {
          'data': value
        },
        dataType: 'json',
        success: function (data) {
            //alert(data.add_fav);
              if($("#fav").text()=="unfavorite")
                $("#fav").text("favorite")
               else
                   $("#fav").text("unfavorite")
        }
      });

    });
$("#follow").click(function () {
      console.log( "Ok" );
      $.ajax({
        url: 'ajax/follow/',
           data: {
          'data': $(this).val()
        },
        success: function (data) {
            alert(data.add_fav);

        }
      });


    });


$(".stars input")

  $(".stars input").click(function () {
      no=$(this).next("label").text()
       $.ajax({
        url: 'ajax/rate/',
        data: {
          'data': no
        },
        dataType: 'json',
           success: function (data) {
            alert(data.add_fav);

        }

      });

    });

  $("#read").click(function () {
        console.log("clicked read")
       $.ajax({
        url: 'ajax/read/',
            data: {
          'data': $(this).val()
        },
           success: function (data) {
            //alert(data.add_fav);
            if($("#read").text()=="unread")
                $("#read").text("read")
               else
                   $("#read").text("unread")
        }

      });

    });

  $("#wishList").click(function () {
        console.log("clicked wishlist ")
       $.ajax({
        url: 'ajax/wishlist/',
            data: {
          'data': $(this).val()
        },
           success: function (data) {
           // alert(data.add_fav);
            if($("#wishList").text()=="unwish")
                $("#wishList").text("wish")
               else
                   $("#wishList").text("unwish")
        }

      });

    });

$("#categoryfollow").click(function () {
      console.log( "Ok" );
      $.ajax({
        url: 'ajax/Categoryfollow/',
           data: {
          'data': $(this).val()
        },
        success: function (data) {
            alert(data.add_fav);

        }
      });


    });

if ($(".stars").attr("rate")==1)
{
$("#star-1").attr('checked', 'checked');
}
else if($(".stars").attr("rate")==2)
{
$("#star-2").attr('checked', 'checked');
}
else if($(".stars").attr("rate") == 3)
{
     console.log("enter")
$("#star-3").attr('checked', 'checked');
}
else if($(".stars").attr("rate") == 4)
{
     console.log("enter")
$("#star-4").attr('checked', 'checked');
}
else if($(".stars").attr("rate") == 5)
{
    console.log("enter 5 stars")
$("#star-5").attr('checked', 'checked');
}

