# PROMPTS GPT
POTENCIA

Hola chat, me encuentro en el laboratorio de la materia "comunicaciones 1" de la universidad industrial de santander, y necesito tu ayuda para realizar un codigo de python para la generación de una simulación con el programa GNU RADIO

Primero, vamos a definir el primer bloque que se va a encarga de la estimación de potencia, el bloque es el bloque "embeded python block" de gnu radio, el bloque debe tener como entrada un vector de tipo complejo y UNA salida de SOLO UN ITEM de tipo float, la función debe calcular la potencia promedio de la ventana de entrada. La potencia se define como la media del cuadrado de la magnitud de las muestras.

Ok, en segundo lugar, debes generarme una función con el mismo bloque "embedded python block", en este caso la función es extraer las estadistica de amplitud. Necesito que me generes el bloque con una entrada vector de tipo complejo y con dos salidas, un solo item por salida y ambas de tipo flotante. La salida 0 debe ser la media de la magnitud de las muestras de entrada, la salida 1 debe ser la desviación estandar de esas mismas muestras

Estas haciendo bien el trabajo, pero estas interpretando como si se te entregara un vector, y se te entrega es una secuencia de datos, debes iterar

Necesito que me hagas lo mismo para el bloque de potencia, te lo agradecería muchisimo

