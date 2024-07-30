
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const helmet = require('helmet');
const connectDB = require('./backend/config/database');
require('dotenv').config();

connectDB();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(bodyParser.json());
app.use(cors());
app.use(helmet());


//  solicitación de rutas   de  API  y  inicio de  servidor



const userRoutes = require('./backend/routes/userRoutes')
app.use('/api/users', userRoutes);

app.use((req, res, next) => {
  res.status(404).json({ message: 'Routas  enpoint  si  definir ' });
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Internal Server Error' });
});



//  iniciar el  servidor  de  Express  y  escuchar  en  el  puerto  ${PORT}...`);  // 

app.get('/', (req, res) => {
  res.send('API is running...');
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
