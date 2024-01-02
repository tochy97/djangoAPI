const loginRequest = (uname, psw) => ({
  "query": `mutation TokenAuth($password: String!, $username: String!){ 
    tokenAuth(password: $password, username: $username) 
      { 
        payload refreshExpiresIn token 
      }
    }`,
  "variables": {password: psw, username: uname}
})

