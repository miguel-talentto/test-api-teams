# Flask Microsoft Teams App

Esta pequeña aplicación Flask te permite autenticarte con Microsoft Teams y obtener información sobre tu perfil y equipos utilizando la API de Microsoft Graph.

## Configuración

Antes de comenzar, necesitarás registrar tu aplicación en el [Portal de Aplicaciones de Azure](https://portal.azure.com/). Sigue estos pasos:


1. **Registro de Aplicación en Azure:**

1. Accede al [Portal de Aplicaciones de Azure](https://portal.azure.com/).

2. Inicia sesión con tu cuenta de Microsoft.

3. En el menú lateral izquierdo (menu hamburguesa), selecciona "Azure Active Directory o Microsoft Entra ID".

4. En el menú de Microsoft Entra ID, selecciona "Registro de aplicaciones".

5. Haz clic en "Nuevo registro" para crear una nueva aplicación.

6. Completa los detalles de registro de la aplicación:
   - **Nombre de la aplicación:** Un nombre descriptivo para tu aplicación.
   - **Tipos de cuenta admitidos:** Puedes seleccionar según tus necesidades, por ejemplo, "Cuentas de cualquier directorio de identidades de organizaciones y usuarios personales de cuentas de Microsoft".
   - **URL de redireccionamiento (URI):** Configura las URLs de redirección, incluida la URL `/callback` en tu aplicación Flask. Para desarrollo local, podría ser algo como `http://localhost:5000/callback`.

7. Después de crear la aplicación, anota el `client_id` y el `Directory (tenant) ID` desde la página de visión general de la aplicación. Necesitarás estos valores en tu código.

8. Para obtener el `client_secret`, ve a la sección "Certificados y Secretos" en la página de la aplicación recién creada. Crea un nuevo secreto y toma nota del valor generado. Ten cuidado de almacenar este valor de manera segura, ya que no podrás verlo nuevamente debes tomar el client_secret `value` no el id.

9. Además, asegúrate de configurar los permisos necesarios para tu aplicación. Ve a la sección "API de Microsoft Graph" y selecciona los permisos que necesitas, como `User.Read`, `TeamMember.Read.All`, `ChannelMessage.Read.All`, `Team.ReadBasic.All`, etc.

10. Guarda los cambios y tu aplicación estará registrada en Azure.

Ahora, puedes utilizar el `client_id`, el `client_secret` (este debe ser el value del client no el id), y la URL de redirección configurada en tu aplicación Flask para realizar la autenticación y autorización a través de Microsoft Teams. Asegúrate de incorporar estos valores en tu código para que tu aplicación Flask pueda interactuar correctamente con la API de Microsoft Teams.


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
   - Copia el archivo `.env.example` y dejalo como `.env` y cambia las claves con la de tu aplicación OJO el `APP_KEY` es del Flask no de azure ese puede ser cualquier cosa random

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
