document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('resultadoModal')) {
        var myModal = new bootstrap.Modal(document.getElementById('resultadoModal'));
        myModal.show();
    }

    var copyButton = document.getElementById('copyButton');
    if (copyButton) {
        copyButton.addEventListener('click', function() {
            var resultadoInput = document.getElementById('resultadoInput');
            resultadoInput.select();
            document.execCommand('copy');
        });
    }
});