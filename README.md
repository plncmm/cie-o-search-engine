## Instalación

1. Crear un ambiente virtual de python e instalar los requerimientos del `requirements.txt`
2. Ejecutar los archivos `index_m.py` e `index_t.py` con el intérprete Python del ambiente virtual creado anteriormente para la creación de los índices.
2. Lanzar el servidor de clasificación con el comando `<ubicación de los binarios del ambiente virtual>/uvicorn main:app`

## Utilización

Este servicio web expone endpoints para la búsqueda en la nomenclatura CIE-O-M y CIE-O-T en `/cie-o-m` y `/cie-o-t` respectivamente. Para realizar una búsqueda, se debe enviar una petición GET al respectivo endpoint con la cadena de búsqueda en el parámetro `q`.

El sevicio responderá con una lista resultados, donde cada resultado es un objeto tiene las siguientes propiedades:

* `code`: Código de la nomenclatura consultada.
* `description`: Descripción del código de la nomenclatura consultada.
* `score`: Valor de la métrica BM25F en el resultado (mientras mayor sea, este resultado es más cercano a la cadena de consulta). 

## Ejemplo de utilización

Para buscar la cadena de texto adenocarcinoma tubular en CIE-O-M se debe realizar la siguiente petición:

```bash
curl --location --request GET 'http(s)://<server url>/cie-o-m?q=adenocarcinoma%20tubular'
```

y la respuesta será la siguiente:

```javascript
[
    {
        "code": "8211/3",
        "description": "Adenocarcinoma tubular",
        "score": 14.65240778171962
    },
    {
        "code": "8211/6",
        "description": "Adenocarcinoma tubular, metástasis",
        "score": 7.883117241094898
    },
    {
        "code": "8210/3",
        "description": "Adenocarcinoma en pólipo adenomatoso",
        "score": 7.528550603683486
    },
    {
        "code": "8263/3",
        "description": "Adenocarcinoma en adenoma tubulovelloso",
        "score": 7.19567170881193
    },
    {
        "code": "8210/2",
        "description": "Adenocarcinoma in situ en pólipo adenomatoso",
        "score": 6.563115285083312
    },
    {
        "code": "8503/3",
        "description": "Adenocarcinoma papilar intraductal con invasión",
        "score": 6.25229547114941
    },
    {
        "code": "8571/3",
        "description": "Adenocarcinoma con metaplasia ósea y cartilaginosa",
        "score": 6.25229547114941
    },
    {
        "code": "8525/3",
        "description": "Adenocarcinoma polimorfo de bajo grado",
        "score": 6.0067746976636975
    },
    {
        "code": "8215/3",
        "description": "Adenocarcinoma de glándulas anales",
        "score": 5.934968311877492
    },
    {
        "code": "8408/3",
        "description": "Adenocarcinoma papilar ecrino",
        "score": 5.934968311877492
    }
] 
```