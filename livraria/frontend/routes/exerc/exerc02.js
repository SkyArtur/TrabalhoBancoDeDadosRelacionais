const router = require("express").Router()
const axios = require("../axiosInstance")


router.get('/', (req, res) => {

    axios.get('/exercicios/2')
        .then(response => response.data)
        .then(exerc => {
            const context = {
                title: 'Exercício 2',
                exercicios: exerc
            }
            res.render('exerc/exerc02', context)
        })
        .catch(error => res.render('exerc/exerc02', error.valueOf()))
})

module.exports = router