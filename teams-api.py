from flask import Flask, redirect, request, session, url_for, render_template
import msal
import requests
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('APP_KEY')

# Configuración de la aplicación (reemplaza con tus propios valores)
client_id = os.getenv('APP_CLIENT')
client_secret = os.getenv('APP_SCRET')
redirect_uri = os.getenv('REDIRECT_URI')

# Nuestro tenantId
tenant_id = os.getenv('TENANT_ID')

# Authority 
authority = 'https://login.microsoftonline.com/' + tenant_id

# Scopes necesarios
SCOPES = ['User.Read', 'TeamMember.Read.All', 'ChannelMessage.Read.All', 'Team.ReadBasic.All']

# Endpoint de token
token_url = 'https://login.microsoftonline.com/' + tenant_id + '/oauth2/v2.0/token'

# Configuración de MSAL
msal_app = msal.ConfidentialClientApplication(
    client_id,
    authority=authority,
    client_credential=client_secret
)

@app.route('/')
def home():
    return render_template('index.html', authenticated='access_token' in session)

@app.route('/login')
def login():
    auth_url = msal_app.get_authorization_request_url(
        scopes=SCOPES,
        redirect_uri=redirect_uri
    )
    return redirect(auth_url)

@app.route('/callback')
def callback():
    error = request.args.get('error')
    error_description = request.args.get('error_description')

    if error:
        return f'Error en la autorización: {error}, Descripción: {error_description}'

    auth_code = request.args.get('code')

    if auth_code:
        result = msal_app.acquire_token_by_authorization_code(
            auth_code,
            scopes=SCOPES,
            redirect_uri=redirect_uri
        )

        if 'error' in result:
            return f'Error al obtener el token: {result["error_description"]}'

        # Guardar el token en la sesión
        session['access_token'] = result['access_token']
        return redirect(url_for('profile'))
    else:
        return 'Código de autorización no presente en la URL de retorno'

@app.route('/profile')
def profile():
    if 'access_token' not in session:
        return redirect(url_for('login'))

    # Obtener información sobre el usuario
    graph_url = 'https://graph.microsoft.com/v1.0/me'
    headers = {
        'Authorization': 'Bearer ' + session.get('access_token'),
        'Accept': 'application/json'
    }
    user_response = requests.get(graph_url, headers=headers)

    if user_response.status_code == 200:
        user_data = user_response.json()
        return render_template('profile.html', user=user_data)
    else:
        return f'Error al obtener información del usuario: {user_response.text}'

@app.route('/get_teams')
def get_teams():
    if 'access_token' not in session:
        return redirect(url_for('login'))

    # Obtener la lista de equipos del usuario
    graph_url = 'https://graph.microsoft.com/v1.0/me/joinedTeams'
    headers = {
        'Authorization': 'Bearer ' + session.get('access_token'),
        'Accept': 'application/json'
    }
    teams_response = requests.get(graph_url, headers=headers)

    if teams_response.status_code == 200:
        teams_data = teams_response.json()
        teams_info = [{'Equipo': team['displayName'], 'ID': team['id']} for team in teams_data.get('value', [])]
        return render_template('teams.html', teams=teams_info)
    else:
        return f'Error al obtener la lista de equipos: {teams_response.text}'

@app.route('/logout')
def logout():
    # Obtener la cuenta del contexto de la sesión
    account = msal_app.get_accounts()
    print('account')
    print(account)
    if account:
        msal_app.remove_account(account[0])
        
    # Limpiar la sesión
    session.clear()
    print('clear')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)