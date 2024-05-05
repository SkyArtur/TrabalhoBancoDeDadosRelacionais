const router = require("express").Router()
const axios = require("../axiosInstance")


router.get('/', (req, res) => {
    axios.get('/exercicios/3')
        .then(response => response.data)
        .then(exerc => {
            const context = {
                title: 'Exercício 3',
                exercicios: exerc
            }
            res.render('exerc/exerc03', context)
        })
        .catch(error => res.render('exerc/exerc03', error.valueOf()))
})

module.exports = router