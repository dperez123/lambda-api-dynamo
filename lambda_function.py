import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('company')

    try:
        http_method = event['httpMethod']
        
        if http_method == 'GET':
            try:
                response = table.scan()
                items = response['Items']

                return {
                    'statusCode': 200,
                    'body': json.dumps(items)
                }
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps(str(e))
                }
        elif http_method == 'POST':
            try:
                payload = json.loads(event['body'])

                item = {
                    'name': payload['name'],
                    'website': payload['website'],
                    'size': payload['size']
                }

                table.put_item(Item=item)

                return {
                    'statusCode': 200,
                    'body': json.dumps('Item inserted successfully')
                }
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps(str(e))
                }
        elif http_method == 'DELETE':
            try:
                payload = json.loads(event['body'])
                # query the name of the company
                response = table.query(
                    KeyConditionExpression='#company_name = :name',
                    ExpressionAttributeNames={
                        '#company_name': 'name'  # Alias for the reserved keyword
                        },
                    ExpressionAttributeValues={
                        ':name': payload['name']
                    }
                )
                if len(response['Items']) == 0:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Item not found')
                    }
                # delete the item
                table.delete_item(
                    Key={
                        'name': payload['name'],
                        'website': payload['website']
                    }
                )

                return {
                    'statusCode': 200,
                    'body': json.dumps('Item deleted successfully')
                }
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps(str(e))
                }
                
        elif http_method == 'PUT':
            try:
                payload = json.loads(event['body'])
                # query the name of the company
                response = table.query(
                    KeyConditionExpression='#company_name = :name',
                    ExpressionAttributeNames={
                        '#company_name': 'name'  # Alias for the reserved keyword
                        },
                    ExpressionAttributeValues={
                        ':name': payload['name']
                    }
                )
                if len(response['Items']) == 0:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Item not found')
                    }
                # update the item
                item = {
                    'name': payload['name'],
                    'website': payload['website'],
                    'size': payload['size']
                }

                table.put_item(Item=item)

                return {
                    'statusCode': 200,
                    'body': json.dumps('Item updated successfully')
                }
            
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps(str(e))
                }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid HTTP method')
            }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing HTTP method')
        }
