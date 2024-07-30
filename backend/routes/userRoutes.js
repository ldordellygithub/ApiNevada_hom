const express = require('express');
const { getAllUsers, getUserById, createUser, updateUser, deleteUser } = require('../controllers/usercontrollers');

const router = express.Router();

// GET /api/users - Obtener todos los usuarios
router.get('/', getAllUsers);

// GET /api/users/:id - Obtener un usuario por ID
router.get('/:id', getUserById);

// POST /api/users - Crear un nuevo usuario
router.post('/', createUser);

// PUT /api/users/:id - Actualizar un usuario por ID
router.put('/:id', updateUser);

// DELETE /api/users/:id - Eliminar un usuario por ID
router.delete('/:id', deleteUser);

module.exports = router;
