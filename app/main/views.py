import os
from flask import render_template, redirect, url_for
from flask.ext.login import login_required, current_user
from werkzeug.utils import secure_filename

from . import main
from .. import db
from ..models import Voter, City
from .forms import VoterForm, VoterEditForm


@main.route('/', methods=['GET'])
@login_required
def index():
    voters = Voter.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', voters=voters)


@main.route('/voter/add', methods=['POST', 'GET'])
@login_required
def voter_add():
    form = VoterForm()
    if form.validate_on_submit():
        db.session.add(Voter(dpi=form.dpi.data, name=form.name.data,
                             user_id=current_user.id, phone=form.phone.data,
                             referred=form.referred.data, city_id=form.city_id.data,
                             email=form.email.data))
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('voter.html', action='Add Voter', form=form)


@main.route('/voter/edit/<int:voterid>', methods=['POST', 'GET'])
@login_required
def voter_edit(voterid):
    voter = Voter.query.filter_by(id=voterid, user_id=current_user.id).first_or_404()
    form = VoterEditForm(obj=voter)
    if form.validate_on_submit():
        voter.dpi = form.dpi.data
        voter.name = form.name.data
        voter.phone = form.phone.data
        voter.referred = form.referred.data
        voter.city_id = form.city_id.data
        voter.email = form.email.data
        db.session.commit()

        # TODO: por aqui voy la presencia o no de archivo para upload
        # TODO: esto es el edit hay que incorporar en el add

        file = form.photo.data

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('/home/aftalavera/Dropbox/Documents/PycharmProjects/tenfold/app/static/uploads', filename))
            voter.photo = filename
            db.session.commit()

            return redirect('/static/uploads/' + filename)
        return redirect(url_for('main.index'))
    return render_template('edit_voter.html', action='Edit Voter', form=form, id=voter.id)


@main.route('/voter/delete/<int:voterid>', methods=['POST', 'GET'])
@login_required
def voter_delete(voterid):
    voter = Voter.query.filter_by(id=voterid, user_id=current_user.id).first_or_404()
    db.session.delete(voter)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/cities')
@login_required
def cities():
    cities = City.query.order_by('city_nam').all()
    return render_template('city_list.html', cities=cities)





__author__ = 'aftalavera'
