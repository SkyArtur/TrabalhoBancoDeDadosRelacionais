const router = require("express").Router()
const axios = require("../axiosInstance")


router.get('/', (req, res) => {
    axios.get('/exercicios/6')
        .then(response => response.data)
        .then(exerc => {
            const context = {
                title: 'Exercício 6',
                exercicios: exerc
            }
            res.render('exerc/exerc06', context)
        })
        .catch(error => res.render('exerc/exerc06', error.valueOf()))
})



module.exports = router