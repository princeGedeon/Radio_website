Fancybox.bind('[data-fancybox="gallery"]', {
  groupAll : true,
  animated: true,
  showClass: fancybox-fadeIn,
  hideClass: false,
   caption: function (fancybox, carousel, slide) {
    return (
      `${slide.index + 1} / ${carousel.slides.length} <br />` + slide.caption
    );
  },
  Image: {
    Panzoom: {
      zoomFriction: 0.7,
      maxScale: function () {
        return 5;
      },
    },
  },
  Thumbs: {
    Carousel: {
      Sync: {
        friction: 0.9,
      },
    },
  },

  click: false,

  dragToClose: true,

  Toolbar: {
    display: [{ id: "counter", position: "center" },
       "close"],
  },
})