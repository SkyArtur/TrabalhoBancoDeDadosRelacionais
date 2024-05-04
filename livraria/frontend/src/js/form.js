function simple_form() {
    let form = $('#form-register')
    let element_id = $('[element_id]')
    if (form) {
        $(element_id).each((i, e) => {
            $(e).change(ev => {
                ev.preventDefault()
                let _id = e.value
                $('#id').attr('value', _id)
                $('#nome').attr('value', $(`#nome${_id}`).text())
                $('#telefone').attr('value', $(`#telefone${_id}`).text())
                $('#email').attr('value', $(`#email${_id}`).text())
                $('#endereco').attr('value', $(`#endereco${_id}`).text())
            })
        })
        $('#app-form-clear').click(event => {
            event.preventDefault()
            $('.form-control').each((i, e) => {
                $(e).attr('value', '')
            })
        })
        $(form).attr('action', window.location.pathname)
    }
}

function input_date() {
    $('input#data').attr('value', new Date().toISOString().split('T')[0])
}

(
    function (){
        simple_form()
        input_date()
    }
)()