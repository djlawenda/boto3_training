import boto3  

# Let's use Amazon S3 

ec2 = boto3.resource('ec2')

# Print out bucket names 

for instance in ec2.instances.all():     
    print(instance.id, instance.state, instance.tags)
