# import jwt
# import time

# def generate_token():
#     with open("AuthKey_39YY8DQPHQ.p8", "r") as f:
#         private_key = f.read().encode('utf-8')
#         team_id = "7KA9SCJT3Y"
#         client_id = "com.inpaket.store"
#         key_id = "39YY8DQPHQ"
#         validity_minutes = 20
#         timestamp_now = int(time.time())
#         timestamp_exp = timestamp_now + (60 * validity_minutes)
#         # Assuming `last_token_expiration` is a class variable defined somewhere else
#         # cls.last_token_expiration = timestamp_exp
#         data = {
#             "iss": team_id,
#             "iat": timestamp_now,
#             "exp": timestamp_exp,
#             "aud": "https://appleid.apple.com",
#             "sub": client_id
#         }
#         token = jwt.encode(
#             payload=data,
#             key=private_key,
#             algorithm="ES256",
#             headers={"kid": key_id, "alg": "ES256"}
#         )
#         print(token)  # Decode bytes to string for printing

# generate_token()



from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import jwt
import time

app = FastAPI()

@app.get("/generate_token")
def generate_token():
    with open("AuthKey_39YY8DQPHQ.p8", "r") as f:
        private_key = f.read().encode('utf-8')
        team_id = "7KA9SCJT3Y"
        client_id = "com.inpaket.store"
        key_id = "39YY8DQPHQ"  # Replace with the desired key_id
        validity_minutes = 20
        timestamp_now = int(time.time())
        timestamp_exp = timestamp_now + (60 * validity_minutes)

        data = {
            "iss": team_id,
            "iat": timestamp_now,
            "exp": timestamp_exp,
            "aud": "https://appleid.apple.com",
            "sub": client_id
        }

        token = jwt.encode(
            payload=data,
            key=private_key,
            algorithm="ES256",
            headers={"kid": key_id, "alg": "ES256"}
        )

        return JSONResponse(content={"client_secret": token})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5000)
