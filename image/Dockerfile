FROM public.ecr.aws/lambda/python:3.11

RUN chmod -R 755 ${LAMBDA_TASK_ROOT}

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip3 install -r requirements.txt

# Copy all files in ./src
COPY src/ ${LAMBDA_TASK_ROOT}

RUN python main.py

# Set the CMD to your handler.
CMD [ "main.handler" ]