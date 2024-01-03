const verifyRequest = (data) => ({
    "query": `mutation VerifyToken($token: String!){ 
        verifyToken(token: $token) 
        { 
          payload
        }
      }`,
    "variables": {token: data}
  })
  
  const logout = (input) => ({
    "query": `mutation RevokeToken($data: String!){ 
        revokeToken(refreshToken: $data) 
        { 
          payload refreshExpiresIn token 
        }
      }`,
    "variables": {data: input}
  })
  