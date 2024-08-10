
# src/servidor/autenticacion.py

TOKENS_AUTORIZADOS = ['service1_token', 'service2_token']

def check_token(token):
    return token in TOKENS_AUTORIZADOS

