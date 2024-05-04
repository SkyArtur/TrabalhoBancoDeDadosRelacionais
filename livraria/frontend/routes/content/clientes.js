const router = require("express").Router()
const axios = require("axios")


router.get('/', (req, res) => {
    axios.get('http://localhost:8000/clientes')
        .then(response => response.data)
        .then(clientes => {
            let context = {
                title: 'Clientes',
                elements: clientes
            }
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
            .catch(console.error)
    } else {
        axios.put('http://localhost:8000/clientes', req.body)
            .catch(console.error)
    }
    res.redirect('/clientes')
})


module.exports = router