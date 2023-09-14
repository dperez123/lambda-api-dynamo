# Lambda, DynamoDB, and API Gateway Example

This is an example README for a serverless application using AWS Lambda, DynamoDB, and API Gateway. The provided code is a Python Lambda function that interacts with a DynamoDB table to perform CRUD (Create, Read, Update, Delete) operations on company records. It exposes these operations through an API Gateway.

## Overview

This example demonstrates how to create a serverless RESTful API for managing company information using AWS Lambda and DynamoDB. The API provides the following functionality:

- **GET**: Retrieve a list of all companies.
- **POST**: Create a new company record.
- **PUT**: Update an existing company record.
- **DELETE**: Delete a company record.

## Prerequisites

Before deploying this application, ensure that you have the following prerequisites in place:

1. **AWS Account**: You need an AWS account to create and manage Lambda functions, DynamoDB tables, and API Gateway resources.

2. **AWS CLI**: Install and configure the AWS Command Line Interface (CLI) to deploy and manage AWS resources.

3. **Python**: Ensure that you have Python installed, as the Lambda function is written in Python.

## Deployment

Follow these steps to deploy the application:

1. **Create a DynamoDB Table**:
   - Create a DynamoDB table named `company` with a primary key attribute `name`. You can configure this table with provisioned or on-demand capacity as per your needs.

2. **Create a Lambda Function**:
   - Create an AWS Lambda function using the provided code. Ensure that the Lambda function has permissions to access the DynamoDB table.

3. **Create an API Gateway**:
   - Create an API Gateway and define the RESTful API endpoints for each HTTP method (GET, POST, PUT, DELETE). Configure the integration of these endpoints with your Lambda function.

4. **Deploy the API**:
   - Deploy the API to make it accessible via a public URL. This URL will be used to access your company management API.

5. **Test Your API**:
   - Use tools like `curl`, Postman, or any HTTP client to test the API endpoints:
     - `GET`: Retrieve a list of all companies.
     - `POST`: Create a new company record.
     - `PUT`: Update an existing company record.
     - `DELETE`: Delete a company record.

## Usage

Here's how you can use the API:

### GET /companies

Retrieve a list of all companies.

Example Request:
```http
GET /companies
```

### POST /companies

Create a new company record.

Example Request:
```http
POST /companies
Content-Type: application/json

{
    "name": "Example Corp",
    "website": "https://example.com",
    "size": "Large"
}
```

### PUT /companies

Update an existing company record.

Example Request:
```http
PUT /companies
Content-Type: application/json

{
    "name": "Updated Corp",
    "website": "https://updated.com",
    "size": "Medium"
}
```

### DELETE /companies

Delete a company record.

Example Request:
```http
DELETE /companies
Content-Type: application/json

{
    "name": "Example Corp",
    "website": "https://example.com"
}
```

## Error Handling

The API provides basic error handling, including validation of HTTP methods and handling exceptions. Responses are returned with appropriate status codes and error messages.

## Conclusion

This example demonstrates how to create a simple serverless API for managing company information using AWS Lambda, DynamoDB, and API Gateway. You can further enhance this application by adding authentication, authorization, and additional features as needed for your use case.
