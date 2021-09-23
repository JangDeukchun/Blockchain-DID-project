import asyncio
import json
import pprint

from indy import pool,ledger,wallet,did,anoncreds
from indy.error import IndyError, ErrorCode

from utils import get_pool_genesis_txn_path, PROTOCOL_VERSION
# import write_did_and_query_verkey as fn1


import negotiate_proof as fn1



from flask import Flask, request

pool_name = 'BoomLedgerPool'
genesis_file_path = get_pool_genesis_txn_path(pool_name)

wallet_config = json.dumps({"id": "wallet"})
wallet_credentials = json.dumps({"key": "wallet_key"})

def print_log(value_color="", value_noncolor=""):
   HEADER = '\033[92m'
   ENDC = '\033[0m'
   print(HEADER + value_color + ENDC + str(value_noncolor))

app = Flask(__name__)

@app.route("/")
def main():
   return "<h1>Hello world!</h1>"



@app.route('/a', methods=['POST'])
async def func1():
  if request.is_json :
    params = request.get_json() #서버에서 보내준 회원의정보
  # await fn5.proof_negotiation()
  e =  await fn1.proof_negotiation(params)
  return e


# @app.route('/e', methods=['POST'])
# async def func5():
#   if request.is_json :
#     params = request.get_json() #서버에서 보내준 회원의정보
# #   await fn5.proof_negotiation()
#   e =  await fn5.proof_negotiation()
#   return params


host_addr = "0.0.0.1"
port_num = "3000"

if __name__ == "__main__":
   app.run(host=host_addr,port=port_num)