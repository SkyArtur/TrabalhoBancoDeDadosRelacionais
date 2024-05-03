const express = require('express')
const app = express()
const path = require('path')
const server = require('http').createServer(app)
const port = process.env.PORT || 3000
const {
    routerHome,
    routerClientes,
    routerEditoras,
    routerLivros,
    routerPedidos,
    routerExerc01,
    routerExerc02,
    routerExerc03,
    routerExerc04,
    routerExerc05,
    routerExerc06,
} = require('./routes')


app.set('view engine', 'pug')
app.set('views', path.join(__dirname, 'views'))
app.set('port', port)
app.use(express.static(path.join(__dirname, 'public')))
app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use('/', routerHome)
app.use('/clientes', routerClientes)
app.use('/editoras', routerEditoras)
app.use('/livros', routerLivros)
app.use('/pedidos', routerPedidos)
app.use('/exerc01', routerExerc01)
app.use('/exerc02', routerExerc02)
app.use('/exerc03', routerExerc03)
app.use('/exerc04', routerExerc04)
app.use('/exerc05', routerExerc05)
app.use('/exerc06', routerExerc06)



server.listen(port, () => {
    console.log(`Server started on port http://localhost:${port}`)
})

