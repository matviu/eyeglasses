/*--promo-slider--*/
(function() {

  var btnPrev = document.querySelector('.promo-slider__btn_prev');
  var btnNext = document.querySelector('.promo-slider__btn_next');
  var slides = document.querySelectorAll('.promo-slider__slide');


  btnPrev.onclick = function(e) {
    showSlide(slideIndex += -1)
  }

  btnNext.onclick = function(e) {
    showSlide(slideIndex += 1);
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

/*--recomended slider--*/
(function() {

  var dots = document.querySelectorAll('.recomended__dot');
  var slides = document.querySelectorAll('.recomended__item');

  dots[0].onclick = function(event) {
    showSlide(1);
    changeDot(1);
  }

  dots[1].onclick = function(event) {
    showSlide(2);
    changeDot(2);
  }

  dots[2].onclick = function(event) {
    showSlide(3);
    changeDot(3);
  }

  var slideIndex = 1;
  showSlide(slideIndex);
  changeDot(slideIndex);

  function showSlide(slideIndex) {
    for (i = 0; i < slides.length; i++) {
      slides[i].style.opacity = '0';
    }
    slides[slideIndex-1].style.opacity = '1';
  }

  function changeDot(slideIndex) {
    for (i = 0; i < dots.length; i++) {
      dots[i].classList.remove('recomended__dot_active');
    }
    dots[slideIndex-1].classList.add('recomended__dot_active');
  }





})();
