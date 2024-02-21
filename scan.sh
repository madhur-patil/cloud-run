#!/bin/bash
set -e
project_id=$1

project_roles=$(gcloud projects get-iam-policy $project_id)
echo $project_roles
