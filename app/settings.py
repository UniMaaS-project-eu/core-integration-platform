from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    request_timeout_seconds: float = 10.0

    ic1_edc_base_url: str | None = None
    ic1_edc_auth_token: SecretStr | None = None

    ic3_knowledge_graph_base_url: str | None = None
    ic3_knowledge_graph_auth_token: SecretStr | None = None

    ic4_federated_catalogue_base_url: str | None = None
    ic4_federated_catalogue_auth_token: SecretStr | None = None

    ic5_resource_monitoring_base_url: str | None = None
    ic5_resource_monitoring_auth_token: SecretStr | None = None

    ic6_iam_governance_base_url: str | None = None
    ic6_iam_governance_auth_token: SecretStr | None = None

    ic7_dpp_base_url: str | None = None
    ic7_dpp_auth_token: SecretStr | None = None

    ic11_chatbot_base_url: str | None = None
    ic11_chatbot_auth_token: SecretStr | None = None

    ic15_orchestrator_base_url: str | None = None
    ic15_orchestrator_auth_token: SecretStr | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()

