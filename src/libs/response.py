from flask import jsonify
def ok(result, message = "OK"):
  response = {
    "status": 200,
    "finally": True,
    "message": message
  }
  if result is not None:
    response["data"] = result
  return jsonify(response), 200
  
def error(code = 500, message = 'Bad Request'):
  return jsonify({
    "status": code,
    "finally": False,
    "message": message,
  }), code