
function links(elements, formated) {
    let attribute = `[${elements}]`
    let links = $(attribute)
    $(links).each((i, link) => {
        let [url, _target] = $(link).attr(elements).split(' ')
        $(link).click(e => {
            window.open(url, _target ?? '_self')
        })
        if  (window.location.pathname === url){
            $(link).toggleClass(formated)
            $(link).children('h6').toggleClass('text-bg-dark')
        }
    })
}
(
    function (){
        links('a-link', 'bg-body')
        links('a-exerc', 'shadow')
    }
)()

