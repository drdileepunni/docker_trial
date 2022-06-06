

def lambda_handler(event, context):

    # Gathering data from event
    data = event.get('data')

    return {
        'statusCode': 200,
        'body': data
    }

#f=open("lambda_trial.json",)
#event= json.load(f)
#f.close()
#output=lambda_handler(event,None)
#print(output)
