// 回到顶部按钮
$(window).scroll(function () {
    $('#backtop').hide();
    if ($(window).scrollTop()>=600) {
        $('#backtop').show();
    };
});
$('#backtop').click(function () {
    var speed=400;
    $('body,html').animate({scrollTop:0}, speed);
    return false;
})