const verifyRequest = (data) => ({
    "query": `mutation VerifyToken($token: String!){ 
        verifyToken(token: $token) 
        { 
          payload
        }
      }`,
    "variables": {token: data}
  })
  
  