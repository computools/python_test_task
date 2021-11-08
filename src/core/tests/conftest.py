from decimal import Decimal
from unittest.mock import AsyncMock

import pytest
from core.domain import CurrencyExchangeRateDTO
from django.urls import reverse


@pytest.fixture
def retrieve_currency_exchange_rates_url() -> str:
    return reverse("core:currency_exchange_rate_retrieve")


@pytest.fixture
def mock_alphavantage_fetch_exchange_rates(mocker):
    data = {
        "1. From_Currency Code": "BTC",
        "2. From_Currency Name": "Bitcoin",
        "3. To_Currency Code": "USD",
        "4. To_Currency Name": "United States Dollar",
        "5. Exchange Rate": "60867.16",
        "6. Last Refreshed": "2021-11-05 17:05:01",
        "7. Time Zone": "UTC",
        "8. Bid Price": "60869.18",
        "9. Ask Price": "60871.45",
    }

    mocker.patch("core.interfaces.AlphaVantageInterface.fetch_exchange_rates", side_effect=AsyncMock(return_value=data))


@pytest.fixture
def mocked_currency_exchange_rate() -> CurrencyExchangeRateDTO:
    return CurrencyExchangeRateDTO(currency_from="BTC", currency_to="USD", rate=Decimal("60867.16"))
