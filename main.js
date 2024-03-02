document.addEventListener('DOMContentLoaded', function() {
    const large = document.querySelector('.large');
    const smallImages = document.querySelectorAll('.small');
    
    smallImages.forEach(function(smallImage) {
        smallImage.addEventListener('click', function() {
            large.src = this.src;
        });
    });
});
