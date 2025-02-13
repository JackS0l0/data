$('.headSlider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    arrows: false,
    dots: false,
    pauseOnHover: false,
    infinite: true,
    speed: 1000,
});
$('.projectBlock').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    arrows: false,
    dots: false,
    pauseOnHover: false,
    infinite: true,
    speed: 1000,
    responsive: [
        {
          breakpoint: 1001,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          }
        }
      ]
});