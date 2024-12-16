def validLoginData(username, password) :
  data = {"username" : username, "password" : password}
  if (username == 'admin' and password == "admin"):
    data = {"username" : "", "password" : ""}
    return {
      "valid" : True,
      "message" : "Login successfully !",
      "type" : "success",
      "data" : data
    }
  return {
    "valid" : False,
    "message" : "invalid username or password !",
    "type" : "warning",
    "data" : data
  }

def validRegisterData(username, email, password, confirm_password, terms) :
  data = {
    "username" : username,
    "email" : email,
    "password" : password,
    "confirm_password" : confirm_password,
    "terms" : terms
  }
  if not terms :
    return {
      "valid" : False,
      "message" : "Please Accept terms and conditions !",
      "type" : "warning",
      "data" : data
    }
  elif password != confirm_password :
    return {
      "valid" : False,
      "message" : "Passwords don't Match !",
      "type" : "warning",
      "data" : data
    }
  else :
    data = {
      "username" : "",
      "email" : "",
      "password" : "",
      "confirm_password" : ""
    }
  return {
    "valid" : True,
    "message" : "Register successfully !",
    "type" : "success",
    "data" : data
  }

