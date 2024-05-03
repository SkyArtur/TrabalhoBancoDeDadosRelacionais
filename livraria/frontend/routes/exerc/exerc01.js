const router = require("express").Router()
const axios = require("axios")


router.get('/', (req, res) => {
    res.render('exerc/exerc01')
})

module.exports = router