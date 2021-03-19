import flask
from flask import jsonify, request
from data.users import User
from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return flask.jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'team_leader', 'collaborators', 'is_finished', 'work_size', 'user_id', 'id'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_news(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'job', 'team_leader', 'collaborators', 'is_finished', 'work_size', 'user_id', 'id'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['job', 'team_leader', 'collaborators', 'is_finished', 'work_size', 'user_id']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first():
        return ({'error': 'Id already exists'})
    jobs = Jobs(
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        collaborators=request.json['collaborators'],
        work_size=request.json['work_size'],
        is_finished=request.json['is_finished'],
        user_id=request.json['user_id'],
        id=request.json['id']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_news(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def edit_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db_sess = db_session.create_session()
    if not db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first():
        return {'error': 'Id already not exists'}
    jobs = db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first()
    db_sess.commit()
    return jsonify({'success': 'OK'})