from selenium import webdriver
import boto3
import time
s3 = boto3.client('s3',
                  aws_access_key_id='AKIA2FGJ6YNGJ5RMW7RX',
                  aws_secret_access_key='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',
                  region_name='us-east-2')
driver = webdriver.Chrome()
driver.get("https://aws.amazon.com/")
driver.save_screenshot("screeshot_aws_website2.png")
bucket_name = 'sel-test-bucket'
object_name = 'screeshot_aws_website2.png'
s3.upload_file('screeshot_aws_website2.png', bucket_name, object_name)

time.sleep(5)
driver.quit()