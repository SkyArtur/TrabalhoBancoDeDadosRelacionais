const router = require("express").Router()
const axios = require("axios")


router.get('/', (req, res) => {
    res.render('home')
})

module.exports = router