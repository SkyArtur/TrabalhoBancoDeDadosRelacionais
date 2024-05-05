const router = require("express").Router()
const axios = require("../axiosInstance")

router.get('/', (req, res) => {
    axios.get('/exercicios/5')
        .then(response => response.data)
        .then(exerc => {
            const context = {
                title: 'Exercício 5',
                exercicios: exerc.map((e) => {
                    e.media = `R$ ${String(e.media).replace('.', ',')}`
                    return e
                })
            }
            res.render('exerc/exerc05', context)
        })
        .catch(error => res.render('exerc/exerc05', error.valueOf()))
})

module.exports = router