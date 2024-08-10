from flask import request, jsonify
from datetime import datetime
import sqlite3

TOKENS_AUTORIZADOS = ['service1_token', 'service2_token']

def configuracion_rutas_logging(app):
    
    def insertar_log(log_data):
        conn = sqlite3.connect('logs.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO logs (timestamp, received_at, service_name, severity, message)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            log_data['timestamp'],
            datetime.utcnow(),
            log_data['service_name'],
            log_data['severity'],
            log_data['message']
        ))
        conn.commit()
        conn.close()

    def obtener_logs(start_date=None, end_date=None, severity=None, creation_date=None):
        conn = sqlite3.connect('logs.db')
        cursor = conn.cursor()
        
        query = "SELECT timestamp, received_at, service_name, severity, message FROM logs WHERE 1=1"
        params = []
        
        if start_date:
            query += " AND timestamp >= ?"
            params.append(start_date)
        
        if end_date:
            query += " AND timestamp <= ?"
            params.append(end_date)
        
        if severity:
            query += " AND severity = ?"
            params.append(severity)
        
        if creation_date:
            query += " AND timestamp LIKE ?"
            params.append(creation_date + '%')
        
        cursor.execute(query, params)
        logs = cursor.fetchall()
        conn.close()

        logs_list = [{
            "timestamp": log[0],
            "received_at": log[1],
            "service_name": log[2],
            "severity": log[3],
            "message": log[4]
        } for log in logs]
        
        return logs_list
    
    @app.route('/')
    def home():
        return "Servidor Flask está funcionando"

    @app.route('/logs', methods=['POST'])
    def recibir_logs():
        token = request.headers.get('Authorization')
        if token not in TOKENS_AUTORIZADOS:
            return jsonify({"error": "No autorizado"}), 401
        
        log_data = request.get_json()
        if not log_data:
            return jsonify({"error": "Datos inválidos"}), 400
        
        insertar_log(log_data)
        return jsonify({"message": "Log recibido"}), 200

    @app.route('/logs', methods=['GET'])
    def mostrar_logs():
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        severity = request.args.get('severity')
        creation_date = request.args.get('creation_date')

        try:
            if start_date:
                start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
                start_date = start_date.strftime('%Y-%m-%d %H:%M:%S')
            if end_date:
                end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
                end_date = end_date.strftime('%Y-%m-%d %H:%M:%S')
            if creation_date:
                creation_date = datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%S')
                creation_date = creation_date.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({"error": "Formato de fecha inválido"}), 400
        
        logs_list = obtener_logs(start_date, end_date, severity, creation_date)
        return jsonify(logs_list), 200
