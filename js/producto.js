const { createApp } = Vue
createApp({
    data() {
        return {
            productos: [],
            url: 'https://eli24177x.pythonanywhere.com/productos',
            error: false,
            cargando: true,
            /*atributos para el guardar los valores del formulario */
            id: 0,
            nombre: "",
            stock: 0,
            precio: 0,
            tipo: "",
            caracteristicas: "",
            peso: 0,
            altura: 0,
            imagen: null
        }
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.productos = data;
                    this.cargando = false

                    console.log(this.productos)
                })
                .catch(err => {
                    console.error(err);
                    this.error = true
                })
        },
        eliminar(id) {
            const url = this.url + '/' + id;
            var options = {
                method: 'DELETE',
            }
            fetch(url, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
                    alert('Registro Eliminado')
                    location.reload(); // recarga el json luego de eliminado el registro
                })
        },
        grabar() {
            let producto = {
                nombre: this.nombre,
                precio: this.precio,
                stock: this.stock,
                tipo: this.tipo,
                caracteristicas: this.caracteristicas,
                peso: this.peso,
                altura: this.altura,
                imagen: this.imagen
            }
            var options = {
                body: JSON.stringify(producto),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
                    alert("Registro grabado")
                    window.location.href = "./productos.html";  // recarga productos.html
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar")  // puedo mostrar el error tambien
                })
        },

        onFileChange(event) {
            const file = event.target.files[0];
            if (file) {
                this.imagen = URL.createObjectURL(file);
            }
        }
    },
    created() {
        this.fetchData(this.url)
    },
}).mount('#app')
