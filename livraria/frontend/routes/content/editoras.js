const router = require("express").Router()
const axios = require("axios")
const httpStatus = require("http-status-codes");


router.get('/', (req, res) => {
    let context = {
        title: 'Editoras',
        elements: null,
        error: null
    }
    axios.get('http://localhost:8000/editoras')
        .then((response) => response.data)
        .then(editoras => {
            context.elements = editoras
            res.render('content/editoras', context)
        })
        .catch(() => {
            context.error = `Error :: ${httpStatus.INTERNAL_SERVER_ERROR} :: Verifique a conexão com o servidor.`
            res.render('content/editoras', context)
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
        axios.post('http://localhost:8000/editoras', body)
            .catch(console.error)
    } else {
        axios.put('http://localhost:8000/editoras', req.body)
            .catch(console.error)
    }
    res.redirect('/editoras')
})


module.exports = router