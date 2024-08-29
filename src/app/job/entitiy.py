DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class Job:
  def __init__(
    self,
    id,
    name,
    location,
    status,
    created_at=None,
    updated_at=None,
    deleted_at=None,
  ):
    self.id = id
    self.name = name
    self.location = location
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.deleted_at = deleted_at

  def get_data(self):
    return {
      "id": self.id,
      "name": self.name,
      "location": self.location,
      "status": self.status,
      "created_at": self.created_at,
      "updated_at": self.updated_at,
      "deleted_at": self.deleted_at,
    }

  def serealize(self):
    data = self.get_data()
    data.pop("deleted_at")
    data["created_at"] = data["created_at"].strftime(DATE_FORMAT)
    data["updated_at"] = data["updated_at"].strftime(DATE_FORMAT)
    return data
  
  @classmethod
  def from_dict(cls, data):
    id = data.get("id")
    name = data.get("name")
    location = data.get("location")
    status = data.get("status")
    created_at = data.get("created_at")
    updated_at = data.get("updated_at")
    deleted_at = data.get("deleted_at")
    
    return Job(id, name, location, status, created_at, updated_at, deleted_at)