"""
El flujo es: 1., 2., 3., 4., 5.
ls -a: lista todos los archivos inclusive los ocultos
1. git init: inicializa repositorio crea .git
git status: ve el estado del repositorio
2. git add . // git add index.html: Pasa el archivo de git init a staging
3. git commit -m "mensaje": pasa el archivo al repositorio local para su seguimiento,
version guardada.
4. git log --oneline: muestra todos los commits realizados ejm: 7f047b8 Comienzo del proyecto
5. git reset hard f047b8: mueve al head, restaura archivos, descarta cambios
open index.html: abre el archivo directamente en el navegador
git log: muestra información detallada
git log --oneline --graph --decorate: 
"""

print("Hola mundo desde Python")
print("Segunda linea")
print("Tercera linea")