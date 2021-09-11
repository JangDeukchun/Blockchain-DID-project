import asyncio
import json
import pprint

from indy import pool,ledger,wallet,did,anoncreds
from indy.error import IndyError, ErrorCode

from utils import get_pool_genesis_txn_path, PROTOCOL_VERSION


import walletcreate as fn1
import schemacreate as fn2
import VC as fn3
import VP as fn4
import verify as fn5



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

@app.route("/a")
async def func1():
   await fn1.write_nym_and_query_verkey()
  
   return "<h1>rotate_key</h1>"

@app.route("/b")
async def func2():
  await fn2.schema_build_and_request()
  return "<h1>rotate_key</h1>"

    
   
@app.route("/c")
async def func3():
  await fn3.VC()
  return "<h1>save schema</h1>" 


@app.route("/d")
async def func4():
  await fn4.VP()
  return "<h1>issue credential<h1>"

@app.route("/E")
async def func5():
  await fn5.verify()
  return "<h1>issue credential<h1>"





# @app.route('/e', methods=['POST'])
# async def func5():
#   if request.is_json :
#     params = request.get_json() #서버에서 보내준 회원의정보
#   # await fn5.proof_negotiation()
#   e =  await fn5.proof_negotiation(params)
#   return e







host_addr = "127.0.0.1"
port_num = "8080"

if __name__ == "__main__":
   app.run(host=host_addr,port=port_num)