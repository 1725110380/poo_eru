class LibroBiblioteca:
    def __init__(self, numero_folio, numero_paginas, nombre, autor, titulo, 
                 editorial, condicion_libro, isbn, formato, idioma):
        
        self.numero_folio = numero_folio
        self.numero_paginas = numero_paginas
        self.nombre = nombre
        self.autor = autor
        self.titulo = titulo
        self.editorial = editorial
        self.condicion_libro = condicion_libro
        self.isbn = isbn
        self.formato = formato
        self.idioma = idioma
        
        print(f" Numero de Folio : {self.numero_folio}")
        print(f" Numero de paginas : {self.numero_paginas}")
        print(f" Nombre : {self.nombre}")
        print(f" Autor : {self.autor}")
        print(f" Titulo : {self.titulo}")
        print(f" Editorial : {self.editorial}")
        print(f" Condicion del libro : {self.condicion_libro}")
        print(f" ISBN : {self.isbn}")
        print(f" Formato : {self.formato}")
        print(f" Idioma : {self.idioma}")

    def clasificacion(self):
        print("clasificar el libro")

    def catalogarlo(self):
        print("Catalogar el libro")

    def prestar(self):
        print("Prestar el libro")

    def leer(self):
        print("Leer el libro")

    def comprar(self):
        print("comprar libro")

noches_blancas = LibroBiblioteca(
    numero_folio="FOL-2026-NB",
    numero_paginas="112",
    nombre="Noches Blancas",
    autor="Fiódor Dostoyevski",
    titulo="Noches blancas y otros relatos",
    editorial="Alianza Editorial",
    condicion_libro="Excelente",
    isbn="978-84-206-5126-2",
    formato="Físico (Pasta blanda)",
    idioma="Español"
)

noches_blancas.leer()