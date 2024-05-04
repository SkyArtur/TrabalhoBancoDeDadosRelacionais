const router = require("express").Router()
const axios = require("axios")


router.get('/', (req, res) => {

    axios.get('http://localhost:8000/exercicios/2')
        .then(response => response.data)
        .then(exerc => {
            constext = {
                title: 'Exercício 2',
                exercicios: exerc
            }
            res.render('exerc/exerc02', constext)
        })
        .catch(error => res.render('exerc/exerc02', error.valueOf()))
})

module.exports = router