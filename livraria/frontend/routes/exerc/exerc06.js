const router = require("express").Router()
const axios = require("axios")



router.get('/', (req, res) => {
    axios.get('http://localhost:8000/exercicios/6')
        .then(response => response.data)
        .then(exerc => {
            constext = {
                title: 'Exercício 6',
                exercicios: exerc
            }
            res.render('exerc/exerc06', constext)
        })
        .catch(error => res.render('exerc/exerc06', error.valueOf()))
})



module.exports = router