NAME=udemy-ml-api
COMMIT_ID=$(shell git rev-parse HEAD)

build-ml-api-aws:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t $(NAME):latest .

tag-ml-api:
	docker tag $(NAME):latest ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-2.amazonaws.com/$(NAME):latest

push-ml-api-aws:
	docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-2.amazonaws.com/$(NAME):latest

