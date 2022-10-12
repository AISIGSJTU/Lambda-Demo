FROM myruntime:base

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}
COPY alexnet_cifar10.py ${LAMBDA_TASK_ROOT}

CMD [ "app.handler" ]
