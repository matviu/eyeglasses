(function() {

  var btnPrev = document.querySelector('.promo-slider__btn_prev');
  var btnNext = document.querySelector('.promo-slider__btn_next');
  var slides = document.querySelectorAll('.promo-slider__slide');

  console.log(slides);

  btnPrev.onclick = function(e) {
    showSlide(slideIndex += -1)
    console.log(slideIndex);
  }

  btnNext.onclick = function(e) {
    showSlide(slideIndex += 1);
    console.log(slideIndex);
  }

  var slideIndex = 1;
  showSlide(slideIndex);

  function showSlide(n) {
    if(n < 1){slideIndex = slides.length};
    if(n > slides.length){slideIndex = 1};

    for (i = 0; i < slides.length; i++) {
      slides[i].style.opacity = '0';
    }
    slides[slideIndex-1].style.opacity = '1';


   };

})();
