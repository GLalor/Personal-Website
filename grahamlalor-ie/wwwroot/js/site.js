// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your Javascript code.


$(document).ready(function () {
    $(document).on('click', '.showMore', function () {
        $('.showMore').text("Show less");
        $('.showMore').attr('class', 'showLess btn btn-info');
        $('.skills').animate({ height: '1100px' }, "slow");
    });

    $(document).on('click', '.showLess', function () {
        //$('.moreSkills').css("visibility", "hidden");
        $('.showLess').text("Show more");
        $('.showLess').attr('class', 'showMore btn btn-info');
        $('.skills').animate({ height: '380px' }, "slow");
    });


    // $("#sendEmail").click(function () {
    //     $('#contactModal').modal('toggle');
    //     $('#light').delay(2500).queue(function (next) {$(this).css('display','none'); next();});
    //     $('#fade').delay(2500).queue(function (next) { $(this).css('display','none'); next();});
    // });

    $(".anchor").click(function (e) {
        e.preventDefault();
        anchor = $(this).attr('href');
        $("html, body").animate({
            'scrollTop': $(anchor).offset().top
        }, 1000);
    });

    $(".navbar-nav li").on("click", function () {
        $(".navbar-nav").find(".active").removeClass("active");
        $(this).parent().addClass("active");
    });

    $("tr[id=popover]").popover({ placement: "top", trigger: "hover" });
});