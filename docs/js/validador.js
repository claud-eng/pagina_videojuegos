$("#formulario1").validate({
    rules: {
        "txtEmail": {
            required: true,
            email: true
        },
        "txtContrasena": {
            required: true,
            minlength: 5
        }
    }, 
    messages: {
        "txtEmail": {
            required: 'Ingrese su email, por favor',
            email: 'No cumple el formato'
        },
        "txtContrasena": {
            required: 'Ingrese su contraseña, por favor',
            minlength: 'Error, la contraseña debe poseer un mínimo de 5 caracteres'
        }
    } 
});

jQuery(document).ready(function () {
    // Show password Button
    $("#formulario2").validate({
        rules: {
            "txtNombre": {
                required: true,
                minlength: 3
            },
            "txtApellido": {
                required: true,
                minlength: 3
            },
            "txtFechaNacimiento": {
                required: true
            },
            "cmbRegion": {
                required: true
            },
            "txtEmail": {
                required: true,
                email: true
            },
            "txtContrasena": {
                required: true,
                minlength: 5
            },
            "txtRepetirContrasena": {
                required: true,
                equalTo: '#id_txtContrasena'
            },
            "novedades": {
                required: true,
            }
    
        }, // --> Fin de reglas
        messages: {
            "txtNombre": {
                required: 'Por favor, ingrese su nombre.',
                minlength: 'Min. 3 caract.'
            },
            "txtApellido": {
                required: 'Por favor, ingrese su apellido.',
                minlength: 'Min. 3 caract.'
            },
            "txtFechaNacimiento": {
                required: 'Por favor, seleccione su fecha de nacimiento.'
            },
            "cmbRegion": {
                required: 'Por favor, seleccione una región.'
            },
            "txtEmail": {
                required: 'Por favor, ingrese su email.',
                email: 'No cumple formato.'
            },
            "txtContrasena": {
                required: 'Por favor, ingrese una contraseña.',
                minlength: 'Min. 5 caract.'
            },
            "txtRepetirContrasena": {
                required: 'Por favor, debe repetir la contraseña anterior.',
                equalTo: 'Las contraseñas no coinciden, intente de nuevo.'
            },
            "novedades": {
                required: 'Por favor, seleccione una opción'
            }
        } //-->Fin de mensajes
     
    });
    
 
});