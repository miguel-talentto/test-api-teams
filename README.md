# Flask Microsoft Teams App

Esta pequeña aplicación Flask te permite autenticarte con Microsoft Teams y obtener información sobre tu perfil y equipos utilizando la API de Microsoft Graph.

## Configuración

Antes de comenzar, necesitarás registrar tu aplicación en el [Portal de Aplicaciones de Azure](https://portal.azure.com/). Sigue estos pasos:

1. **Registro de Aplicación en Azure:**
   - Ve al [Portal de Aplicaciones de Azure](https://portal.azure.com/).
   - Crea una nueva aplicación y obtén el `client_id` y `client_secret`.
   - Configura las URLs de redireccionamiento, incluida la URL `/callback` en tu aplicación Flask.

2. **Configuración del entorno virtual:**
   - Crea un entorno virtual utilizando `venv` o `virtualenv`:
     ```bash
     python -m venv venv
     ```
   - Activa el entorno virtual:
     ```bash
     source venv/bin/activate  # En sistemas basados en Unix
     venv\Scripts\activate  # En sistemas basados en Windows
     ```

3. **Instalación de dependencias:**
   - Instala las dependencias necesarias:
     ```bash
     pip install -r requirements.txt
     ```

4. **Archivo de entorno (.env):**
   - Crea un archivo `.env` en el directorio del proyecto y agrega las siguientes variables:
     ```env
     FLASK_APP=app.py
     FLASK_ENV=development
     CLIENT_ID=tu_client_id
     CLIENT_SECRET=tu_client_secret
     REDIRECT_URI=http://localhost:5000/callback
     ```

## Uso

1. **Ejecución de la aplicación:**
   - Asegúrate de que el entorno virtual esté activado.
   - Ejecuta la aplicación Flask:
     ```bash
     python teams-api.py
     ```
   - Accede a la aplicación en [http://localhost:5000](http://localhost:5000).

2. **Inicio de Sesión:**
   - Haz clic en "Iniciar Sesión" para autenticarte con Microsoft Teams.

3. **Perfil:**
   - Después de iniciar sesión, podrás ver tu perfil de usuario.

4. **Equipos:**
   - Accede a la ruta `/get_teams` para obtener una lista de tus equipos en Microsoft Teams.

5. **Cerrar Sesión:**
   - Puedes cerrar sesión accediendo a la ruta `/logout`.

## Notas Adicionales

- Asegúrate de que tu aplicación tenga los permisos necesarios en el Portal de Aplicaciones de Azure.
- Si encuentras problemas de autorización, verifica los scopes en el archivo `app.py` y en la configuración de tu aplicación en Azure.
- Para ambientes de producción, asegúrate de configurar la aplicación en Azure con las URLs de redireccionamiento correctas y utiliza HTTPS.

¡Disfruta usando la aplicación con Microsoft Teams!

## WIP

- De momento sigue dando error obtener los equipos pero aun no se sabe si es porque no se cuenta con una organización que tenga equipos o si es por falta de permisos para leer estos aun esta WIP.