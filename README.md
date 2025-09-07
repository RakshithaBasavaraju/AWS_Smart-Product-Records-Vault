📦 AWS Smart Product Records Vault

A cloud-based product management system that allows users to add and view product details using AWS Lambda, DynamoDB, API Gateway, and a responsive HTML/JavaScript frontend. The project showcases serverless architecture and provides efficient, scalable storage and retrieval of product information.

✅ Features

✅ Add new products with productCode, price, description, and createdAt.

✅ List all products in a user-friendly table.

✅ Search products by code, price, or description.

✅ Fully serverless solution using AWS services.

✅ Lightweight and easily extendable for more functionality.

🛠 Technology Stack

AWS Lambda – Serverless compute to handle backend logic.

Amazon DynamoDB – NoSQL database to store product information.

API Gateway – Exposes Lambda functions through HTTP endpoints.

HTML/CSS/JavaScript – User interface for interacting with the backend.

📂 Project Structure


<img width="796" height="201" alt="image" src="https://github.com/user-attachments/assets/571d8bdd-de0e-4353-8ab9-ae01795874dc" />


⚙ Setup Instructions
✅ DynamoDB Setup

Create a DynamoDB table named product.

Set the primary key as productCode (String).

No need to define other attributes; they are dynamically added per item.

✅ Lambda Function Setup

Create a new Lambda function in AWS using Python 3.x.

Copy the lambda_function.py code into the Lambda editor.

Attach an IAM role with permissions to read/write from DynamoDB (AmazonDynamoDBFullAccess or scoped permissions).

✅ API Gateway Setup

Create a new API (HTTP API recommended).

Configure a route like /getData with POST method.

Integrate the API route with your Lambda function.

Deploy and note the endpoint URL (replace API_URL in the frontend code).

✅ Frontend Setup

Replace YOUR_API_GATEWAY_URL in index.html with your API Gateway endpoint.

Open index.html in your browser to start interacting with the app.

📥 Usage

Fill in the product details and click Add Product to store it.

The list of products will automatically update.

Use the search bar to filter products by code, description, or price.

Products are stored permanently in DynamoDB and can be accessed from anywhere.

📦 Example Request Formats
<img width="836" height="545" alt="image" src="https://github.com/user-attachments/assets/dcd5e59b-0f92-4e39-ba59-2636fa8814c1" />


🚀 Future Improvements

Add update and delete operations.

Implement user authentication using AWS Cognito.

Enable pagination for large datasets.

Add image upload functionality using S3.

📄 License

This project is open-source and available for educational and demonstration purposes.
