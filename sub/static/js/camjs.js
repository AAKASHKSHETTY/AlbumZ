$('.post-wrapper').slick({
  infinite: true,
  slidesToShow: 7,
  slidesToScroll: 7,
  nextArrow: $('.next'),
  prevArrow: $('.prev'),
});

$('.post-wrapper2').slick({
  infinite: true,
  slidesToShow: 7,
  slidesToScroll: 7,
  nextArrow: $('.next2'),
  prevArrow: $('.prev2'),
});

function toggle() {
  var blur = document.getElementById('blur');
  blur.classList.toggle('active');
  var cont = document.getElementById('container');
  cont.classList.toggle('active');
}