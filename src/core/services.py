from contextlib import suppress
from typing import Optional

from asgiref.sync import sync_to_async

from .domain import CurrencyExchangeRateDTO
from .interfaces import AlphaVantageInterface
from .models import CurrencyExchangeRate


class CurrencyExchangeRatesCRUD:
    """This service uses for communicating with database.
    Django ORM uses as a repository pattern.
    """

    @staticmethod
    @sync_to_async
    def last() -> Optional[CurrencyExchangeRateDTO]:
        with suppress(CurrencyExchangeRate.DoesNotExist, AttributeError):
            instance = CurrencyExchangeRate.objects.last()
            return CurrencyExchangeRateDTO(**instance.__dict__)

    @staticmethod
    @sync_to_async
    def create(payload: CurrencyExchangeRateDTO) -> Optional[CurrencyExchangeRate]:
        with suppress(AttributeError):
            instance = CurrencyExchangeRate.objects.create(**payload.dict())
            return CurrencyExchangeRateDTO(**instance.__dict__)

    @staticmethod
    @sync_to_async
    def count() -> Optional[int]:
        return CurrencyExchangeRate.objects.count()


class ExchangeRatesService:
    """Base currencies exchange rates."""

    @classmethod
    async def fetch_exchange_rates_from_alpha_vantage(cls) -> CurrencyExchangeRateDTO:
        """Retrun the converted to internal object AlphaVantage fetching response."""

        payload: dict = await AlphaVantageInterface.fetch_exchange_rates()
        return CurrencyExchangeRateDTO(**payload)

    @classmethod
    async def update_exchange_rates(cls) -> None:
        """Fetch exchange rates and do a new database commit."""

        payload = await cls.fetch_exchange_rates_from_alpha_vantage()
        return await CurrencyExchangeRatesCRUD.create(payload)

    @classmethod
    async def get_last_exchange_rate(cls) -> dict:
        """Return the latest exchange rates from the database."""

        last_currency_exchange_rate: CurrencyExchangeRateDTO = await CurrencyExchangeRatesCRUD.last()

        if not last_currency_exchange_rate:
            return await cls.get_fresh_exchange_rates()

        return last_currency_exchange_rate

    @classmethod
    async def get_fresh_exchange_rates(cls) -> dict:
        """Update currency exchange via AlphaVantage and return."""

        exchange_rates: CurrencyExchangeRateDTO = await cls.update_exchange_rates()
        return exchange_rates
