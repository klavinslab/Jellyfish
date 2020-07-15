import argparse
import pandas as pd
import plan_experiment as plan_experiment
from agavepy.actors import get_context, get_client, send_bytes_result

def main():
    print("Got JSON.")
    context = get_context()
    server = context['message_dict']['server']
    file = context['message_dict']['file']
    name = context['message_dict']['name']
    temp = context['message_dict']['temp']
    plate = context['message_dict']['plate']
    print("JSON recieved has values", server, file, name, temp, plate)
    plan_experiment.main(server, file, name, temp, plate)


if __name__ == '__main__':
  main()
