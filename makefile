-include .env

deploy:
	gcloud functions deploy GA4_list_users \
	--gen2 \
	--project=$(GCP_PROJECT_ID) \
	--region=europe-west2 \
	--runtime=python310 \
	--source=. \
	--entry-point=run