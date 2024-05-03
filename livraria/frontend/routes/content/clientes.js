const router = require("express").Router()
const axios = require("axios")


router.get('/', (req, res) => {
    res.render('content/clientes')
})

module.exports = router