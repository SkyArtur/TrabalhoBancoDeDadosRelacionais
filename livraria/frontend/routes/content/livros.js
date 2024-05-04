const router = require("express").Router()
const axios = require("axios")


router.get('/', (req, res) => {
    axios.get('http://localhost:8000/livros')
        .then(response => response.data)
        .then(livros => {
            axios.get('http://localhost:8000/editoras')
                .then(response => response.data)
                .then(editoras => {
                    let context = {
                        title: 'Livros',
                        editoras: editoras,
                        elements: livros
                    }
                    res.render('content/livros', context)
                })
        })
})

router.post('/', (req, res) => {
    req.body.preco = Number(req.body.preco)
    axios.post('http://localhost:8000/livros', req.body)
        .catch(console.error)
    res.redirect('/livros')
})

module.exports = router