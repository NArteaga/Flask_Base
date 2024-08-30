from src import router , client
from flask import request
from src.app.job.repository import JobRepository
from src.libs.response import ok, error
from datetime import datetime, timezone

repository_job = JobRepository(client)
@router.route('/job', methods=['GET'])
def get_job():
  try:
    job = repository_job.get_job()
    return ok(job)
  except Exception as e:
    return error(500, str(e))

@router.route('/job/<int:id>', methods=['GET'])
def get_by_id(id):
  try:
    job = repository_job.get_by_id(id)
    return ok(job)
  except Exception as e:
    return error(500, str(e))

@router.route('/job', methods=['POST'])
def create_job():
  try:
    job = request.get_json()
    current_time = datetime.now(timezone.utc)
    job["created_at"] = current_time
    job["updated_at"] = current_time
    result = repository_job.create_job(job)
    return ok(result)
  except Exception as e:
    return error(500, str(e))

@router.route('/job/<int:id>', methods=['PATCH'])
def update_job(id):
  try:
    job = request.get_json()
    current_time = datetime.now(timezone.utc)
    job["updated_at"] = current_time
    result = repository_job.update_job(id, job)
    return ok(result)
  except Exception as e:
    return error(500, str(e))

@router.route('/job/<int:id>', methods=['DELETE'])
def delete_logic_job(id):
  try:
    current_time = datetime.now(timezone.utc)
    job = { "deleted_at": current_time }
    result = repository_job.update_job(id, job)
    return ok(result)
  except Exception as e:
    return error(500, str(e))

@router.route('/job/del/<int:id>', methods=['DELETE'])
def delete_physical_job(id):
  try:
    result = repository_job.delete_job(id)
    return ok(result)
  except Exception as e:
    return error(500, str(e))