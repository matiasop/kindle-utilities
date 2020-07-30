# kindle-utilities

## clippings-json

Programa para convertir citas del kindle a formato json.

## vocabulario

Programa que crea un archivo .txt con el todas las palabras del vocabulario del kindle.

## diccionario

Programa para hacer consultas a una API del diccionario de wikipedia sobre las palabras del vocabulario del kindle.

## Tutoriales

### ¿Cómo obtener recortes/notas del kindle?

1) Conectar kindle por USB al computador
2) Acceder a 'Kindle/documents'
3) Ver contenidos del archivo 'My Clippings.txt'

### ¿Cómo obtener el vocabulario del kindle?

1) Conectar kindle con el USB al computador
2) Acceder al directorio 'Kindle/system/vocabulary'
3) Usar sqlite para abrir el archivo vocab.db usando el siguiente comando: sqlite3 vocab.db
4) Escribir .tables para ver las tablas en la bdd de vocab
5) Las palabras buscadas en el diccionario se encuentran en la tabla LOOKUPS. Para ver los headers de las columnas de la tabla, se debe usar el comando PRAGMA table_info(LOOKUPS);
6) Las palabras buscadas se encuentran en la columna word_key de la tabla. Para obtener las palabras se debe escribir SELECT word_key FROM LOOKUPS;
7) Listo. Ahora se puede copiar el output a otro documento.

### ¿Cómo resetear la estimación de tiempo de lectura del kindle?

1) Ir a un libro
2) Apretar el botón de búsqueda, que tiene forma de lupa
3) Escribir: ;ReadingTimeReset
