const router = require("express").Router()
const axios = require("axios")


router.get('/', (req, res) => {
    axios.get('http://localhost:8000/exercicios/4')
        .then(response => response.data)
        .then(exerc => {
            constext = {
                title: 'Exercício 4',
                exercicios: exerc
            }
            res.render('exerc/exerc04', constext)
        })
        .catch(error => res.render('exerc/exerc04', error.valueOf()))
})

module.exports = router