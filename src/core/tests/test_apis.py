import pytest
from core.services import CurrencyExchangeRatesCRUD

pytestmark = pytest.mark.django_db


@pytest.mark.asyncio
async def test_alphvantage_response(
    retrieve_currency_exchange_rates_url, mock_alphavantage_fetch_exchange_rates, mocked_currency_exchange_rate, client
):
    response = await client.get(retrieve_currency_exchange_rates_url)
    expected_response = mocked_currency_exchange_rate.as_json()

    assert response.status_code == 200
    assert response.json() == expected_response
    assert await CurrencyExchangeRatesCRUD.count() == 1


@pytest.mark.asyncio
async def test_alphvantage_extra_population(
    retrieve_currency_exchange_rates_url, mock_alphavantage_fetch_exchange_rates, mocked_currency_exchange_rate, client
):
    response = await client.post(retrieve_currency_exchange_rates_url)
    expected_response = mocked_currency_exchange_rate.as_json()

    assert response.status_code == 200
    assert response.json() == expected_response
    assert await CurrencyExchangeRatesCRUD.count() == 2
