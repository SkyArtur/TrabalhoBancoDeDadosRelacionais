const router = require("express").Router()
const axios = require("../axiosInstance")

router.get('/', (req, res) => {
    axios.get('/exercicios/4')
        .then(response => response.data)
        .then(exerc => {
            const context = {
                title: 'Exercício 4',
                exercicios: exerc
            }
            res.render('exerc/exerc04', context)
        })
        .catch(error => res.render('exerc/exerc04', error.valueOf()))
})

module.exports = router