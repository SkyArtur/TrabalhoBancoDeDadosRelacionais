const router = require("express").Router()
const axios = require("../axiosInstance")
const httpStatus = require("http-status-codes")

router.get('/', (req, res) => {
    let context = {
        title: 'Pedidos',
        elements: null,
        clientes: null,
        livros: null,
        error: null
    }
    axios.get('/pedidos')
        .then(response => response.data)
        .then(pedidos => {
            context.elements = pedidos.map(pd => {
                pd.valor = `R$ ${String(pd.valor).replace('.', ',')}`
                return pd
            })
            axios.get('/clientes')
                .then(response => response.data)
                .then(clientes => {
                    context.clientes = clientes.map(cl => {return {id: cl.id, nome: cl.nome}})
                    axios.get('/livros')
                        .then(response => response.data)
                        .then(livros => {
                            context.livros = livros.map(lv => {return {id: lv.id, nome: lv.titulo}})
                            res.render('content/pedidos', context)
                        })
                })
        })
        .catch(() => {
            context.error = `Error :: ${httpStatus.INTERNAL_SERVER_ERROR} :: Verifique a conexão com o servidor.`
            res.render('content/pedidos', context)
        })
})


router.post('/', (req, res) => {
    axios.post('/pedidos', req.body)
        .catch(console.error)
    res.redirect('/pedidos')
})

module.exports = router