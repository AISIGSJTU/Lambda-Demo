FROM public.ecr.aws/lambda/python:3.8

RUN pip install torch==1.10.0+cpu torchvision==0.11.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

CMD [ "app.handler" ]
