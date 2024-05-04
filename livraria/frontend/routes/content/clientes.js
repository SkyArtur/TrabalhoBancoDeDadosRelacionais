const httpStatus = require('http-status-codes')
const router = require("express").Router()
const axios = require("axios")


router.get('/', (req, res) => {
    let context = {
        title: 'Clientes',
        elements: null,
        error: null
    }
    axios.get('http://localhost:8000/clientes')
        .then(response => response.data)
        .then(clientes => {
            context.elements = clientes
            res.render('content/clientes', context)
        })
        .catch(error => {
            context.error = `Error :: ${httpStatus.INTERNAL_SERVER_ERROR} :: Verifique a conexão com o servidor.`
            res.render('content/clientes', context)
        })
})

router.post('/', (req, res) => {
    if (!req.body.id) {
        let body = {
            nome: req.body.nome,
            telefone: req.body.telefone,
            email: req.body.email,
            endereco: req.body.endereco,
        }
        axios.post('http://localhost:8000/clientes', body)
            .catch(() => res.redirect('/clientes'))
    } else {
        axios.put('http://localhost:8000/clientes', req.body)
            .catch(() => res.redirect('/clientes'))
    }
    res.redirect('/clientes')
})


module.exports = router