# Run Alembic Migration

1. Run `alembic revision -m "describe change"`. This command generates a revision file in migration/versions directory
2. Define the schema change in `upgrade` and/or `downgrade` function
3. Copy the new version at the top of the version file and update the `CURRENT_ALEMBIC_VERSION` in `metadata_db_dependency.py`
4. Update the relevant SQLAlchemy classes
5. Run `alembic upgrade head`