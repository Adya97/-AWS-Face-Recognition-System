import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('lionel-messi.jpg','Leo Messi'),
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('famousperson-img','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})