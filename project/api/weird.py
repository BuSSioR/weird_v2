from flask import Blueprint, jsonify, request, current_app
from project.services.weird_words import WeirdText
from project.api.errors import PayloadException
from project.handlers.handlers import check_json,check_lenght,check_list
import re
encoder_blueprint = Blueprint('encoder', __name__)


@encoder_blueprint.route('/v1/encode', methods=['POST'])
def encode():
    '''Returns encoded sentence, validates request payload.'''
    missing = check_json(['sentence'], request.json)
    if missing:
        raise PayloadException(
            message=f'Following args missing: {missing}'
        )
    to_encode = check_lenght(request.json['sentence']) 
    w_conventer = WeirdText()
    encoded = w_conventer.encode_sentence(to_encode)

    return jsonify({
        'encoded': encoded
    }), 200


@encoder_blueprint.route('/v1/decode_without_list', methods=['POST'])
def decode_without_list():
    '''Returns decoded sentence based on program algortihm,
    validates request payload.'''
    
    missing = check_json(['sentence'], request.json)
    if missing:
        raise PayloadException(
            message=f'Following args missing: {missing}'
        )
    to_decode = check_lenght(request.json['sentence']) 
    w_conventer = WeirdText()
    decoded = w_conventer.decode_sentence(to_decode)

    return jsonify({
        'decoded': decoded
    }), 200


@encoder_blueprint.route('/v1/decode', methods=['POST'])
def decode():
    '''Returns decoded sentence based on words list.'''
    missing = check_json(['sentence', 'decode_list'], request.json)
    if missing:
        raise PayloadException(
            message=f'Following args missing: {missing}'
        )
    to_decode = request.json['sentence']
    decode_list = request.json['decode_list']
    decode_list = check_list(to_decode, decode_list)
    w_conventer = WeirdText()
    decoded = w_conventer.decode_based_on_list(to_decode, decode_list)

    return jsonify({
        'decoded': decoded
    }), 200
