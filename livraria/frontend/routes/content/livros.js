const router = require("express").Router()
const axios = require("axios")
const httpStatus = require("http-status-codes");


router.get('/', (req, res) => {
    let context = {
        title: 'Livros',
        editoras: null,
        elements: null,
        error: null
    }
    axios.get('http://localhost:8000/livros')
        .then(response => response.data)
        .then(livros => {
            axios.get('http://localhost:8000/editoras')
                .then(response => response.data)
                .then(editoras => {
                    context.elements = livros.map(lv => {
                        lv.preco = `R$ ${String(lv.preco).replace('.', ',')}`
                        return lv
                    })
                    context.editoras = editoras
                    res.render('content/livros', context)
                })
        })
        .catch(() => {
            context.error = `Error :: ${httpStatus.INTERNAL_SERVER_ERROR} :: Verifique a conexão com o servidor.`
            res.render('content/livros', context)
        })
})

router.post('/', (req, res) => {
    req.body.preco = Number(req.body.preco)
    axios.post('http://localhost:8000/livros', req.body)
        .catch(console.error)
    res.redirect('/livros')
})

module.exports = router