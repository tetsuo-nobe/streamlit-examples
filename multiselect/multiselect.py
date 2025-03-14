import streamlit as st


st.set_page_config(layout='wide')

service_names = list([
    'Amazon EC2', 
    'Amazon S3', 
    'Amazon RDS', 
    'Amazon VPC', 
    'AWS IAM',
    'AWS Lambda', 
    'Amazon DynamoDB',
    'AWS Step Functions',
    'Amazon SQS', 
    'Amazon SNS', 
    'AWS CloudFormation', 
    'Amazon Bedrock']
)


selected_services = st.multiselect(
    label='好きな AWS サービスを選択してください',
    options=service_names,
    help='ここにリストされているサービス名は抜粋されたものです。')

# リストのアイテムが選択されたか否かは len 関数で確認する。 is not None では正しく判定できない。
if len(selected_services) > 0:
   st.markdown('あなたが選択した AWS サービス')
   for service in selected_services:
       st.markdown(service)