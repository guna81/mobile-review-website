document.addEventListener('DOMContentLoaded', () => {

    // Change the color of the heading when dropdown changes
    document.querySelector('#varient').onchange = function() {
        document.querySelector('#price').innerHTML = this.value;
    };
    document.querySelector('#varient2').onchange = function() {
      document.querySelector('#price2').innerHTML = this.value;
    };

});