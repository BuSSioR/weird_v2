from flask import Blueprint, jsonify, request
from project.services.weird_words import WeirdText
from project.api.errors import ResourceNotProvidedException,\
    SentenceTooShortException

encoder_blueprint = Blueprint('encoder', __name__)


class SentenceChecker(object):

    def check_sentence(self, request):
        return self.check_if_json_delivered(request)

    def check_if_json_delivered(self, request):
        post_data = request.json
        if not post_data:
            raise ResourceNotProvidedException(
                message='Provide {"sentence":"<str>"} in payload!'
            )
        return self.check_if_sentence_not_empty(request)

    def check_if_sentence_not_empty(self, request):
        post_data = request.json
        to_encode = post_data.get('sentence', None)
        if not to_encode:
            raise ResourceNotProvidedException(
                message='Provide {"sentence":"<str>"} in payload!'
            )
        return self.check_lenght(request)

    def check_lenght(self, request):
        post_data = request.json
        to_encode = post_data.get('sentence', None)
        if len(to_encode) < 4:
            raise SentenceTooShortException(
                message='Sentence is too short to be encoded!'
            )
        return to_encode


@encoder_blueprint.route('/v1/encode', methods=['POST'])
def encode():
    sentence_checker = SentenceChecker()

    to_encode = sentence_checker.check_sentence(request)
    w_conventer = WeirdText()
    encoded = w_conventer.encode_sentence(to_encode)

    return jsonify({
        'encoded': encoded
    }), 200


@encoder_blueprint.route('/v1/decode', methods=['POST'])
def decode():
    sentence_checker = SentenceChecker()
    to_decode = sentence_checker.check_sentence(request)
    w_conventer = WeirdText()
    decoded = w_conventer.decode_sentence(to_decode)

    return jsonify({
        'decoded': decoded
    }), 200
