const router = require("express").Router()
const axios = require("axios")


router.get('/', (req, res) => {
    axios.get('http://localhost:8000/exercicios/3')
        .then(response => response.data)
        .then(exerc => {
            constext = {
                title: 'Exercício 3',
                exercicios: exerc
            }
            res.render('exerc/exerc03', constext)
        })
        .catch(error => res.render('exerc/exerc03', error.valueOf()))
})

module.exports = router