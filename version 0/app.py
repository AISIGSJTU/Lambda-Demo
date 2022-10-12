import torch


def handler(event, context):
    ones = torch.ones([1,2,3])
    shape = ones.shape
    message = 'Hello {}!'.format(shape)  
    return { 
        'message' : message
}