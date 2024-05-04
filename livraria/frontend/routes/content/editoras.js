const router = require("express").Router()
const axios = require("axios")


router.get('/', (req, res) => {
    axios.get('http://localhost:8000/editoras')
        .then((response) => response.data)
        .then(editoras => {
            let context = {
                title: 'Editoras',
                elements: editoras
            }
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