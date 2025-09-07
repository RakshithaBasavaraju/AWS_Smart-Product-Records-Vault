
import json
import boto3
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('product')  # Ensure this matches your actual table name

def lambda_handler(event, context):
    operation = event.get('operation', '')

    if operation == 'addProduct':
        return saveProduct(event)
    elif operation == 'listProduct':
        return getProducts()
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid operation')
        }

def saveProduct(event):
    gmt_time = time.gmtime()
    now = time.strftime('%a, %d %b %Y %H:%M:%S', gmt_time)

    # Get all required fields from event
    product_code = event.get('productCode')
    price = event.get('price')
    description = event.get('description', '')

    # Insert into DynamoDB
    table.put_item(
        Item={
            'productCode': product_code,
            'price': price,
            'description': description,
            'createdAt': now
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Product with ProductCode : ' + product_code + ' created at ' + now)
    }

def getProducts():
    response = table.scan()
    items = response.get('Items', [])

    return {
        'statusCode': 200,
        'body': json.dumps(items),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
