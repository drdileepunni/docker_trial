

def lambda_handler(event, context):

    # Gathering data from event
    data = event.get('data')
    print(data)

    report_json = {
	"Hi there": "Hello"
	}
    return {
        'statusCode': 200,
        'body': report_json
    }

#f=open("lambda_trial.json",)
#event= json.load(f)
#f.close()
#output=lambda_handler(event,None)
#print(output)
