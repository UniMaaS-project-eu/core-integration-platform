from app.services.errors import missing_contract


def list_infrastructure_assets() -> None:
    missing_contract(
        component="IC5 Resource Monitoring Engine",
        missing_inputs=["API spec", "Data model", "Polling vs streaming expectation", "Asset identifiers", "Auth"],
    )

