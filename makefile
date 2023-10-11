
deploy:
	gcloud functions deploy GA4_list_users \
	--gen2 \
	--project=ga4-analytics-352613 \
	--region=europe-west2 \
	--runtime=python310 \
	--source=. \
	--entry-point=run