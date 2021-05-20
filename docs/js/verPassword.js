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

jQuery(document).ready(function () {
    // Show password Button
    $("#showpassword").on('click', function () {
 
        var pass = $("#id_txtContrasena2");
        var pass2 = $("#id_txtRepetirContrasena2");
 
        var fieldtype = pass.attr('type');
        var fieldtype2 = pass2.attr('type');
 
        if (fieldtype == 'password' & fieldtype2 == 'password') {
            pass.attr('type', 'text');
            pass2.attr('type', 'text');
            $(this).text("Ocultar Password");
        } else {
            pass.attr('type', 'password');
            pass2.attr('type', 'password');
            $(this).text("Ver Password");
        }
 
    });
 
});