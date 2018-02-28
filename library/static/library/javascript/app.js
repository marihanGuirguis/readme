
$("#categories").click(function () {

    $.ajax({

        url:'http://localhost:8000/library/templates/ajax/getcategory/',
        type:'GET',

        beforeSend:function () {
        },

        success:function (data) {
            $("#categories").empty();
            var ele = "<option selected disabled>Categories</option>";
            $("#categories").append(ele)
            $.each(data,function (index,item) {
                //alert(JSON.stringify(item["fields"]["type"]))
                var val = JSON.stringify(item["fields"]["type"]) ;
                var val2 = val.replace('\"','');
                var val3 = val2.replace('\"','');
                var ele = "<option value="+val+">"+val3+"</option>";
                $("#categories").append(ele)


            })
        },

        error:function () {
            alert("Some Error")
        }

    });
});


$("#authers").click(function () {

    $.ajax({

        url:'http://localhost:8000/library/templates/ajax/get_author/',
        type:'GET',

        beforeSend:function () {
        },

        success:function (data) {
            $("#authers").empty();
            var ele = "<option selected disabled>Your favourite authers</option>";
            $("#authers").append(ele)
            $.each(data,function (index,item) {
                //alert(JSON.stringify(item["fields"]["type"]))
                var val = JSON.stringify(item["fields"]["name"]) ;
                var val2 = val.replace('\"','');
                var val3 = val2.replace('\"','');
                var ele = "<option value="+val+">"+val3+"</option>";
                $("#authers").append(ele)


            })
        },

        error:function () {
            alert("Some Error")
        }

    });
});


$("#books_list").click(function () {

    $.ajax({

        url:'http://localhost:8000/library/templates/ajax/get_book/',
        type:'GET',

        beforeSend:function () {
        },

        success:function (data) {
            $("#books_list").empty();
            var ele = "<option selected disabled>Your favourite Books</option>";
            $("#books_list").append(ele)
            $.each(data,function (index,item) {
                //alert(JSON.stringify(item["fields"]["type"]))
                var val = JSON.stringify(item["fields"]["name"]) ;
                var val2 = val.replace('\"','');
                var val3 = val2.replace('\"','');
                var ele = "<option value="+val+">"+val3+"</option>";
                $("#books_list").append(ele)


            })
        },

        error:function () {
            alert("Some Error")
        }

    });
});


$("#categories").change(function (e) {
    if($('#categories option:selected').val()!="Categories") {
        var type = $('#categories option:selected').val();
        $(location).attr('href', "/library/" + type);
    }
});



$("#authers").change(function () {
    if($('#authers option:selected').val()!="Your favourite authers") {
        var author = $('#authers option:selected').val();
        $(location).attr('href', "/library/authers/" + author);
    }
});

$("#books_list").change(function () {
    if($('#books_list option:selected').val()!="Your favourite Books") {
        var book = $('#books_list option:selected').val();
        $(location).attr('href', "/library/books/"+book);
    }
});



$('.carousel').carousel({
  interval: 100
});

$("#getAllAuthors").click(function (e) {


     e.preventDefault();
     $(location).attr('href', "/library/allAuthors")

});

$("#submitSearch").click(function (event) {

    event.preventDefault();

    if($("#textSearch").val()!="") {
        var text = $("#textSearch").val();

        $(location).attr('href', "/library/search/" + text);
    }
    else
    {
        alert("What are you searching about!!!")
    }
});

function updateBtn () {

    // var username = $("#newUserName").val();
    //
    // var Password = $("#newPassword").val();
    //
    // var email = $("#newEmail").val();


    $(location).attr('href', "/library/updateUser");

};

