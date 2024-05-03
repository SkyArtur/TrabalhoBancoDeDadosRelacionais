(
    function (){
        let form = $('#form-register')
        if (form) {
            $(form).attr('action', window.location.pathname)
        }
    }
)()