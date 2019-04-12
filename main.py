import remora_client
import remora_server
import  time

remora_server.server()

time.sleep(0.1)
remora_client.client()