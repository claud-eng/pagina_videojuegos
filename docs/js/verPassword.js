jQuery(document).ready(function () {
    $("#showpassword").on('click', function () {

        var pass = $("#id_txtContrasena");

        var fieldtype = pass.attr('type');

        if (fieldtype == 'password') {
            pass.attr('type', 'text');
            $(this).text("Ocultar Contraseña");
        } else {
            pass.attr('type', 'password');
            $(this).text("Ver Contraseña");
        }

    });
});