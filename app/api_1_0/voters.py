from flask import jsonify
from . import api
from ..models import Voter
from cee import cee_source


@api.route('/voters/<int:voterid>')
def get_voter(voterid):
    # voter = Voter.query.get_or_404(voterid)
    voter = cee_source(voterid)
    # return jsonify(voter.dict())
    return jsonify(voter)


@api.route('/voters')
def list_voters():
    voters = Voter.query.all()
    for voter in voters:
        yield jsonify(voter)
