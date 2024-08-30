from sqlalchemy import Table, Column, Integer, String, DateTime
from src.app.job.entitiy import Job
from src.libs.error import Exceptions

class JobRepository():
  def __init__(self, client):
    self.client = client
    self.session_factory = client.session_factory
    self.test = False
    
    table_name = "job"
    
    self.job_table = Table(
      table_name,
      client.mapper_registry.metadata,
      Column("id", Integer, primary_key=True),
      Column("name", String(255)),
      Column("location", String(255)),
      Column("status", String(255)),
      Column("created_at", DateTime),
      Column("updated_at", DateTime),
      Column("deleted_at", DateTime),
    )
    client.mapper_registry.map_imperatively(Job, self.job_table)
    
  def get_job(self):
    with self.session_factory() as session:
      jobs = session.query(Job).filter_by(deleted_at = None).all()
      result = []
      for job in jobs:
        result.append(job.serealize())
      return result
    
  def get_by_id(self, id):
    with self.session_factory() as session:
      job = session.query(Job).filter_by(id = id, deleted_at = None).first()
      if (job):
        return job.serealize()
      raise Exceptions('Not found registered with job id: ' + str(id))
      
  def create_job(self, job):
    with self.session_factory() as session:
      try:
        data = Job.from_dict(job)
        result = session.add(data)
        session.flush()
        session.refresh(data)
        session.commit()
        return data.serealize()
      except Exception as e:
        raise Exceptions('Not created registered the job')
  
  def update_job(self, id, fields):
    with self.session_factory() as session:
      session.query(Job).filter_by(id = id, deleted_at = None).update(fields)
      session.commit()
      job = session.query(Job).filter_by(id = id, deleted_at = None).first()
      if (job):
        return job.serealize()
      if (fields["deleted_at"]):
        return None
      raise Exceptions('Not updated registered with job id: ' + str(id))
  
  def delete_job(self, id):
    with self.session_factory() as session:
      try:
        job = session.query(Job).get(id)
        session.delete(job)
        session.commit()
        return 'ok'
      except Exception as e:
        raise Exceptions('Not deleted registered the job')
