import boto3 # importing boto3 module



dynamodb = boto3.resource('dynamodb',
    aws_access_key_id='AKIAQUVMAJA3M2HTIREW', #insert your aws_access_key_id
    aws_secret_access_key='4wpwr2jO+9817HNdDvTKNznkaHEDiSAHZSuhigfd') #in


table = dynamodb.Table('great_guitar_albums') #variable to hold table name

with table.batch_writer() as batch: #batch writing 10 items
    
    batch.put_item(
        Item={
            'album': 'The Essential Stevie Ray Vaughan and Double Trouble ',
            'artist': 'Stevie Ray Vaughan and Double Trouble'
            }
        )
    batch.put_item(
        Item={
            'album': 'Led Zeppelin 4',
            'artist': 'Led Zeppelin'
            }
        )
    batch.put_item(
        Item={
            'album': 'Are You Experienced',
            'artist': 'Jimi Hendrix'
            }
        )
    batch.put_item(
        Item={
            'album': 'Dark Side Of The Moon',
            'artist': 'Pink Floyd'
            }
        )
    batch.put_item(
        Item={
            'album': 'Appetite for Destruction',
            'artist': 'Guns n Roses'
            }
        )
    batch.put_item(
        Item={
            'album': 'Lucille',
            'artist': 'BB King'
            }
        )
    batch.put_item(
        Item={
            'album': 'Back in Black',
            'artist': 'AC/DC'
            }
        )
    batch.put_item(
        Item={
            'album': 'Revolver',
            'artist': 'The Beatles'
            }
        )
    batch.put_item(
        Item={
            'album': 'Nevermind',
            'artist': 'Nirvana'
            }
        )
    batch.put_item(
        Item={
            'album': 'Van Halen',
            'artist': 'Van Halen'
            }
        ) 
  