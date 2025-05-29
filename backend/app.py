import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db, Game
from datetime import datetime

app = Flask(__name__)
CORS(app)

DB_USER = 'main'
DB_PASSWORD = 'vini230904'
DB_HOST = 'novodb.cy5hytcq78mc.us-east-1.rds.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'postgres'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/games', methods=['GET'])
def listar_games():
    games = Game.query.all()
    return jsonify([g.to_dict() for g in games]), 200

@app.route('/games', methods=['POST'])
def adicionar_game():
    data = request.get_json()
    novo = Game(nome=data['nome'], categoria=data['categoria'], ano=int(data['ano']))
    db.session.add(novo)
    db.session.commit()
    return jsonify({"mensagem": "Jogo adicionado com sucesso!"}), 201

@app.route('/update', methods=['POST'])
def atualizar_game():
    data = request.get_json()
    game = Game.query.get(int(data['id']))
    if not game:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    game.nome = data['nome']
    game.categoria = data['categoria']
    game.ano = int(data['ano'])
    db.session.commit()
    return jsonify({"mensagem": "Jogo atualizado com sucesso!"})

@app.route('/delete', methods=['POST'])
def deletar_game():
    data = request.get_json()
    game = Game.query.get(int(data['id']))
    if game:
        db.session.delete(game)
        db.session.commit()
        return jsonify({"mensagem": "Jogo deletado com sucesso!"})
    return jsonify({"erro": "Jogo não encontrado"}), 404

@app.route('/report', methods=['GET'])
def gerar_relatorio():
    games = Game.query.all()
    return jsonify({
        "totalItems": len(games),
        "lastUpdate": datetime.utcnow().isoformat() + "Z"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
