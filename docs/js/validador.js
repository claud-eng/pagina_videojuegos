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