const router = require("express").Router()
const axios = require("axios")
const e = require("express");


router.get('/', (req, res) => {
    axios.get('http://localhost:8000/exercicios/5')
        .then(response => response.data)
        .then(exerc => {
            constext = {
                title: 'Exercício 5',
                exercicios: exerc.map((e) => {
                    e.media = `R$ ${String(e.media).replace('.', ',')}`
                    return e
                })
            }
            res.render('exerc/exerc05', constext)
        })
        .catch(error => res.render('exerc/exerc05', error.valueOf()))
})

module.exports = router