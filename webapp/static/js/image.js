  $(document).ready(function () {
        $('.popup-image').magnificPopup({
            type: 'image',
            image: {
                verticalFit: true,
                titleSrc: function (item) {
                    return item.el.attr('title');
                }
            },
            mainClass: 'mfp-img-mobile',
            maxWidth: 200,
            maxHeight: 200
        });
    });