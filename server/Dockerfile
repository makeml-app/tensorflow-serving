FROM tensorflow/serving

# Define metadata
LABEL author="MakeML"
LABEL version="1.0"
LABEL description="Deploy tensorflow object detection model with MakeML"

# Copy model
WORKDIR /models
RUN mkdir -p object-detect/1
RUN mkdir -p object-detect/1/variables
ADD model/saved_model.pb object-detect/1/

EXPOSE 80
ENTRYPOINT ["tensorflow_model_server", "--model_base_path=/models/object-detect"]
CMD ["--rest_api_port=80","--port=81"]
