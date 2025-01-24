const express = require('express');
const mongoose = require('mongoose');
const Response = require('./models/response');

const app = express();
app.use(express.json());


// Conectar ao MongoDB
mongoose.connect('mongodb+srv://eusouanderson:67983527@cluster0.fuidnmk.mongodb.net/assistenteBot', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Conectado ao MongoDB'))
    .catch((err) => console.error('Erro ao conectar ao MongoDB:', err));

app.get('/', (req, res) => {
    res.send('Server is running!');
})

// Rota para salvar frases
app.post('/api/responses', async (req, res) => {
    try {
        const { phrase, response } = req.body;
        const newResponse = new Response({ phrase, response });
        await newResponse.save();
        res.status(201).json(newResponse);
    } catch (err) {
        res.status(500).json({ message: 'Erro ao salvar resposta', error: err });
    }
});

// Rota para ler todas as frases e respostas
app.get('/api/responses', async (req, res) => {
    try {
        const responses = await Response.find();
        res.status(200).json(responses);
    } catch (err) {
        res.status(500).json({ message: 'Erro ao buscar respostas', error: err });
    }
});

// Iniciar o servidor
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Servidor rodando na porta ${port}`);
});
